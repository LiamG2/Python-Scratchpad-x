import streamlit as st
# noinspection PyUnresolvedReferences
from streamlit_lottie import st_lottie

lottie_polyfox_1 = ('https://raw.githubusercontent.com/LiamG2/Python'
                    '-Scratchpad/main/kzrdAgrilI.json')

st.sidebar.title('Sidebar Title')
st.sidebar.header('Sidebar Header')

# method for adding widgets/lotties to sidebar
with st.sidebar:  
    st_lottie(lottie_polyfox_1, height=100, key='polyfox_1')
    # note different 'key' name above, needed when using same animation
    # \multiple times


st.title('🎈 Much longer title of My new app')

st.write(
    '.............................................................'
    '................... testing 2 column layoutt')

# set up [any-num] column layout in streamlit
col1, col2 = st.columns(2, gap="large")

# initiate 1st column
with col1:
    # add here everything that needs to be in Column 1
    st.write(
        'Let\'s start building!!! For help and inspiration, head \
        over to ['
        'docs.streamlit.io](https://docs.streamlit.io/).')
    st_lottie(lottie_polyfox_1, height=100, key="polyfox_2")
    # note different 'key' name above, needed when using same animation
    # \multiple times

# initiate 2nd column
with col2:
    # add here everything that needs to be in Column 2
    st.write(
        'Let\'s start building!!! For help and inspiration, head \
        over to ['
        'docs.streamlit.io](https://docs.streamlit.io/).')
    st_lottie(lottie_polyfox_1, height=100, key='polyfox_3')
    # note different 'key' name above, needed when using same animation
    # \multiple times
