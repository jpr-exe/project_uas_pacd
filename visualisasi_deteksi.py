import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# =====================================================================
# VARIABEL PATH GAMBAR (Silakan ganti dengan file gambar Anda)
# =====================================================================
IMAGE_PATH = 'daftar_makanan/test/pizza/1152100.jpg' 

def main():
    # 1. Validasi keberadaan file gambar
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: File gambar '{IMAGE_PATH}' tidak ditemukan!")
        print("Pastikan file tersebut ada, atau ubah variabel IMAGE_PATH di atas.")
        return

    # 2. Membaca gambar menggunakan OpenCV (format bawaan BGR)
    img_bgr = cv2.imread(IMAGE_PATH)
    if img_bgr is None:
        print(f"Error: Gagal memuat file gambar dari '{IMAGE_PATH}'.")
        return

    # 3. Salin citra asli untuk membuat citra "After"
    img_after_bgr = img_bgr.copy()
    h, w, c = img_after_bgr.shape

    # Tentukan area tengah gambar (bounding box) berukuran 50% dari lebar & tinggi
    x1, y1 = int(w * 0.25), int(h * 0.25)
    x2, y2 = int(w * 0.75), int(h * 0.75)

    # Warna hijau di BGR untuk OpenCV: (Blue=0, Green=255, Red=0)
    color_green_bgr = (0, 255, 0)
    
    # Ketebalan garis dan font yang adaptif terhadap dimensi gambar
    thickness = max(2, int(min(w, h) * 0.008))
    font_scale = max(0.5, min(w, h) * 0.002)
    font_thickness = max(1, int(thickness * 0.6))

    # Gambar kotak pembatas hijau
    cv2.rectangle(img_after_bgr, (x1, y1), (x2, y2), color_green_bgr, thickness)

    # Menentukan teks label simulasi deteksi
    # Jika nama folder induk adalah kelas makanan, gunakan sebagai label. Default: "PIZZA"
    label_text = "PIZZA"
    parent_folder = os.path.basename(os.path.dirname(IMAGE_PATH)).upper()
    if parent_folder in ["PIZZA", "STEAK", "SUSHI"]:
        label_text = parent_folder

    # Posisi teks tepat di atas kotak hijau (y1)
    text_y = y1 - 10 if y1 - 10 > 15 else y1 + 25
    
    # Warna putih di BGR untuk OpenCV: (255, 255, 255)
    color_white_bgr = (255, 255, 255)

    # Menambahkan teks label putih di atas kotak hijau
    cv2.putText(img_after_bgr, label_text, (x1, text_y), 
                cv2.FONT_HERSHEY_SIMPLEX, font_scale, color_white_bgr, 
                font_thickness, cv2.LINE_AA)

    # 4. Konversi format warna dari BGR ke RGB untuk Matplotlib
    img_before_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_after_rgb = cv2.cvtColor(img_after_bgr, cv2.COLOR_BGR2RGB)

    # 5. Visualisasi Berdampingan (Side-by-Side) dengan Subplot Matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Subplot Kiri: Before (Citra Input)
    axes[0].imshow(img_before_rgb)
    axes[0].set_title("Before (Citra Input)", fontsize=14, fontweight='bold', pad=12)
    axes[0].axis('off')  # Sembunyikan koordinat dan garis tepi

    # Subplot Ranan: After (Hasil Deteksi)
    axes[1].imshow(img_after_rgb)
    axes[1].set_title("After (Hasil Deteksi)", fontsize=14, fontweight='bold', pad=12)
    axes[1].axis('off')  # Sembunyikan koordinat dan garis tepi

    # Tampilkan layout yang rapi
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
