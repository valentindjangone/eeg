from collections import OrderedDict

import streamlit as st
import os

current_path = os.path.dirname(os.path.abspath(__file__))

# TODO : 
import config

# TODO : 
from tabs import home, intro, second_tab, third_tab, fourth_tab, fifth_tab


st.set_page_config(
    page_title=config.TITLE,
    page_icon="🧠",
)

with open(os.path.join(current_path,"style.css"), "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


# TODO: add new and/or renamed tab in this ordered dict by
# passing the name in the sidebar as key and the imported tab
# as value as follow :

TABS = OrderedDict([
        ("🏠 " + home.sidebar_name, home),
        ("📖 " + intro.sidebar_name, intro),
        ("🔍 " + second_tab.sidebar_name, second_tab),
        ("🔧 " +third_tab.sidebar_name, third_tab),
        ("⚙️ " + fourth_tab.sidebar_name, fourth_tab),
        ("📊 " + fifth_tab.sidebar_name, fifth_tab)
    ]
)



def run():
    st.sidebar.image(
        "https://dst-studio-template.s3.eu-west-3.amazonaws.com/logo-datascientest.png",
        width=200,
    )
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {config.PROMOTION}")

    st.sidebar.markdown("### Team members:")
    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    tab.run()


if __name__ == "__main__":
    run()
