import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import os



import streamlit as st

title = "Second tab"
sidebar_name = "Analyse et visualisation des données"
current_path = os.path.dirname(os.path.abspath(__file__))
imageorgadata =os.path.join(current_path, "/mount/src/eeg/streamlit_app/assets/tab_2/orgadata.png")
image = os.path.join(current_path, "../assets/tab_2/eeg_raw.png")
gif = os.path.join(current_path, "../assets/tab_2/Gif_evoked_RightHand.mp4")


def run():
    # Affichage du titre
    st.title("Analyse et visualisation des datas")

    # Affichage du titre
    st.header("Les données")

    # Affichage du texte descriptif
    st.write("- Les données de chacun des participants étaient stockées dans un fichier matlab.\n"
            "- Leur extraction et l’utilisation de la librairie MNE nous a permis de les séparer  \n en « epoch ».\n"
            """- Chaque epoch correspond à la fenêtre temporelle durant laquelle le participant  \n réalisait une condition expérimentale (repos ou l’un des 4 mouvements ou \n l’indication du début d’une séquence expérimentale).""")
    st.image(imageorgadata)
    # Affichage du titre
    st.header("Premières visualisations")

    st.write("A l’aide de la librairie MNE et de la commande plot_raw, il est possible d’observer \nl’amplitude du signal pour l’ensemble des électrodes d’enregistrement : ")

    # Affichage de l'image
    st.image(image)


    # Affichage du titre diapo 3 et 4
    st.header("Premières visualisations (EEG)")

    st.write("Il est également possible d’observer le signal de chaque électrode ou capteur,\nmoyenné pour une condition particulière : ")


    # Options du menu déroulant
    options = ['EEG', 'NIRS']
    selected_option = st.selectbox('Sélectionnez le type de signaux à afficher', options)

    if selected_option == 'EEG':
        # Affichage des 4 images EEG
        image1 = os.path.join(current_path,"../assets/tab_2/EEG1.png")
        image2 = os.path.join(current_path,"../assets/tab_2/EEG2.png")
        image3 = os.path.join(current_path,"../assets/tab_2/EEG3.png")
        image4 = os.path.join(current_path,"../assets/tab_2/EEG4.png")
        st.image([image1, image2], caption=['Main Gauche', 'Main Droite'])
        st.image([image3, image4], caption=['Bras Gauche', 'Bras Droit'])
    else:
        # Affichage des 4 images NIRS
        image1 = os.path.join(current_path,"../assets/tab_2/NIRS1.png")
        image2 = os.path.join(current_path,"../assets/tab_2/NIRS2.png")
        image3 = os.path.join(current_path,"../assets/tab_2/NIRS3.png")
        image4 = os.path.join(current_path,"../assets/tab_2/NIRS4.png")
        st.image([image1, image2], caption=['Main Gauche', 'Main Droite'])
        st.image([image3, image4], caption=['Bras Gauche', 'Bras Droit'])





    # Affichage du titre diapo 5
    st.header("Premières visualisations")

    st.write("Enfin, il est possible d’accéder à la dynamique des changements d’activité neuronale \nà l’aide de la fonction plot_topomap de MNE : ")
    st.video(gif)



    # Affichage du titre diapo 6
    st.header("Analyse fréquentielle du signal EEG")
    st.write("Il est également possible d’observer la densité  spectrale de puissance (ou PSD en \nanglais). Elle nous renseigne sur la répartition fréquentielle de la puissance \nd’un signal :")


    image_psd =  os.path.join(current_path,"../assets/PSD.png")
    st.image(image_psd)

    st.write("Rappel, rythmes physiologiques : delta (<4Hz), thêta (4-8Hz), alpha (8-12Hz,\nbêta (12 à 30 Hz) et gamma (>30Hz)")
