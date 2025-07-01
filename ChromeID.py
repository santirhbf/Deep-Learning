import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pickle
from PIL import Image
from transformers import ViTImageProcessor
import os
import matplotlib.pyplot as plt

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

st.sidebar.title("Welcome to ChromeID!")


st.sidebar.image("data/mascota.png", width=200)
st.sidebar.markdown(
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


model_processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")
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


loaded_model = pickle.load(open('picklemodel.pkl', 'rb'))
prediction = predict_image_color_vit(uploaded_file, loaded_model, model_processor, classes_names)


class_folders = ['Black', 'Blue', 'Brown', 'Green', 'red', 'White']
if prediction in class_folders:
    st.markdown(f'<p style="font-size:20px; text-align:left; ">The color of the image you uploaded is: <b>{prediction}</b></p>', unsafe_allow_html=True)
else:
    st.markdown(f'<p style="font-size:20px; text-align:left; ">The color of the image you uploaded does not seem to be clear enough, please try again.</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:15px; text-align:left; ">(It might help zooming in more, or taking the picture closer to the object you want to identify).</p>', unsafe_allow_html=True)


st.markdown(f'<p style="font-size:20px; font-weight:bold; text-align:left; ">Please insert your height in METERS:</p>', unsafe_allow_html=True)
heightmt=st.slider("",min_value=0.60,max_value=2.80,value=1.65,step=0.01)
heightft=heightmt*3.281
st.markdown(f'<p style="font-size:16px; color:grey;">(This is in feet would be: {heightft:.2f} feet)</p>', unsafe_allow_html=True)

BMI=weightkg/(heightmt**2)
st.markdown(f'<p style="font-size:20px; text-align:left; "><b>Your BMI ratio is --&rarr;</b> {BMI:.2f} KG/M<sup>2</sup></p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">Please insert the aproximate hours you sleep per night:</p>', unsafe_allow_html=True)
sleep=st.slider("",min_value=0.0,max_value=12.0,value=6.0,step=0.5)

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">Please insert your aproximate stress level:</p>', unsafe_allow_html=True)
stresslvl=st.slider("",min_value=1.0,max_value=10.0,value=5.0,step=0.5)

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">Please insert the number of pregnancies you have gone through:</p>', unsafe_allow_html=True)
pregnancies=st.slider("",min_value=0,max_value=20,value=6,step=1)

min_birth_date = datetime.date(1900, 1, 1)
max_birth_date = datetime.date.today()
st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">Please insert your date of birth:</p>', unsafe_allow_html=True)
birth=st.date_input('',min_value=min_birth_date,max_value=max_birth_date)
today = datetime.date.today()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
st.markdown(f'<p style="font-size:16px; color:grey;">(Meaning you are {age} years old)</p>', unsafe_allow_html=True)

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">Now please from the following boxes, check the ones which apply to you:</p>', unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
    history=st.checkbox("Family history of diabetes")
    hypertension=st.checkbox("Hypertension")
with col2:
    hyperlipidemia=st.checkbox("Hyperlipidemia")
    cardiovasc=st.checkbox("Cardiovascular disease")
with col3:
    polyov=st.checkbox("Polycystic Ovary Syndrome")

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; "><br>Please select your smoking status at the moment:</p>', unsafe_allow_html=True)
smoker=st.radio("",('Never','Former','Current'))
smokestat=0
if smoker=='Current':
    smokestat=2
elif smoker=='Former':
    smokestat=1
else:
    smokestat=0

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">Lastly, please select your ethnicity:</p>', unsafe_allow_html=True)
ethnicity=st.selectbox('',('African','Asian','Caucasian','Hispanic','Other'))
African=0
Asian=0
Caucasian=0
Hispanic=0
Other=0
if ethnicity=='African':
    African=1
    Asian=0
    Caucasian=0
    Hispanic=0
    Other=0
elif ethnicity=='Asian':
    African=0
    Asian=1
    Caucasian=0
    Hispanic=0
    Other=0
elif ethnicity=='Caucasian':
    African=0
    Asian=0
    Caucasian=1
    Hispanic=0
    Other=0
elif ethnicity=='Hispanic':
    African=0
    Asian=0
    Caucasian=0
    Hispanic=1
    Other=0
elif ethnicity=='Other':
    African=0
    Asian=0
    Caucasian=0
    Hispanic=0
    Other=1

st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; "><br></p>', unsafe_allow_html=True) #JUST A SPACE BETWEEN TEXT AND BUTTON

loaded_model = pickle.load(open('picklemodel.pkl','rb'))
scaler = pickle.load(open('scalermodel.pkl','rb'))

input_data1 = np.array([[age, pregnancies, smokestat, sleep, stresslvl, BMI]])
std_data = scaler.transform(input_data1)

input_data2 = np.array([[history, hypertension, hyperlipidemia, cardiovasc, polyov, African, Asian, Caucasian, Hispanic, Other]])

final_data = np.hstack((std_data, input_data2))
final_reshaped = final_data.reshape(1, -1)

prediction = loaded_model.predict_proba(final_reshaped)

button=st.button("GET TEST RESULTS")
if button==True:
    if prediction[0][1]>0.3:
        st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">There are considerably high odds of you having diabetes, but do not worry, it could be a false positive. You should consider taking more tests to be sure, better be safe than sorry</p>', unsafe_allow_html=True)
    else:
        st.balloons()
        st.markdown(f'<p style="font-size:20px; text-align:left; font-weight:bold; ">You are as healthy as an apple, good job, keep it up!</p>', unsafe_allow_html=True)
