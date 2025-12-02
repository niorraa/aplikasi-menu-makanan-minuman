APLIKASI MENU MAKANAN & MINUMAN

Aplikasi Menu Makanan & Minuman merupakan perangkat lunak sederhana berbasis Python yang dirancang untuk membantu pengguna dalam menentukan pilihan menu secara praktis. Aplikasi ini menampilkan daftar makanan dan minuman yang tersedia, dilengkapi dengan informasi harga, sehingga pengguna dapat melihat opsi menu secara lebih jelas dan terstruktur.

Program ini berfungsi sebagai alat bantu interaktif yang memungkinkan pengguna melakukan proses pemilihan menu secara lebih cepat. Melalui antarmuka berbasis terminal, aplikasi ini memberikan pengalaman penggunaan yang mudah dipahami, baik oleh pengguna pemula maupun yang sudah terbiasa dengan aplikasi berbasis teks.

Selain sebagai alat pemilihan menu, aplikasi ini juga dikembangkan untuk tujuan pembelajaran, khususnya dalam memahami dasar-dasar pemrograman Python dan penerapan kerja kolaboratif menggunakan GitHub. Dengan adanya fitur pemilihan, pengolahan data sederhana, serta struktur kode yang terorganisasi, aplikasi ini menjadi contoh yang baik dalam membangun program kecil yang fungsional dan mudah dikembangkan.

Fitur Utama Aplikasi Menu Makanan & Minuman
Program Aplikasi Menu Makanan & Minuman memiliki beberapa fitur utama yang dirancang untuk membantu pengguna memilih menu secara manual maupun acak. Berikut adalah fitur-fitur utama yang tersedia:
1.	Menampilkan Daftar Menu Makanan & Minuman
Program menyediakan dua daftar menu:
•	Menu makanan lengkap dengan harga per item
•	Menu minuman lengkap dengan harga per item
Pengguna dapat melihat seluruh pilihan sebelum melakukan pemesanan atau pengacakan.
2.	Pemilihan Item Secara Manual
Pengguna dapat memilih item dengan menentukan nomor menu:
•	Pilih makanan manual
•	Pilih minuman manual
•	Pilih beberapa makanan
•	Pilih beberapa minuman
•	Pilih beberapa campuran (makanan + minuman)
Total harga otomatis dijumlahkan.
3.	Pengacakan Menu
Aplikasi menyediakan fitur acak untuk memudahkan pengguna yang bingung ingin pesan apa:
•	Acak makanan 1 item
•	Acak minuman 1 item
•	Acak combo (1 makanan + 1 minuman)
•	Acak beberapa makanan
•	Acak beberapa minuman
•	Acak beberapa campuran (makanan + minuman)
Semua hasil acak akan menampilkan item terpilih beserta total harga.
4.	Fitur Kombinasi Makanan + Minuman
Program menyediakan fitur:
•	Combo acak 1 makanan + 1 minuman
•	Memilih beberapa campuran secara manual
•	Acak campuran berbagai item dari kedua kategori
Fitur ini memberikan fleksibilitas yang lebih luas untuk pemesanan.
5.	Tampilan Interaktif & Bersih
Program menggunakan:
•	Clear screen otomatis (cls/clear) untuk tampilan menu yang bersih
•	Struktur menu yang rapi dan mudah digunakan
•	Loop utama (while True) sehingga pengguna dapat memilih menu berkali-kali tanpa keluar dari aplikasi.
6.	Perhitungan Total Otomatis
Setiap kali pengguna memilih beberapa item, program:
•	Menghitung total harga
•	Menampilkan semua item yang dipilih
•	Memberikan ringkasan akhir transaksi
Fitur ini membantu pengguna mengetahui estimasi biaya pesanan.
7.	Fitur Keluar
Program menyediakan pilihan untuk keluar dari aplikasi dengan aman ketika selesai digunakan.

Instalantasi & Cara Menjalankan
Instalasi
1. Pastikan Python Sudah Terinstal
   Program_utama.py ini dibuat menggunakan Python, jadi pengguna harus memiliki Python versi 3.14.
2. Download / Clone Proyek
   Untuk mendapatkan file program_utama.py, pengguna dapat:
   • Clone repository GitHub
   • git clone <link-repository-anda>
3. Masuk ke Folder Proyek
   Buka terminal / cmd, lalu masuk ke folder di mana file program_utama.py berada:
   • cd nama-folder-proyek
4. Pastikan Dependensi Standar Python Tersedia
   Program ini hanya menggunakan library bawaan Python seperti:
   • random
   • time
   • os
5. Jalankan Program
   Untuk menjalankan aplikasi:
   • python program_utama.py
   atau jika perangkat memakai python3:
   • python3 program_utama.py
   Program kemudian menampilkan menu interaktif yang berisi pilihan seperti:
   • pilih makanan/minuman manual
   • acak makanan/minuman
   • acak combo
   • mode campuran
   • dan keluar (exit)
6. Gunakan Terminal untuk Navigasi Program
   • Program menggunakan fungsi input & tampilan terminal.
   • Pengguna cukup mengetik angka menu sesuai pilihan.
   Contoh:
   1 → untuk pilih makanan manual  
   3 → acak makanan  
   5 → acak combo  
   12 → keluar aplikasi
   
Cara Menjalankan
Setelah proses instalasi selesai, ikuti langkah-langkah berikut untuk menjalankan aplikasi:
1. Buka Terminal / Command Prompt
   • Windows → buka Command Prompt
   • macOS / Linux → buka Terminal
2. Masuk ke Folder Tempat Program Berada
   Gunakan perintah:
   • cd nama-folder-proyek
   Ganti nama-folder-proyek dengan folder yang berisi file program_utama.py.
   Contoh:
   • cd AplikasiPilihanMakanan
3. Jalankan Program
   Gunakan salah satu perintah berikut, tergantung sistem:
   • Windows / sebagian sistem
   python program_utama.py
   • macOS / Linux / beberapa Windows
   python3 program_utama.py
   Setelah perintah dijalankan, program akan dimulai.
4. Ikuti Menu yang Tampil di Layar
   Program akan menampilkan menu seperti:
   1. Pilih Makanan
   2. Pilih Minuman
   3. Acak Makanan
   4. Acak Minuman
   5. Combo Acak
   ...
   12. Keluar
   Untuk menggunakan program:
   • Ketik nomor menu yang ingin dipilih
   • Tekan Enter
   • Ikuti instruksi berikutnya
   Contoh:
   • Masukkan pilihan: 3
   Program akan mengacak makanan dan menampilkan hasilnya.
5. Akhiri Program
   Untuk keluar dari aplikasi:
   • Pilih menu: 12
   Program akan menampilkan pesan keluar dan berhenti.

   

