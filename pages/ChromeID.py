import streamlit as st
import numpy as np
import pickle
from PIL import Image
import transformers
import os
import matplotlib.pyplot as plt
import gdown


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

col1,col2,col3=st.columns(3)
with col2:
    st.image("data/mascota.png", width=200)

st.markdown(f'<p style="font-size:25px; text-align:left; "><br></p>', unsafe_allow_html=True)


st.markdown("""👁️ Hi, I am **ChromeID**, and I am here to help you identify any color you want!
    How **ChromeID** works is, you upload an image with something you would like to identify the color of, and
    **ChromeID** will do the rest! Sit tight, and it will make you see the world with new eyes!
    You will never have to worry of mising anything! You are safe with ChromeID!""")

st.markdown(f'<p style="font-size:25px; text-align:left; ">Upload the image you want <b>ChromeID</b> to see for you!</p>', unsafe_allow_html=True)

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


# Download the model if it doesn't already exist
MODEL_URL = "https://drive.google.com/uc?id=121D_p6XdPPLj8dKM09z4zg1jwfEELE3I"
MODEL_FILE = "color_pred_color.pkl"

if not os.path.exists(MODEL_FILE):
    gdown.download(MODEL_URL, MODEL_FILE, quiet=False)

# Load the model
with open(MODEL_FILE, "rb") as f:
    loaded_model = pickle.load(f)


prediction = predict_image_color_vit(uploaded_file, loaded_model, model_processor, classes_names)


class_folders = ['Black', 'Blue', 'Brown', 'Green', 'red', 'White']


with col2:
    if st.button("LET ME SEE!"):
        if prediction in class_folders:
            st.markdown(f'<p style="font-size:20px; text-align:left; ">The color of the image you uploaded is: <b>{prediction}</b></p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="font-size:20px; text-align:left; ">The color of the image you uploaded does not seem to be clear enough, please try again.</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size:15px; text-align:left; ">(It might help zooming in more, or taking the picture closer to the object you want to identify).</p>', unsafe_allow_html=True)