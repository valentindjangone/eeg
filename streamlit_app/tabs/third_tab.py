import streamlit as st
import mne
import matplotlib.pyplot as plt
import os


sidebar_name = "Preprocessing"

title = "Méthodes de Preprocessing utilisées"
text = """Le pretraitemement des données, ou preprocessing, est
indispensable à l'analyse des signaux EEG et NIRS. Il permet notamment
de s'étalonner par rapport aux électrodes de référence, de réduire les
bruits parasites, de supprimer les mauvais canaux, ou encore d'éliminer les
artéfacts de mouvement.
Les méthodes de preprocessing utilisées durant ce projet sont basées sur
celles proposées par les auteurs du dataset, ainsi que sur celles trouvées
dans d’autres articles scientifiques traitant de problématiques similaires.
"""

header_filtres = "Filtres numériques"
subheader_filtres = "Filtre passe-bande (passe-bas + passe-haut)"
txt_filtres = """Le filtre passe-haut laisse passer les hautes fréquences
et coupe les basses fréquences, par rapport à une fréquence de référence (fc
sur le schéma), et inversement pour le filtre basse-bas ; Tout simplement en
combinant les deux, on peut obtenir un filtre passe-bande ou bien un filtre
coupe-bande."""
img_filtres = "../assets/tab3/ExplicationFiltres.png"
text_filtreseeg= """Pour les données EEG, un filtre passe-haut de 0.01 HZ et un filtre
passe-bas de 24.49 Hz ont été appliqués. Ce sont des filtres utilisés de
manière conventionnelle dans l’analyse de signal EEG et qui permettent de
conserver les signaux physiologiques tout en retirant des bruits parasites
comme le 60Hz (courant du casque) par exemple."""

subheader_butterworth = "Filtre Butterworth"
text_butterworth= """Pour les données fNIRS, nous avons utilisé un filtre passe-bande
particulier, un filtre Butterworth d'ordre 4. Le gain de ce filtre est le
plus constant possible dans la bande passante et tend vers 0 dB dans la bande
de coupure. La fréquence pour le filtre passe-haut était de 0,01Hz et 0,2Hz pour
le filtre passe-bas.
"""
img_butterworth = "../assets/tab3/Butterworth_orders.png"

rawo = mne.io.read_raw_fif("../assets/tab3/S1_eeg.fif",preload=True)
rawo10 = rawo.copy()
rawo10.crop(tmax=10).load_data()

ph, pb =0.01, 24.49
min, max = 0.0, 80.0
step = 0.01

def _update_slider(value):
    st.session_state["filter_slider"] = value
    display_fig()
if "filter_slider" not in st.session_state:
    st.session_state["filter_slider"] = 0, 0

def display_fig():
    if st.session_state["filter_slider"] == 0:
        pht,pbt=ph,pb
    else:
        pht,pbt=st.session_state["filter_slider"]
    canal=st.session_state["select_canal"]
    raw=rawo10.copy()
    if st.session_state["check_butter"]:
        raw.filter(pht,pbt,method='iir', iir_params = None)
    else:
        raw.filter(pht,pbt)
    fig, ax = plt.subplots(figsize=(24, 12))
    ax.plot(raw.times, raw.get_data(picks=canal).squeeze()*1000000)
    plt.ylabel("Tension (microV)", fontsize=20)
    plt.xlabel("Temps (s)", fontsize=20)    
    return fig

def display_ica():
    rawica=rawo.copy()
    if st.session_state["radio_ica"] == "Pas de filtre et d'ICA":
        img_ica="../assets/tab3/EEGAvantFiltrage.png"
    else:
        img_ica="../assets/tab3/EEGApresFiltrage.png"
    return img_ica

header_ICA = "Independant Components Analysis sur les signaux EEG"
text_ICA = """L'analyse en composantes indépendantes ou ICA permet d’identifier
et supprimer les artefacts pouvant provenir de diverses sources, telles
que les mouvements oculaires, les battements du coeur, les bruits électriques,
etc... L'ICA permet de séparer ces sources artefactuelles des signaux
cérébraux d'intérêt, facilitant ainsi une meilleure interprétation et
analyse des données.
"""

header_concentration = "Concentration en HbO et HbR sur les signaux fNIRS"
text_concentration = """Les deux signaux utilisés en fNIRS correspondant à deux longueurs
d’onde (760 nm et 850 nm) ont également subi une transformation mathématique
pour les transformer en signaux de concentration d’hémoglobine oxygénée (HbO)
et d’hémoglobine désoxygénée (HbR). Cette transformation a été réalisée
en appliquant la loi de Beer-Lambert.
"""
img_absorption="../assets/tab3/AbsorptionHbOHbR.png"
hbo_righthand_FC1_1="../assets/tab3/NIRS_hbo_righthand_FC1_1.png"
hbo_righthand_FC1_2="../assets/tab3/NIRS_hbo_righthand_FC1_2.png"
hbo_righthand_FC1_3="../assets/tab3/NIRS_hbo_righthand_FC1_3.png"
hbr_righthand_FC1_1="../assets/tab3/NIRS_hbr_righthand_FC1_1.png"
hbr_righthand_FC1_2="../assets/tab3/NIRS_hbr_righthand_FC1_2.png"
hbr_righthand_FC1_3="../assets/tab3/NIRS_hbr_righthand_FC1_3.png"


def run():

    st.title(title)
    st.write(text)

    st.header(header_filtres)
    st.subheader(subheader_filtres)
    col1, col2 = st.columns(2)
    with col1:
        st.write(txt_filtres)
    with col2:
        st.image(img_filtres)
    st.write(text_filtreseeg)
    st.subheader(subheader_butterworth)    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.image(img_butterworth)
    with col2:
        st.write(text_butterworth)
    st.subheader("Exemple sur données EEG")
    #st.write(st.session_state["filter_slider"])
    col1, col2 = st.columns([4, 1])
    with col1:
        filtre=st.slider("Filtre fréquence (Hz)",min,max,value=(ph,pb),step=step,key="filter_slider",on_change=display_fig)
    with col2:
        st.button("Defaut : 0,01 à 24,49", on_click=_update_slider, kwargs={"value": (ph,pb)})
        st.checkbox("Butterworth Ordre 4", on_change=display_fig, key="check_butter")
    st.selectbox("Choix du canal :", options=("C1","C2","C3","C4","FC1", "FC2","FC5","FC6","Fz"), index=0, on_change=display_fig, key="select_canal")
    st.pyplot(display_fig())

    st.header(header_ICA)
    st.write(text_ICA)
    col1, col2 = st.columns([1, 3])
    with col1:
        scenario = st.radio("Scenario:",("Pas de filtre et d'ICA","Avec filtre et ICA 4 composants principaux"),key="radio_ica",on_change=display_ica)
    with col2:
        st.image(display_ica())
    
    st.header(header_concentration)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(text_concentration)
    with col2:
        st.image(img_absorption)
    st.write("1) Signaux originaux **sans transformation** pour les longueurs d’ondes 760 et 850 nm")
    col1, col2 = st.columns(2)
    with col1:
        st.image(hbo_righthand_FC1_1)
    with col2:
        st.image(hbr_righthand_FC1_1)
    st.write("""2) Signaux **après transformation en concentration HbO et HbR**.
    Les coefficients d'absorptivité molaire (correspondant à la mesure de la force avec laquelle une espèce chimique absorbe, et donc atténue, la lumière à une longueur d'onde donnée) utilisés pour appliquer la loi de Beer-Lambert pour nos longueurs d’onde sont les suivants : 
    760 :  3.56 pour HbR et 1,34 pour HbO
    850 :  1,59 pour HbR et 2,44 pour HbO
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.image(hbo_righthand_FC1_2)
    with col2:
        st.image(hbr_righthand_FC1_2)
    st.write("3) Signaux après utilisation d’un **filtre passe-bande Butterworth de 4ème ordre**, entre 0.01 et 0.2 Hz pour éliminer les artefacts.")
    col1, col2 = st.columns(2)
    with col1:
        st.image(hbo_righthand_FC1_3)
    with col2:
        st.image(hbr_righthand_FC1_3)
