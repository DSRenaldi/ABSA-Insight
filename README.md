# ABSA Insight

ABSA Insight adalah aplikasi dashboard untuk menganalisis komentar pelanggan PDAM menggunakan pendekatan **Aspect-Based Sentiment Analysis (ABSA)**. Aplikasi ini membantu pengguna mengetahui aspek layanan yang sedang dibicarakan sekaligus mengidentifikasi sentimen pada setiap komentar sebagai **positif**, **netral**, atau **negatif**.

## Tujuan Aplikasi

Aplikasi ini dirancang untuk membantu proses pemantauan dan evaluasi layanan PDAM berdasarkan komentar pelanggan. Hasil analisis disajikan dalam bentuk ringkasan, grafik, tren, dan tabel sehingga pengguna dapat lebih mudah:

- Mengetahui persebaran sentimen pelanggan.
- Mengidentifikasi aspek layanan yang paling sering dibahas.
- Melihat aspek yang memperoleh respons positif maupun negatif.
- Memantau perubahan sentimen dan pembahasan aspek dari waktu ke waktu.
- Menelusuri hasil analisis hingga ke komentar dan segmen teks terkait.

## Fitur Utama

- **Autentikasi pengguna** untuk membatasi akses ke dashboard.
- **Ringkasan analisis** berupa jumlah komentar, distribusi sentimen, dan aspek layanan teratas.
- **Analisis per aspek** untuk membandingkan sentimen pada setiap kategori layanan.
- **Visualisasi tren** sentimen dan aspek berdasarkan periode waktu.
- **Tabel data komentar** yang dilengkapi pencarian, filter tanggal, filter aspek, dan filter sentimen.
- **Detail segmentasi komentar** untuk melihat aspek dan sentimen dari setiap bagian komentar.
- **Ekspor data** hasil penyaringan komentar ke dalam berkas CSV.
- **Unggah dataset CSV** untuk memproses dan menyimpan data baru ke dalam dashboard.
- **Analisis komentar manual** untuk menguji satu komentar tanpa menyimpannya ke database.
- **Riwayat input data** untuk memantau proses penambahan dataset pengguna.

## Halaman Aplikasi

### Login

Halaman autentikasi yang harus dilalui sebelum pengguna dapat mengakses dashboard dan seluruh fitur analisis.

### Overview

Menampilkan gambaran umum data komentar, meliputi total komentar, jumlah sentimen positif, netral, dan negatif, aspek teratas, serta visualisasi distribusi aspek dan sentimen. Pengguna juga dapat memilih sumber data dan menyaring data berdasarkan rentang tanggal.

### Analisis Aspek

Menyajikan analisis performa setiap aspek layanan. Halaman ini menampilkan distribusi aspek, komposisi sentimen pada setiap aspek, serta skor yang membantu pengguna membandingkan respons pelanggan antar-aspek.

### Sentiments & Aspects Trends

Menampilkan perubahan sentimen dan aspek berdasarkan waktu. Visualisasi yang tersedia mencakup tren persebaran sentimen, tren aspek, distribusi aspek, sentimen per aspek, tren mingguan, dan heatmap sentimen negatif.

### Tabel Data Komentar

Menampilkan data komentar beserta hasil analisisnya secara lengkap. Pengguna dapat mencari komentar berdasarkan kata kunci, menyaring data berdasarkan tanggal, aspek, atau sentimen, membuka detail segmentasi komentar, dan mengunduh data hasil penyaringan.

### Input Data

Menyediakan dua metode pengujian dan penambahan data:

1. **CSV Dataset Upload** untuk memproses banyak komentar sekaligus dan menyimpan hasilnya ke database.
2. **Manual Entry** untuk menganalisis satu komentar tanpa menyimpan hasil pengujian ke database.

Halaman ini juga menyediakan contoh berkas CSV dan tabel riwayat input data.

## Format Data CSV

Berkas yang diunggah harus berformat `.csv` dan memiliki kolom berikut:

| Kolom | Keterangan |
| --- | --- |
| `postUrl` | Tautan sumber postingan tempat komentar diperoleh. |
| `comment_text` | Isi komentar yang akan dianalisis. |
| `ownerUsername` | Nama pengguna pemilik komentar. |
| `date` | Tanggal komentar atau postingan. |
| `month` | Bulan komentar atau postingan. |

Contoh struktur data:

```csv
postUrl,comment_text,ownerUsername,date,month
https://contoh.com/post/1,"Air di rumah saya sudah kembali lancar",pengguna_01,2025-01-15,January
https://contoh.com/post/2,"Tagihan bulan ini meningkat",pengguna_02,2025-01-16,January
```

Setelah diproses, aplikasi akan menghasilkan informasi berupa segmen komentar, prediksi aspek, dan label sentimen.

## Model ABSA

Penjelasan mengenai model, metodologi, pengolahan data, dan proses pengembangan Aspect-Based Sentiment Analysis yang digunakan pada aplikasi ini tersedia pada repositori berikut:

[Aspect-Based Sentiment Analysis Layanan PDAM](https://github.com/DSRenaldi/Aspect-Based-Sentiment-Analysis-Layanan-PDAM)
