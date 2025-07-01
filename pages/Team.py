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
    "Home": "Home.py",
    "ChromeID": "pages/ChromeID.py",
    "Team": None
}

for page_name, file_path in PAGES.items():
    if file_path:
        st.sidebar.page_link(file_path, label=page_name)
    else:
        st.sidebar.write(f"### {page_name}")

def display_team_member(name, role, bio, fun_fact, image_path):
    col1, col2 = st.columns([1, 3])  # Create two columns for layout

    with col1:
        st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)
        st.image(image_path, width=150)  # Display the team member's image

    with col2:
        st.markdown(f"### {name}")
        st.markdown(f"**{role}**")
        st.write(bio)
        st.markdown(f"💡 *{fun_fact}*")
        st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)

col1,col2,col3=st.columns(3)
with col2:
    st.image("data/logo.png", width=200)
st.markdown(f'<p style="font-size:40px; text-align:center; font-weight:bold; ">Meet Our Team</p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)

st.markdown("Our team brings together expertise in deep learning, team leadership, and web development.")

team_members = [
    ("Guillermo Medina", "🚀 Lead Business Strategist", 
        "Guillermo is from Valencia, and he made sure ChromeID was perfectly trained to have the most accurate results in the market.",
        "👨‍🍳 He is a Michelin Star chef at **Yo me lo guiso, yo me lo como**! :avocado:", "data/Guille.jpg"),

    ("Lucía Sarobe", "👁️ Visualization Professional", 
        "Lucía is from Pamplona/Iruña, and took care of making sure everything ran smoothly and made sure to bring our solution to everyone.",
        "📰 She has been on the **front page of Diario de Navarra**! 🌟", "data/Lucia.png"),

    ("Santiago Ruiz Hernández", "🧑‍💻 Front-End Developer", 
        "Santiago is also from Valencia, and worked on **The App**, making sure ChromeID would be available for everyone to **see**.",
        ":softball: He is a **professional padel player**, and is a **natural redhead**! 🔥", "data/santi.jpg")
]

for member in team_members:
    display_team_member(*member)
