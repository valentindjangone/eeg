import streamlit as st
import pandas as pd
import numpy as np


title = "Modélisation"
sidebar_name = "Modèlisation"

sub_header_1 = "Extraction de caractéristiques"
sub_header_2 = "Classification"
sub_header_3 = "Système de vote"
sub_header_4 = "Validation"

def run():

    st.title(title)
    st.subheader(sub_header_1)
    st.markdown(
        """
        Nous avons utilisé la version multivariée et simplifiée de l'algorithme RandOm Convolutional KErnel Transform (Mini ROCKET Multivariate) pour l'extraction de caractéristiques des enregistrements EEG et NIRS.
        
        \n\nUn ensemble de kernels est généré aléatoirement et est appliquée à un sous-ensemble aléatoire de 9 séries temporelles (ici 9 canaux), ce qui permet de capturer les interactions entre ces séries temporelles.
        \n\nC'est particulièrement utile pour nos données, où les interactions entre les signaux de différents électrodes peuvent être informatifs pour la classification des mouvements.

        """
    )

    st.subheader(sub_header_2)
    st.markdown(
        """
        La classification d'ondes cérébrales est sujette à des variations importantes selon la façon dont sont mélangées les données de test et d'entraînement. Un modèle performera toujours mieux sur des données propres à un seul individu qu'il ne le ferait sur une combinaison de données provenant de plusieurs individus.
        \nCette situation est due à la variabilité interindividuelle des signaux EEG, qui peut être influencée par de nombreux facteurs, comme l'âge, le sexe, l'état de santé, la fatigue, la forme du cerveau bien d'autres.
        \n\nL'utilisation de RidgeClassifierCV, avec son mécanisme de validation croisée, nous permet de trouver un modèle optimal qui peut généraliser à partir de ces variations. De plus, l'ajout de la régularisation Ridge aide à prévenir le surapprentissage, qui peut être un problème courant lors de l'entraînement de modèles sur des données hautement dimensionnelles,
        comme c'est le cas avec les caractéristiques extraites par Mini ROCKET.
        """
    )
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('../images/Cortex_sensorimoteur1.jpg')
    st.subheader(sub_header_3)
    st.markdown(
        """
        Notre système de vote tire avantageusement parti de nos données et de l'algorithme d'extraction de caractéristiques Mini ROCKET Multivariate.
        Il établit un lien entre les données EEG et FNIRS, et exploite la variance générée par la création aléatoire de kernels dans l'algorithme Mini ROCKET.
        \n\nEn effet, la génération de kernel étant faite de manière aléatoire, il peut y avoir une variance significative entre plusieurs itérations d'entraînements puisque ce ne sont jamais les mêmes features qui sont classées.

        \n\nConcrètement, ce système fonctionne en commençant avec les prédictions de trois modèles initiaux, chacun classant un type de données différent: EEG, HbR (hémoglobine réduite), et HbO (oxyhémoglobine).

        \nPar la suite, nous effectuons de nombreux cycles d'entraînement (500 fois pour chaque type de données), pendant lesquels de nouveaux modèles sont formés et leurs prédictions sont comparées aux modèles initiaux.
        À chaque cycle, si l'ajout des prédictions du nouveau modèle améliore le score total par rapport aux modèles initiaux, alors ce nouveau modèle est conservé. Sinon, il est rejeté.
        \nSi le vote sur les prédictions des modèles initiaux auquel on ajoute le modèle nouvellement entraîné est supérieur au vote sur les modèles initiaux, alors le modèle est conservé. Si le score est inférieur, le modèle est rejeté. 
        """
    )

    st.video("VotingClassifierAnimation.mp4")
    st.markdown("_Vidéo : Animation du système de classification de vote_") 

    st.subheader(sub_header_4)
    st.markdown(
        """
        \n\nEnfin, puisque nous ne conservons que les modèles ayant contribué à l'amélioration du score sur les données de test, nous introduisons un biais de sélection favorable propre à ces données. Autrement dit, malgré la validation croisée,
        comme nous ajustons nos modèles uniquement sur la base des scores obtenus sur les données de test, nous risquons d'optimiser le modèle pour ces données spécifiques, ce qui pourrait conduire à un surapprentissage.
        Pour vérifier que le modèle généralise effectivement sur toutes les données, nous vérifions les scores sur un jeu de validation.

        """
    )
