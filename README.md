## Introduction

This repository aims to present the project initiated as part of our Data Scientist training at DataScientest. Our project aims to classify brain waves associated with motor execution. The primary goal of this classification is to create a Human-Machine Interface (HMI) allowing users to interact with devices or computer systems using their real-time brain activities. By detecting and interpreting movement intentions from Electroencephalographic (EEG) and Functional Near-Infrared Spectroscopy (FNIRS) signals, we aim to contribute to the development of an intuitive and effective interface for facilitating communication and control with machines, thus opening new perspectives in technology and accessibility.

## Challenges

Such a classification presents two main difficulties:

**Inter-subject Variability:** EEG signals can vary significantly from one subject to another due to anatomical, physiological, and cognitive differences. *This inter-subject variability can make it difficult to generalize the classification model to the entire population.

**Spatial Overlap:** The movements we want to detect (right arm, right hand, left arm, left hand) are spatially close in the brain. This means that the corresponding EEG signals can overlap, making it difficult to distinguish them accurately.

## Summary

We have classified 1500 events from electroencephalographic and functional near-infrared spectroscopy data (EEG & fNIRS) from 15 subjects.

The data comes from motor executions: right arm, left arm, right hand, left hand.

We process the signal with the specialized library MNE, extract features with the ROCKET random feature generation algorithm, and classify the events according to the 4 above classes with a linear classifier.

## Team 

The project was developed by the following team:


- Julien Brachet [GitHub](https://github.com/brachetj) / [LinkedIn](https://www.linkedin.com/in/julien-brachet-76b37325/)
- François Crouchet [GitHub](https://github.com/fcrouchet) /[Linkedin](https://www.linkedin.com/in/fcrouchet/)
- Valentin Djangoné [GitHub](https://github.com/valentindjangone) / [LinkedIn](https://www.linkedin.com/in/valentin-djangoné/)
- Nicolas Mavromatis [GitHub](https://github.com/9Nicox) / [LinkedIn](https://www.linkedin.com/in/nicolas-mavromatis/)
## To Launch the Streamlit Application...

To launch the app, simply click on the following link: https://eegproject.streamlit.app
