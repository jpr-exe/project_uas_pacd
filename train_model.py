import os
import cv2
import numpy as np
import joblib
from skimage.feature import hog
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Fungsi untuk memuat data dan mengekstraksi fitur HOG
def proses_ekstraksi_data(base_dir, kelas_makanan):
    fitur_list = []
    label_list = []
    
    for label_idx, nama_kelas in enumerate(kelas_makanan):
        folder_path = os.path.join(base_dir, nama_kelas)
        
        # Lewati jika folder tidak ada
        if not os.path.exists(folder_path):
            continue
            
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            citra = cv2.imread(file_path)
            
            if citra is not None:
                # Ubah ukuran dan warna
                citra_resized = cv2.resize(citra, (64, 64))
                citra_gray = cv2.cvtColor(citra_resized, cv2.COLOR_BGR2GRAY)
                
                # Hitung vektor HOG
                fitur_hog = hog(citra_gray, 
                                orientations=9, 
                                pixels_per_cell=(8, 8),
                                cells_per_block=(2, 2), 
                                block_norm='L2-Hys', 
                                visualize=False)
                
                fitur_list.append(fitur_hog)
                label_list.append(label_idx)
                
    return np.array(fitur_list), np.array(label_list)

# 2. Definisi jalur direktori dan kategori
train_dir = "daftar_makanan/train"
test_dir = "daftar_makanan/test"
kelas_makanan = ["pizza", "steak", "sushi"]

# 3. Proses Data Latih (Training)
print("Memulai ekstraksi fitur data latih...")
X_train, y_train = proses_ekstraksi_data(train_dir, kelas_makanan)

# 4. Proses Data Uji (Testing)
print("Memulai ekstraksi fitur data uji...")
X_test, y_test = proses_ekstraksi_data(test_dir, kelas_makanan)

# 5. Pelatihan Model Logistic Regression
print("Melatih model Logistic Regression...")
# Parameter max_iter diatur ke 1000 untuk memastikan algoritma mencapai konvergensi matematis
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Evaluasi Kinerja Model
print("Mengevaluasi akurasi model...")
y_pred = model.predict(X_test)
akurasi = accuracy_score(y_test, y_pred)

print(f"\nAkurasi Model: {akurasi * 100:.2f}%")
print("Laporan Klasifikasi Lengkap:")
print(classification_report(y_test, y_pred, target_names=kelas_makanan))

# 7. Penyimpanan Model Terlatih
print("\nMenyimpan parameter model ke file model_logreg.pkl...")
joblib.dump(model, "model_logreg.pkl")
print("Proses komputasi selesai.")