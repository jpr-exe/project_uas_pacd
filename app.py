import streamlit as st
import cv2
import numpy as np
import joblib
from skimage.feature import hog
from PIL import Image

st.set_page_config(page_title="Deteksi Makanan", page_icon="🍔")
st.title("Aplikasi Klasifikasi Citra Makanan")
st.write("Sistem ini menggunakan metode HOG dan Logistic Regression untuk mengenali gambar **Pizza**, **Steak**, atau **Sushi**.")

@st.cache_resource
def load_model():
    return joblib.load('model_logreg.pkl')

model = load_model()
kelas_makanan = ["pizza", "steak", "sushi"]

uploaded_file = st.file_uploader("Unggah file gambar (JPG, JPEG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. Load the original image
    image = Image.open(uploaded_file)
    image_array = np.array(image.convert('RGB'))
    
    # 2. Extract HOG features and predict
    image_gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    image_resized = cv2.resize(image_gray, (64, 64))

    fitur_hog = hog(image_resized, 
                    orientations=9, 
                    pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2), 
                    block_norm='L2-Hys', 
                    visualize=False)

    fitur_final = fitur_hog.reshape(1, -1)
    hasil_prediksi = model.predict(fitur_final)
    label_kelas = kelas_makanan[hasil_prediksi[0]].upper()

    image_after = image_array.copy()
    h, w, c = image_after.shape
    
    x1, y1 = int(w * 0.25), int(h * 0.25)
    x2, y2 = int(w * 0.75), int(h * 0.75)
    
    thickness = max(2, int(min(w, h) * 0.008))
    font_scale = max(0.5, min(w, h) * 0.002)
    font_thickness = max(1, int(thickness * 0.6))
    
    cv2.rectangle(image_after, (x1, y1), (x2, y2), (0, 255, 0), thickness)
    
    text_y = y1 - 10 if y1 - 10 > 15 else y1 + 25
    cv2.putText(image_after, label_kelas, (x1, text_y), 
                cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 
                font_thickness, cv2.LINE_AA)

    st.success(f"Hasil Deteksi: {label_kelas}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center; color: #4A90E2;'>Before (Citra Input)</h4>", unsafe_allow_html=True)
        st.image(image, use_container_width=True)
    with col2:
        st.markdown("<h4 style='text-align: center; color: #2ECC71;'>After (Hasil Deteksi)</h4>", unsafe_allow_html=True)
        st.image(image_after, use_container_width=True)