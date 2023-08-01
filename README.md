# Projet EEG


## Introduction

Ce repository a pour objectif de présenter le projet initié dans le cadre de notre formation de[Data Scientist](https://datascientest.com/en/data-scientist-course) à [DataScientest](https://datascientest.com/)

Notre projet vise à **classifier** les ondes cérébrales associées à l'**exécution motrice**. L'objectif principal de cette classification est de créer une **Interface Homme - Machine (IHM)** permettant aux utilisateurs d'interagir avec des dispositifs ou des systèmes informatiques en utilisant leurs activités cérébrales en temps réel. En détectant et en interprétant les **intentions de mouvement** à partir des signaux électroencéphalographiques **(EEG)** et Functional Near Infrared Spectroscopy **(FNIRS)**, nous souhaitons contribuer au développement d'une interface intuitive et efficace pour faciliter la communication et le contrôle avec les machines, ouvrant ainsi la voie à de nouvelles perspectives dans la technologie et l' **accessibilité**.

## Défis

Une telle classification présente deux difficultés principales :

**Variabilité inter-sujets :** Les signaux EEG peuvent varier considérablement d'un sujet à l'autre en raison des différences anatomiques, physiologiques et cognitives. Cette variabilité inter-sujets peut rendre difficile la généralisation du modèle de classification à l'ensemble de la population.

**Recouvrement Spatial :** Les mouvements que l'on souhaite détecter (bras droit, main droite, bras gauche, main gauche) sont spatialement proches dans le cerveau. Cela signifie que les signaux EEG correspondants peuvent se chevaucher, rendant difficile leur distinction précise.



## Résumé

Nous avons classifié **1500** évènements issus de données électro encéphalographiques et spéctroscopiques fonctionnelles dans le proche infra rouge **(EEG & fNIRS)** issues de **15 sujets**.

Les données sont issues d'**exécutions motrices** : bras droit, bras gauche, main droite, main gauche.

Nous traitons le signal avec la librairie spécialisée **MNE**, en extrayons les caractéristiques avec l'algorithme de génération aléatoire de caractéristiques **ROCKET** et classifions les évènements selon les 4 classes ci-dessus avec un **classifieur linéaire**.




## Équipe

Le projet a été développé par l'équipe suivante :

- Julien Brachet ([GitHub](https://github.com/brachetj) / [LinkedIn](https://www.linkedin.com/in/julien-brachet-76b37325/)
- François Crouchet [GitHub](https://github.com/fcrouchet) /[Linkedin](https://www.linkedin.com/in/fcrouchet/)
- Valentin Djangoné [GitHub](https://github.com/valentindjangone) / [LinkedIn](https://www.linkedin.com/in/valentin-djangoné/))
- Nicolas Mavromatis [GitHub](https://github.com/9Nicox) / [LinkedIn](https://www.linkedin.com/in/nicolas-mavromatis/)


## Pour lancer l'application Streamlit ...

Pour lancer app :

```shell
cd streamlit_app
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run app.py
```

The app should then be available at [localhost:8501](http://localhost:8501).
