# Import des bibliothèques
import streamlit as st
from PIL import Image
import pandas as pd
from bibliotheque.lib import  *
import datetime 
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def formatage_de_la_page(fichier_css):
    with open(fichier_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_data
def nombre_de_chevaux():
    df = pd.read_csv("data/data_nettoye.csv")
    today = datetime.datetime.today()
    df["DATE_DE_NAISSANCE"] = pd.to_datetime(df["DATE_DE_NAISSANCE"], errors="coerce")
    df["DATE_DE_DECES"] = pd.to_datetime(df["DATE_DE_DECES"], errors="coerce")
    nombre = df[(df["DATE_DE_DECES"].notna())&(df["DATE_DE_NAISSANCE"]>today-datetime.timedelta(days=365*40))].shape[0]
    return nombre

@st.cache_data
def age_moyen():
    df = pd.read_csv("data/data_nettoye.csv")
    nombre = round(df['AGE'].mean(), 2)
    return nombre

@st.cache_data
def camembert():
    df = pd.read_csv("data/data_nettoye.csv")
    # Comptez le nombre de chevaux par sexe
    sex_counts = df[df["SEXE"]!="I"]['SEXE'].value_counts().reset_index()
    sex_counts.columns = ['Sexe', 'Nombre de Chevaux']
    # Couleurs personnalisées
    custom_colors = ['#8E8282','#4E8E8E','#6ECECE', '#7EA8A8', '#8E8282']
    # Créez un graphique en camembert pour la proportion des sexes en utilisant les couleurs personnalisées
    fig = px.pie(sex_counts, names='Sexe', values='Nombre de Chevaux',
                color_discrete_sequence=custom_colors)
    fig.update_traces(textinfo='percent+label', textposition='inside', textfont_color='white')
    fig.update_layout(showlegend=False)
    return fig

@st.cache_data
def histogram():
    df = pd.read_csv("data/data_nettoye.csv")
    # Supprimez les lignes avec des races nulles
    df_clean = df.dropna(subset=['RACE'])
    # Regroupez les catégories 'poney non const', 'selle non const' et 'origines const.' sous 'inconnus'
    df_clean['RACE'] = df_clean['RACE'].replace({'poney non const': 'inconnus',
                                                'selle non const': 'inconnus',
                                                'origines const.': 'inconnus',
                                                'origine const.': 'inconnus',
                                                'ane non const': 'inconnus',
                                                'or. inconnue': 'inconnus',
                                                'trait non const': 'inconnus',
                                                'oi type poney': 'inconnus',
                                                'chev. de selle': 'inconnus',
                                                'oi type trait': 'inconnus'})
    # Comptez le nombre de chevaux par race
    race_counts = df_clean['RACE'].value_counts().reset_index()
    race_counts.columns = ['Race', 'Nombre de Chevaux']
    # Triez les races par nombre de chevaux en ordre décroissant
    race_counts = race_counts.sort_values(by='Nombre de Chevaux', ascending=False)
    # Sélectionnez les 10 races les plus importantes et regroupez les autres sous "autres"
    top_10_races = race_counts.head(10)
    others_count = race_counts['Nombre de Chevaux'][10:].sum()
    others_df = pd.DataFrame({'Race': ['Autres'], 'Nombre de Chevaux': [others_count]})
    top_10_races = pd.concat([top_10_races, others_df], ignore_index=True)
    custom_colors = ['#2E2E2E', '#3E5E5E', '#4E8E8E', '#5EAEBE', '#6ECECE', '#7EA8A8', '#8E8282', '#9EADAD', '#AEA3A3', '#BE9E9E', '#CEB3B3']    
    # Créez un graphique en barres pour représenter la proportion des races et spécifiez les couleurs pour chaque barre
    fig = px.bar(top_10_races, x='Race', y='Nombre de Chevaux',
                color='Race', color_discrete_sequence=custom_colors)
    fig.update_layout(showlegend=False)
    fig.update_yaxes(title_text='', showticklabels=False)
    return fig


@st.cache_data
def courbe():
    df = pd.read_csv("data/data_nettoye.csv")
    df["DATE_DE_NAISSANCE"] = pd.to_datetime(df["DATE_DE_NAISSANCE"], errors="coerce")
    df["DATE_DE_DECES"] = pd.to_datetime(df["DATE_DE_DECES"], errors="coerce")
    # Supprimez les lignes avec des dates de naissance nulles
    df_clean = df.dropna(subset=['DATE_DE_NAISSANCE'])
    # Extrait l'année et le mois de la colonne 'DATE_DE_NAISSANCE'
    df_clean['Année'] = df_clean['DATE_DE_NAISSANCE'].dt.year
    df_clean['Mois'] = df_clean['DATE_DE_NAISSANCE'].dt.month
    # Filtrer les données pour commencer en 1960 et exclure l'année 2023
    df_clean = df_clean[(df_clean['Année'] >= 1960) & (df_clean['Année'] < 2023)]
    # Comptez le nombre de chevaux par mois et par année
    counts_by_month = df_clean.groupby(['Année', 'Mois']).size().reset_index(name='Nombre de Chevaux')
    # Créez un graphique en barres pour la variation saisonnière par mois
    fig = px.line(counts_by_month, x='Mois', y='Nombre de Chevaux', animation_frame='Année',
                 color_discrete_sequence=['#4E8E8E'])
    fig.update_layout(yaxis=dict(fixedrange=True,  # Fixer l'échelle de l'axe Y principal
            range=[0, counts_by_month['Nombre de Chevaux'].max()]))  # Définir une échelle fixe pour Y
    fig.update_yaxes(title_text='', showticklabels=False)
    return fig

@st.cache_resource
def nuage_mot():
    df = pd.read_csv("data/data_nettoye.csv")
    # Supprimez les lignes avec des noms nuls
    df_clean = df.dropna(subset=['NOM'])
    # Nettoyez les noms en supprimant "NOM NOMME" et "N."
    df_clean['NOM'] = df_clean['NOM'].str.replace('NON NOMME', '')
    df_clean['NOM'] = df_clean['NOM'].str.replace('N.', '')
    # Comptez la fréquence d'utilisation de chaque nom
    name_counts = df_clean['NOM'].value_counts()
    # Sélectionnez les 50 à 100 noms les plus utilisés
    top_names = name_counts.iloc[0:60]
    # Chargez l'image du cheval depuis votre dossier
    horse_mask = np.array(Image.open('images/image_horse4.jpg'))
    # Créez une palette de couleurs personnalisée avec des tons marrons, verts foncés, bleus foncés, gris foncés, etc.
    custom_colormap = plt.cm.colors.ListedColormap(['#2E2E2E', '#3E5E5E', '#4E8E8E', '#5EAEBE', '#6ECECE', '#7EA8A8', '#8E8282'])
    # Créez un nuage de mots avec les noms les plus utilisés et utilisez l'image du cheval comme masque
    wordcloud = WordCloud(width=900, height=1000, background_color='white', mask=horse_mask, min_font_size=2,
                        colormap=custom_colormap, collocations=False, prefer_horizontal=0.95).generate_from_frequencies(top_names)
    plt.figure(figsize=(10, 10))  # Ajustez la taille de la figure
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    return plt
