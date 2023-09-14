import streamlit as st
import pandas as pd
import numpy as np
import os

current_path = os.path.dirname(os.path.abspath(__file__))
confmat = os.path.join(current_path, '../assets/tab_5/normalized_confusion_matrix.png')
accgain = os.path.join(current_path, '../assets/tab_5/accuracy_gain.png')
kappa = os.path.join(current_path, '../assets/tab_5/kappa_coeff.png')
accev = os.path.join(current_path, '../assets/tab_5/accuracy_evolution.png')
title = "Résultats"
sidebar_name = "Résultats"


def run():

    st.title(title)

    st.image(accev)
    st.write("""
             La précision initiale calculée sur le vote des 3 modèles initiaux, l'entraînement sur HbR a rendu 3 modèles valides, 5 sur Hbo, 4 sur EEG.
             Les pente générale sur les données de test et celles de validation sont relativement
             proches donc il n'y a pas d'overfitting conséquent. On en déduit également que les données de validation sont représentatives des données de test.
             Plusieurs répétitions avec des random_state différents accréditent cette affirmation.""")
    
    st.image(confmat)      
    st.write("""Globalement, le modèle semble le mieux performer sur la classe "Bras droit", avec une précision de 89%. Les classes les plus confondues sont "Bras gauche" avec "Bras droit", et "Main gauche" avec "Main droite".
                \n\nCela suggére que le modèle a plus de difficultés à distinguer la gauche de la droite plutôt qu'à distinguer les bras des mains.
             """)
    
    st.image(accgain)
    st.write("""
             Notre système nous permet un boost de .1 sur les données de validation.
             """)
    st.image(kappa)
