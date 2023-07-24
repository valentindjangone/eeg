import streamlit as st
import pandas as pd
import numpy as np


title = "Résultats"
sidebar_name = "Résultats"


def run():

    st.title(title)

    st.image("accuracy_evolution.png")
    st.image('normalized_confusion_matrix.png')       
    st.image('correct_incorrect.png')
    st.image('accuracy_gain.png')
    st.image('kappa_coeff.png')
