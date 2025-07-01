import streamlit as st
import numpy as np
import pickle
from PIL import Image
import transformers
import os
import matplotlib.pyplot as plt
import requests as req

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
    "ChromeID": None,
    "Team": "pages/Team.py"
}

for page_name, file_path in PAGES.items():
    if file_path:
        st.sidebar.page_link(file_path, label=page_name)
    else:
        st.sidebar.write(f"### {page_name}")

st.title("Welcome to ChromeID!")


st.image("data/mascota.png", width=200)
st.markdown(
    "<p class='dog-text'>:eye: Hi, I am <b>ChromeID</b>, and I am here to help you identify any color you want!"
    " How <b>ChromeID</b> works is, you upload an image with something you would like to identify the color of, and our "
    "<b>ChromID</b> will do the rest! Sit tight, and it will make you see the world with new eyes!",
    "You will never have to worry of mising anything! You are safe with ChromeID!</p>",
    unsafe_allow_html=True
)

st.title("Please upload the image you want ChromeID to see for you!")

# File uploader for images
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Display the image if uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


model_processor = transformers.ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
classes_names = sorted(os.listdir("data/cleaned_color_dataset"))


def predict_image_color_vit(file, model, processor, class_names):
    # Load and preprocess image
    img = file
    inputs = processor(images=file, return_tensors="tf")

    # Predict
    preds = model.predict(inputs["pixel_values"])
    pred_class = np.argmax(preds.logits, axis=1)[0]
    pred_label = class_names[pred_class]

    # Display result
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Predicted Color: {pred_label}")
    plt.show()

    return pred_label


def download_file_from_google_drive(id_file, destination_name):
    URL = "https://docs.google.com/uc?export=download"

    session = req.Session()

    # Initial request
    response = session.get(URL, params={'id': id_file}, stream=True)
    token = get_confirm_token(response)

    if token:
        # Re-request with confirmation
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination_name)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination_name):
    CHUNK_SIZE = 32768  # 32 KB

    with open(destination_name, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)


# File ID from your Google Drive link
file_id = "121D_p6XdPPLj8dKM09z4zg1jwfEELE3I"
destination = "color_pred_model.pkl"

# Download the file
download_file_from_google_drive(file_id, destination)

# Load the pickle model
with open(destination, "rb") as f:
    loaded_model = pickle.load(f)

prediction = predict_image_color_vit(uploaded_file, loaded_model, model_processor, classes_names)


class_folders = ['Black', 'Blue', 'Brown', 'Green', 'red', 'White']


col1,col2,col3=st.columns(3)
with col2:
    if st.button("LET ME SEE!"):
        if prediction in class_folders:
            st.markdown(f'<p style="font-size:20px; text-align:left; ">The color of the image you uploaded is: <b>{prediction}</b></p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="font-size:20px; text-align:left; ">The color of the image you uploaded does not seem to be clear enough, please try again.</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size:15px; text-align:left; ">(It might help zooming in more, or taking the picture closer to the object you want to identify).</p>', unsafe_allow_html=True)