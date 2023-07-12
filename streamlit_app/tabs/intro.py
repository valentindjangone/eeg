import streamlit as st


title = 'Our Journey With EEG : Decoding Motor Execution Signals'

sidebar_name = "Introduction"


def run():

    # TODO: choose between one of these GIFs
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")
    _left, mid, _right = st.columns(3)
    with mid:
      st.image("https://i.gifer.com/74ny.gif", use_column_width=5)
    
    st.title(title)

    st.markdown("---------")

    st.subheader('Introduction')


    st.write("""
    Welcome to this project at the intersection of neurosciences, machine learning, and data visualization. 

   
Every time we reach, grasp or wave, there's an intricate dance of electrical activity taking place within our brains. These seemingly simple actions trigger a cascade of signals, with each neuron playing a part in the grand performance. This cerebral ballet is captured and visualized using EEG (Electroencephalogram) data.

The challenge we've embraced is to find the specific patterns within the EEG data that represent the command to move our hands and arms. It's like discerning a single melody within an orchestra's symphony - not an easy feat, but an intriguing one!

We put state of the art machine learning techniques to use, aiming to classify these hand and arm movement commands within the EEG data. Join us as we visualize and interpret this data.

""")
