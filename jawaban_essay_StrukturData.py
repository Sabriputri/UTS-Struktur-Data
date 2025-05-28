from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", "B", 18)
pdf.cell(200, 10, txt="UTS-STRUKTUR-DATA", ln=True, align="C")
pdf.ln(10)

# Isi
pdf.set_font("Arial", size=12)

isi = [
    "1. Jelaskan menurut anda apa itu struktur data!:",
    "Struktur data merupakan metode untuk menyimpan dan mengelola data dalam sebuah program supaya ",
    "lebih teratur, mudah diakses, dan efisien saat digunakan. Secara umum, struktur data terbagi ",
    "menjadi beberapa jenis, salah satunya adalah struktur data linear, yaitu data yang tersusun ",
    "secara berurutan seperti array, stack, queue, dan linked list. Struktur linear ini sendiri ",
    "bisa bersifat statis, contohnya array yang ukurannya tetap, dan dinamis, seperti linked list ",
    "yang ukurannya fleksibel. Selain itu, ada pula struktur data non-linear seperti tree dan graph ",
    "yang penyusunannya tidak berurutan melainkan bercabang atau saling terhubung satu sama lain. ",
    "Dengan memahami macam-macam struktur data tersebut, kita bisa membuat program yang lebih ",
    "optimal dan sesuai dengan kebutuhan pengolahan data.",
    "",

    "2, Jelaskan menurut anda kegunaan struktur data!",
    "Struktur data punya peran penting karena memudahkan proses pengolahan data dalam program. Dengan memilih struktur data yang tepat, kita bisa menghemat waktu, mempercepat proses pencarian, serta mengurangi penggunaan memori secara berlebihan.",
    "",

    "3. Sebutkan jenis-jenis struktur data yang anda ketahui dan jelaskan!",
    "Beberapa sedikit jenis struktur data yang saya kenal meliputi:",
    "- Array adalah kumpulan data yang berurutan dan dapat dicari dengan mudah.",
    "- Tumpukan adalah data yang pertama masuk akan keluar terahkhir ( LIFO).",
    "- Pohon merupakan suatu struktur data hierarkis yang terdiri atas semua simpul, dengan akar sebagai simpul pertama adalah simpul lainnya sebagai anak atau cabang. Struktur data hierarkis yang terdiri dari semua node, dengan akar menjadi node pertama danlainnya menjadi anak atau cabang.",
    "- Linked List (Daftar Tertaut): Sekumpulan data yang saling terhubung lewat penghubung (pointer), dan cocok dipakai kalau datanya sering berubah-ubah jumlahnya.",
    "",

    "4. Jelaskan menurut anda apa itu Array dan kegunaanya untuk apa!",
    "Pengertian dan fungsi array untuk menyimpan daftar nilai, data pengguna, atau elemen yang ingin kita akses secara berurutan dengan cepat.",
    "",

    "5. Berikan Contoh array yang anda ketahui!",
    "- Urutan rak sepatu.",
    "- Urutan kontak whatsApp.",
    "- Urutan nama siswa dalam satu kelas",
    "- Urutan nama hari dalam satu minggu",
    "",

    "6. Buatlah dengan bahasa pemograman yang anda kuasai contoh dari struktur data menurut pandangan anda!",
    "antrean_penjualan = ['Snack', 'Minuman', 'Makanan', 'Perlengkapan mandi']",
    "antrean_penjualan += ['Makanan ringan']",
    "print('Antrean sekarang:', antrean_penjualan)",
    "penjualan_dilayani = antrean_penjualan[0]",
    "antrean_penjualan = antrean_penjualan[1:]",
    "print('Penjualan yang dilayani:', penjualan_dilayani)",
    "print('Sisa antrean:', antrean_penjualan)",
    "",
]

for baris in isi:
    pdf.cell(200, 10, txt=baris, ln=True)

# Simpan PDF
pdf.output("Jawaban_UTS_Essay-Putri_Sabrina_Metekohy.pdf")

print("Jawaban_UTS_Essay-Putri_Sabrina_Metekohy.pdf")
