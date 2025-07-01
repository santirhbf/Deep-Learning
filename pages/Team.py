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
        st.image(image_path, width=150)  # Display the team member's image

    with col2:
        st.markdown(f"### {name}")
        st.markdown(f"**{role}**")
        st.write(bio)
        st.markdown(f"💡 *{fun_fact}*")

col1,col2,col3=st.columns(3)
with col2:
    st.image("data/logo.png", width=200)
st.markdown(f'<p style="font-size:40px; text-align:center; font-weight:bold; ">Meet Our Team</p>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)

st.markdown("Our team brings together expertise in deep learning, team leadership, , and web development.")

team_members = [
    ("Guillermo Medina", "🚀 Lead Business Strategist", 
        "🇪🇸 Guillermo is from Valencia and brings **years of consulting and business strategy insights** to the project. 📊 His expertise in **decision-making & market analysis** helped shape the <b>vision</b> of our trading system.",
        "👨‍🍳 He is a Michelin Star chef at **Yo me lo guiso, yo me lo como**! :avocado:", "data/Guille.jpg"),

    ("Lucía Sarobe", ":eye: Ophthalmologist", 
        "🇪🇸 Lucía is from Pamplona/Iruña and is **the best Ophtalmologist in Euskal Erria**, she makes sure that everyone can <b>see</b> the world in full HD.",
        "📰 She has been on the **front page of Diario de Navarra**! 🌟", "data/Lucia.png"),

    ("Santiago Ruiz Hernández", "📌 Project Point Lead", 
        "🇪🇸 Santiago is from Valencia, Spain, and worked on **various aspects of the project**, acting as a key **point lead** to keep everything running smoothly. 🔄 His contributions touched on multiple areas of **EDA, strategy, and technical implementation**.",
        ":softball: He is a **professional padel player** and is a **natural redhead**! 🔥", "data/santi.jpg")
]

for member in team_members:
    display_team_member(*member)
