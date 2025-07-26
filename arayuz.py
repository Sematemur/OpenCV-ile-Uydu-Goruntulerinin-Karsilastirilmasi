import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

st.title("Görüntü Farkı Analizi")

pre_image = st.file_uploader("Öncesi Fotoğraf", type=["png", "jpg", "jpeg"])
post_image = st.file_uploader("Sonraki Fotoğraf", type=["png", "jpg", "jpeg"])

if st.button("Tespit Et") and pre_image and post_image:
    files = {
        "pre": pre_image,
        "post": post_image
    }

    response = requests.post("http://localhost:8000/detect", files=files)

    if response.status_code == 200:
        result = response.json()

        heatmap = Image.open(BytesIO(base64.b64decode(result["heatmap"])))
        graymap = Image.open(BytesIO(base64.b64decode(result["graymap"])))

        st.image(heatmap, caption="ISIL HARİTA")
        st.image(graymap, caption="GRİ GÖRÜNTÜ")
    else:
        st.error("API hatası: " + str(response.status_code))
