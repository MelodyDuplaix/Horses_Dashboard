# Import des bibliothèques
import streamlit as st
from PIL import Image
import pandas as pd
from bibliotheque.lib import  *
from datetime import datetime 
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
import numpy as np


# config de pages
st.set_page_config(
    page_title="Analyse associations",
    page_icon="📊",
    layout="wide",
    menu_items={
        "Get Help": "https://www.cefim.eu/",
        "About" : "https://www.linkedin.com/in/melody-duplaix-391672265"
    }
)



# Application du style css
formatage_de_la_page("style.css")
st.set_option('deprecation.showPyplotGlobalUse', False)

# titre, contexte et logos
contexte = "Ce tableau de bord vise à vous fournir un aperçu complet de la population de chevaux dans le pays, en mettant en lumière des informations clés"
st.title("Population équine en France :horse:")
st.write(contexte)



# contenu pincipal

# KPI
colonne1, colonne2 = st.columns(2)
with colonne1:
    st.metric(label="Nombre de chevaux en 2023", value=nombre_de_chevaux())
with colonne2:
    st.metric(label="Age moyen des chevaux en 2023", value=f"{age_moyen()} ans")

# Graphiques

colonnepie, colonnehisto = st.columns(2)
with colonnepie:
    st.markdown("<h2>Élevage de Chevaux : Forte Présence de Juments</h2>", unsafe_allow_html=True)
    "Nombre de chevaux par sexe en 2023"
    st.plotly_chart(camembert(), use_container_width=True)
    st.markdown("<font color='#4e8e8e'>M: Entiers</font><br><font color='#8e8282'>F: Juments</font><br><font color='#6ecece'>H: Hongres</font>", unsafe_allow_html=True)
with colonnehisto:
    st.markdown("<h2>Races de Chevaux : Majorité Inconnues</h2>", unsafe_allow_html=True)
    "proportion des races des chevaux en 2023"
    st.plotly_chart(histogram(), use_container_width=True)
    
colonneline, colonnenuage = st.columns(2)
with colonneline:
    st.markdown("<h2>Saisonnalité de Reproduction et Tendance par année</h2>", unsafe_allow_html=True)
    "Nombre de naissance par année et par mois de 1960 à 2022"
    st.plotly_chart(courbe(), use_container_width=True)
with colonnenuage:
    st.markdown("<h2>Noms les Plus Courants : Un Nuage de Mots Équins</h2>", unsafe_allow_html=True)
    "Noms des chevaux selon leur fréquence de 1985 à aujourd'hui"
    st.pyplot(nuage_mot(), use_container_width=True)
    
    
st.markdown("Ces données sont issues du fichier des équidés du SIRE(Système d'Information Répertoriant les Equidés), disponibles à cette adresse : [Fichier des équidés - data.gouv.fr](https://www.data.gouv.fr/fr/datasets/fichier-des-equides/#/discussions) ")