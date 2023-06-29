import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pyvista as pv
import mne
from pathlib import Path
from mne.datasets import sample

title = "The basics of EEG"
sidebar_name = "The basics of EEG"

def run():

    st.title(title)
    st.write("""
    ## What is Electroencephalography (EEG)?""")
    col1, col2 = st.columns(2)  # Crée deux colonnes

    with col1:  # Dans la colonne de droite
        st.write("""

        Electroencephalography, or EEG, is a non-invasive method to record electrical activity of the brain. Developed in the early 20th century, it has become a fundamental tool in the fields of neurology, psychology, and cognitive sciences.

        Whenever we think, dream, feel, or move, our neurons, communicate through electrical impulses. These impulses create patterns of electrical activity that we can capture through electrodes placed on the scalp.
        """)
    with col2:  # Dans la colonne de gauche
        st.image('https://zupimages.net/up/23/26/bl8v.png')

    st.write("""
    An EEG records these patterns, usually as wavy lines. These oscillations, referred to as 'brain waves', are a window into our brain's functioning, offering insights into different states of consciousness like sleep, alertness, and relaxation.
    """)

    st.image('https://www.diygenius.com/wp-content/uploads/2022/12/brainwave-frequencies-chart.jpg', caption = 'Brain waves frequencies and their associated mental state')
    st.write("""

    Our project, harnesses the power of EEG to study motor execution - specifically the intention to move our body. We utilize machine learning techniques to sift through the complex patterns in the EEG data, and classify those signals that correspond to our arms and hands movement intentions.
    """)

