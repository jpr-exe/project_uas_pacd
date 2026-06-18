# Aplikasi Deteksi Makanan Pintar (Pizza, Steak, & Sushi)

Halo! Selamat datang di proyek **Aplikasi Klasifikasi Citra Makanan**. 

Pernahkah anda membayangkan bagaimana komputer bisa "melihat" dan mengenali makanan di piring kita? Aplikasi sederhana ini dibuat untuk menjawab rasa penasaran tersebut! Sistem ini dirancang untuk mengenali tiga jenis makanan populer secara otomatis: **Pizza**, **Steak**, dan **Sushi**.

---

## Bagaimana Cara Kerjanya? 

Bayangkan aplikasi ini seperti seorang koki digital yang memiliki kacamata khusus:
1. **Melihat Bentuk (HOG - Histogram of Oriented Gradients)**
Saat anda mengirimkan foto makanan, aplikasi ini tidak langsung menebak begitu saja. Pertama-tama, ia akan mengubah foto menjadi hitam-putih dan mendeteksi garis-garis tepi serta bentuk makanan tersebut (seperti bentuk bulat pada pizza atau pola gulungan pada sushi).
2. **Mencocokkan Pola (Logistic Regression)**
Setelah mendapatkan pola bentuknya, "koki digital" kita akan mencocokkannya dengan database pengetahuan yang sudah ia pelajari sebelumnya selama proses latihan (training).
3. **Hasil Deteksi (Scan Box)**
Aplikasi akan menampilkan gambar asli anda di sebelah kiri, dan di sebelah kanan ia akan memberikan kotak hijau pemindaian (seperti di film fiksi ilmiah!) lengkap dengan nama makanan yang berhasil ia kenali.

---

## Apa Saja Fiturnya?

*   **Pemindai Cerdas**
Dilengkapi dengan simulasi kotak pemindai (*scanning box*) berwarna hijau tepat di tengah makanan.
*   **Tampilan Berdampingan (Before vs After)**
Kamu bisa langsung membandingkan foto asli yang diunggah dengan hasil analisis sistem.
*   **Antarmuka Sederhana & Menarik**
Dibangun menggunakan Streamlit sehingga sangat mudah digunakan oleh siapa saja tanpa perlu memahami kode di baliknya.

---

## Cara Menjalankan Aplikasi di Komputermu

Bagi anda yang ingin mencobanya sendiri, ikuti langkah-langkah mudah berikut ini:

### 1. Persiapan
Pastikan anda sudah membuka terminal atau Command Prompt di folder tempat proyek ini disimpan.

### 2. Aktifkan Lingkungan Virtual (Virtual Environment)
Agar pustaka (library) aplikasi ini tidak mengganggu program lain di komputermu, kami menggunakan wadah khusus bernama `env`. Aktifkan wadah ini dengan perintah:

*   **Jika menggunakan Windows PowerShell:**
    ```powershell
    .\env\Scripts\Activate.ps1
    ```
*   **Jika menggunakan Windows Command Prompt (CMD):**
    ```cmd
    .\env\Scripts\activate.bat
    ```

### 3. Pasang Pustaka yang Dibutuhkan
Jika ini pertama kalinya anda menjalankan aplikasi, pasang semua pustaka pendukung dengan mengetikkan perintah berikut lalu tekan Enter:
```bash
pip install streamlit opencv-python numpy joblib scikit-image pillow matplotlib
```

### 4. Mulai Jalankan Aplikasi!
Ketik perintah di bawah ini untuk memulai aplikasi:
```bash
streamlit run app.py
```

Tunggu beberapa saat, dan browser internetmu akan otomatis terbuka menampilkan aplikasi ini. Sekarang, anda tinggal mengunggah foto Pizza, Steak, atau Sushi kesukaanmu!

---

## Struktur Folder Proyek
*   `app.py`: Program utama untuk memunculkan halaman web aplikasi.
*   `train_model.py`: Kode yang digunakan untuk melatih kecerdasan buatan agar bisa mengenali makanan.
*   `model_logreg.pkl`: "Otak" hasil latihan yang digunakan aplikasi untuk mengenali gambar.
*   `visualisasi_deteksi.py`: Skrip simulasi visual untuk melihat proses pendeteksian lewat grafik.

---
