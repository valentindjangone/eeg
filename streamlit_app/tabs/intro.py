import streamlit as st
from PIL import Image

# Ouvrir l'image PNG
image = Image.open("C:\\Users\\brach\\Documents\\datascientest\\Projet EEG\\eeg-main\\eeg-main\\images\\ImageEEG.png")

# Définir la nouvelle largeur souhaitée
new_width = 700

# Calculer la nouvelle hauteur proportionnelle en conservant les proportions originales
width, height = image.size
new_height = int((height / width) * new_width)

# Redimensionner l'image
resized_image = image.resize((new_width, new_height))

# Enregistrer l'image redimensionnée
resized_image.save("C:\\Users\\brach\\Documents\\datascientest\\Projet EEG\\eeg-main\\eeg-main\\images\\image_resized.png")

def balises_html(texte):
    texte_formate = f"<ul>{texte}</ul>"
    st.markdown(texte_formate, unsafe_allow_html=True)

# Utilisation de la fonction balises_html pour créer une liste à puces
liste = """
<li>Visualisation des données.</li>
<li>Preprocessing des données : pour élimiminer ou réduire les artefacts notamment les artfects de mouvements. </li>
<li>Feature Engineering pour extraire des caractétristiques notamment temporelles, fréquentielles ou dans le domaine temps/fréquence.</li>
<li>Elaboration des modèles de machine et de deep learning pour établir les prédictions.</li>
"""


sidebar_name = "Introduction"


def run():

    # TODO: choose between one of these GIFs
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")
    _left, mid, _right = st.columns(3)
  
    st.header("Interface Cerveau Machine / Intelligence  Artificielle : la combinaison gagnante")
    img = Image.open("C:\\Users\\brach\\Documents\\datascientest\\Projet EEG\\eeg-main\\eeg-main\\images\\image_resized.png")
    st.image(img, width = 400, caption = "")
    tab1, tab2 = st.tabs(["Introduction", "Objectifs"])

    with tab1:
      st.header ("Introduction")
      st.write(""" Bienvenue sur la page de notre projet qui est à l'intersection de la neuroscience, de l'intelligence artificielle et de 
                  l'électronique.""")
                  
      st.write("""Depuis les années 50, les techniques  d'Electroencéphalographiques (EEG) sont utilisées pour mesurer l'activité cérébrale.""")
                  
      st. write("""Elles ont été complétées par d'autres techniques d'imagerie comme la Spectroscopie proche infra-rouge fonctionnelle (FNIRS), la magnétoencéphalographie (MEG) et l'imagerie pa résonnance magnétique.""")
                   
      st.write("""En mesurant cette activité, il est devenu possible de traduire  signaux électroniques ou neurologiques produits par le cerveau  en commandes compréhensibles par une machine.""")
                  
      st.write("""Et ainsi de construire de nouvelles IHM : les Brain Computer Interfaces (BCI).""")

      
      
    with tab2:
      st.header("Description du projet")
      
      st.write(""" L'objectif de notre projet est de réaliser un modèle de classification permettant de prédire les mouvements réalisés par un utilisateur.""")
                  
      st.write("""Pour cela nous avons utilisé des jeux de données opensource où ont été mesurées les données EEG de 15 individus réalisant 4 mouvements différents ((Levage bras droit, levage bras gauche, préhension main droite, préhension main gauche).""")
      
      st.write(""" Dans le cadre de ce projet la méthodologie suivante : """)
      balises_html(liste)
      

 
      


    
