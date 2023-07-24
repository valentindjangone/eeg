import streamlit as st
import pandas as pd
import numpy as np


title = "Résultats"
sidebar_name = "Résultats"


def run():

    st.title(title)

    st.image("../images/accuracy_evolution.png")
    st.write("""
             La précision initiale calculée sur le vote des 3 modèles initiaux, l'entraînement sur HbR a rendu 3 modèles valides, 5 sur Hbo, 4 sur EEG.
             Les pente générale sur les données de test et celles de validation sont relativement
             proches donc il n'y a pas d'overfitting conséquent. On en déduit également que les données de validation sont représentatives des données de test.
             Plusieurs répétitions avec des random_state différents accréditent cette affirmation.""")
    
    st.image('../images/normalized_confusion_matrix.png')      
    st.write("""Globalement, le modèle semble le mieux performer sur la classe "Bras droit", avec une précision de 89%. Les classes les plus confondues sont "Bras gauche" avec "Bras droit", et "Main gauche" avec "Main droite".
                \n\nCela suggére que le modèle a plus de difficultés à distinguer la gauche de la droite plutôt qu'à distinguer les bras des mains.
             """)
    
    st.image('../images/accuracy_gain.png')
    st.write("""
             Notre système nous permet un boost de .1 sur les données de validation.
             """)
    st.image('../images/kappa_coeff.png')
