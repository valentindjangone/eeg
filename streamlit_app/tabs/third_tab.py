import streamlit as st
import mne
import matplotlib.pyplot as plt

sidebar_name = "Preprocessing"

title = "Méthodes de Preprocessing utilisées"
text = """Le pretraitemement des données, ou preprocessing, est
indispensable à l'analyse des signaux EEG et NIRS. Il permet notament
de s'étalonner par rapport aux électrodes de référence, de réduire les
bruits parasites, de supprimer les mauvais canaux, ou encore d'éliminer les
artéfacts de mouvement.
Les méthodes de preprocessing utilisées durant ce projet sont basées sur
celles proposées par les auteurs du dataset, ainsi que sur celles trouvées
dans d’autres articles scientifiques traitant de problématiques similaires.
"""

header1 = "Filtres numériques"
subheader11 = "Filtre passe-bande (passe-bas + passe-haut)"
text11= """Pour les données EEG, un filtre passe-haut de 0.01 HZ et un filtre
passe-bas de 24.49 Hz ont été appliqués. Ce sont des filtres utilisés de
manière conventionnelle dans l’analyse de signal EEG et qui permettent de
conserver les signaux physiologiques tout en retirant des bruits parasites
comme le 60Hz (courant du casque) par exemple."""

rawo = mne.io.read_raw_fif("../data/S1_eeg.fif",preload=True)
rawo10 = rawo.copy()
rawo10.crop(tmax=10).load_data()
rawo50 = rawo.copy()
rawo50.crop(tmax=50).load_data()

def _update_slider(value):
    st.session_state["filter_slider"] = value
    display_fig()
if "filter_slider" not in st.session_state:
    st.session_state["filter_slider"] = 0
ph, pb =0.01, 24.49
min, max = 0.0, 100.0
step = 0.01

def display_fig():
    pht,pbt=st.session_state["filter_slider"]
    raw=rawo10.copy()
    if st.session_state["check_butter"]:
        raw.filter(pht,pbt,method='iir', iir_params = None)
    else:
        raw.filter(pht,pbt)
    fig, ax = plt.subplots(figsize=(24, 12))
    ax.plot(raw.times, raw.get_data(picks='FC1').squeeze())
    return fig

def display_ica():
    rawica=rawo.copy()
    if st.session_state["radio_ica"] == "Pas de filtre et d'ICA":
        img_ica="../images/EEGAvantFiltrage.png"
    else:
        img_ica="../images/EEGApresFiltrage.png"
    return img_ica

subheader12 = "Filtre Butterworth"
text12= """Pour les données fNIRS, nous avons utilisé un filtre passe-bande
particulier, un filtre Butterworth d'ordre 4. Le gain de ce filtre est le
plus constant possible dans la bande passante et tend vers 0 dB dans la bande
de coupure.
"""

header2 = "Independant Components Analysis sur signal EEG"
text2 = """L'analyse en composantes indépendantes ou ICA permet d’identifier
et supprimer les artefacts pouvant provenir de diverses sources, telles
que les mouvements oculaires, les battements du coeur, les bruits électriques,
etc... L'ICA permet de séparer ces sources artefactuelles des signaux
cérébraux d'intérêt, facilitant ainsi une meilleure interprétation et
analyse des données.
"""

header3 = "Concentration en HbO et HbR sur signaux fNIRS"
text3 = """Les deux signaux utilisés en fNIRS correspondant à deux longueurs
d’onde (760 nm et 850 nm) ont également subi une transformation mathématique
pour les transformer en signaux de concentration d’hémoglobine oxygénée (HbO)
et d’hémoglobine désoxygénée (HbR). Cette transformation a été réalisée
en appliquant la loi de Beer-Lambert.
"""
hbo_righthand_FC1_1="../images/NIRS_hbo_righthand_FC1_1.png"
hbo_righthand_FC1_2="../images/NIRS_hbo_righthand_FC1_2.png"
hbo_righthand_FC1_3="../images/NIRS_hbo_righthand_FC1_3.png"
hbr_righthand_FC1_1="../images/NIRS_hbr_righthand_FC1_1.png"
hbr_righthand_FC1_2="../images/NIRS_hbr_righthand_FC1_2.png"
hbr_righthand_FC1_3="../images/NIRS_hbr_righthand_FC1_3.png"

def run():

    st.write(" ")
    st.write(" ")
    st.write(" ")

    st.title(title)
    st.write(text)

    st.header(header1)
    st.subheader(subheader11)
    st.write(text11)
    col1, col2 = st.columns([4, 1])
    with col1:
        filtre=st.slider("Filtre",min,max,value=(ph,pb),step=step,key="filter_slider",on_change=display_fig)
    with col2:
        st.button("Defaut : 0,01 à 24,49", on_click=_update_slider, kwargs={"value": (ph,pb)})
        st.checkbox("Butterworth Ordre 4", on_change=display_fig, key="check_butter")
    st.pyplot(display_fig())

    st.subheader(subheader12)
    st.write(text12)
    
    st.header(header2)
    st.write(text2)
    col1, col2 = st.columns([1, 3])
    with col1:
        scenario = st.radio("Scenario:",("Pas de filtre et d'ICA","Avec filtre et ICA 4 composants principaux"),key="radio_ica",on_change=display_ica)
    with col2:
        st.image(display_ica())
    
    st.header(header3)
    st.write(text3)
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
