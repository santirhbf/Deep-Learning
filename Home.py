import streamlit as st

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] ul {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

PAGES = {
    "Home": None,
    "ChromeID": "pages/ChromeID.py",
    "Team": "pages/Team.py"
}

for page_name, file_path in PAGES.items():
    if file_path:
        st.sidebar.page_link(file_path, label=page_name)
    else:
        st.sidebar.write(f"### {page_name}")
col1,col2,col3=st.columns(3)
with col2:
    st.image("data/logo.png", width=200)

st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:35px; text-align:left; ">Welcome to <b>ChromeID!</b> -- Your Intelligent Online Color Detector</p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:15px; text-align:left; ">Now, all the colors of the world, lie within your grasp!</p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:20px; text-align:left; "><b>ChromeID</b> is an innovative, AI-powered assistant designed to enhance the world of color for people with color vision deficiency. Whether you’re shopping, dressing, designing, or simply exploring your surroundings, ChromeID helps you identify and understand colors you might not easily perceive. Our intelligent system provides clear, accurate color names, contrasts, and suggestions—so you never miss out on the beauty and function of color again. ChromeID empowers you to navigate daily life with more confidence, independence, and creativity. You’re just one step away from seeing the world in a whole new way.</p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:25px; text-align:left;font-weight:bold;">What are you waiting for?</p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:25px; text-align:left; ">Start your experience here!</p>', unsafe_allow_html=True)
website_url = "https://deep-learning-xyjfsdgreafpa5dj36ctzz.streamlit.app/ChromeID"
if st.button("LET'S GO!"):
    st.markdown(f'<meta http-equiv="refresh" content="0; URL={website_url}">', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)

cola,colb,colc=st.columns(3)
with cola:
    st.image("data/red_rose.jpeg", width=205)
    st.image("data/green_grass.jpeg", width=205)
with colb:
    st.image("data/pink_donut.jpeg", width=205)
    st.image("data/orange_nature.jpeg", width=205)
with colc:
    st.image("data/blue_ocean.jpeg", width=205)
    st.image("data/yellow_sun.jpeg", width=205)