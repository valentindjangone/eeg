import streamlit as st
import os


title = "Projet DataScientest : Classification de signaux EEG et fNIRS."
sidebar_name = "Page d'accueil du projet"

def run():
    # Créez trois colonnes (gauche, centre, droite)
    left_column, center_column, right_column = st.beta_columns(3)

    # Afficher le gif dans la colonne du milieu
    center_column.image("https://media.giphy.com/media/lkdIhnHHnFma6xvICt/giphy-downsized-large.gif", width=400)

    st.title(title)
    st.markdown("---")

    st.markdown(
        """
        Bienvenue sur la page d'accueil du projet réalisé dans le cadre du projet fil rouge de la formation de Data Scientist chez Datascientest.
        Vous pouvez naviguer grâce au panneau latéral pour découvrir les différentes étapes réalisées tout au long de ce projet.
        """
    )