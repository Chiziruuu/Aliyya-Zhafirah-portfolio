from flask import Flask, render_template

app = Flask(__name__)

DATA = {
    "nama": "Aliyya Zhafirah",
    "nama_pendek": "Aliyya",
    "prodi": "Teknologi Rekayasa Sistem Elektronika",
    "kampus": "Politeknik Caltex Riau",
    "angkatan": "2024",
    "ipk": "3.97",
    "ttl": "Kuok, 26 Juni 2006",
    "domisili": "Simpang Pawuo",
    "email": "aliyya24trse@mahasiswa.pcr.ac.id",
    "whatsapp": "082288651983",
    "instagram": "@aliyyazhafrh",
    "tagline": "Embedded System & Electronics Engineering Student",
    "hero_kalimat": "Merancang masa depan melalui elektronika, sistem tertanam, dan otomasi industri.",
    "tentang": "Saya adalah mahasiswa Program Studi Teknologi Rekayasa Sistem Elektronika angkatan 2024 yang memiliki minat besar dalam bidang elektronika, sistem tertanam (embedded system), otomasi industri, dan teknologi manufaktur. Saat ini saya aktif mempelajari mikroprosesor dan mikrokontroler, sistem kontrol, serta sistem instrumentasi untuk mendukung pengembangan solusi berbasis teknologi. Saya memiliki ketertarikan dalam perancangan perangkat keras dan perangkat lunak, serta senang mengembangkan proyek yang mengintegrasikan elektronika dengan sistem otomatis.",
    "motto": "Menimba ilmu adalah perjalanan tanpa batas. Tidak ada kata terlambat untuk belajar, karena setiap pengetahuan yang diperoleh hari ini adalah bekal untuk masa depan yang lebih baik.",

    "hard_skills": [
        "Pemrograman C", "Arduino", "Embedded System", "Mikroprosesor",
        "Mikrokontroler", "Elektronika Analog", "Elektronika Digital",
        "Sistem Kontrol", "Sistem Instrumentasi", "PCB Design",
        "Schematic Design", "PCB Layout", "Wiring Elektronika",
        "Troubleshooting Hardware", "Proteus", "Eagle",
        "Visual Studio Code", "Microsoft Office", "Microsoft Excel", "LabVIEW",
    ],
    "soft_skills": [
        "Leadership", "Teamwork", "Problem Solving",
        "Critical Thinking", "Time Management",
        "Communication Skills", "Public Speaking",
        "Adaptability", "Project Management",
    ],

    "organisasi": [
        {
            "nama": "Himpunan Mahasiswa Teknologi Rekayasa Sistem Elektronika (HIMIKA)",
            "singkatan": "HIMIKA",
            "jabatan": "Staff Kementerian Riset dan Teknologi",
            "periode": "2025 – 2026",
            "tugas": [
                "Mengembangkan program kerja berbasis teknologi dan inovasi.",
                "Melakukan penelitian terkait perkembangan elektronika dan teknologi industri.",
                "Mengelola program pelatihan teknis bagi mahasiswa.",
                "Mendukung kompetisi teknologi dan proyek rekayasa.",
                "Membantu pengembangan proyek elektronika dan embedded system.",
            ],
        },
        {
            "nama": "ICON",
            "singkatan": "ICON",
            "jabatan": "Staff Divisi Riset dan Teknologi",
            "periode": "2025 – 2026",
            "tugas": [
                "Melakukan riset dan analisis teknologi.",
                "Mengembangkan dan mengimplementasikan proyek teknologi organisasi.",
                "Berpartisipasi dalam perancangan, pengujian, dan evaluasi sistem elektronik.",
                "Menyelenggarakan workshop dan sesi pelatihan teknologi.",
                "Menyiapkan dokumentasi riset dan laporan proyek.",
            ],
        },
    ],

    "kepanitiaan": [
        {
            "nama": "HIMIKA RoboCamp",
            "jabatan": "Divisi Riset dan Teknologi",
            "tahun": "2025",
            "tugas": [
                "Menyiapkan materi pelatihan robotika dan elektronika.",
                "Memberikan mentoring teknis kepada peserta.",
                "Membantu perakitan dan pemrograman robot.",
                "Memfasilitasi sesi praktik robotika.",
            ],
        },
        {
            "nama": "RoboArm",
            "jabatan": "Divisi Riset dan Teknologi",
            "tahun": "2025",
            "tugas": [
                "Membimbing siswa SMA dalam kegiatan pembelajaran robotika.",
                "Menyampaikan pelatihan dasar elektronika dan pemrograman.",
                "Membantu proses perakitan dan pengujian robot.",
                "Mendukung penyiapan materi pembelajaran teknis.",
            ],
        },
        {
            "nama": "JTIN EXPO",
            "jabatan": "Divisi Event",
            "tahun": "2025",
            "tugas": [
                "Merencanakan dan mengelola kegiatan acara.",
                "Mengatur jadwal dan pelaksanaan acara.",
                "Berkoordinasi dengan peserta, pembicara, dan panitia.",
                "Memastikan kelancaran operasional acara sesuai rundown.",
            ],
        },
        {
            "nama": "P5 SMAN 16 Pekanbaru",
            "jabatan": "Instruktur Robotika Line Follower",
            "tahun": "2025",
            "tugas": [
                "Mengajarkan dasar-dasar robotika line follower.",
                "Membimbing siswa dalam perakitan elektronik dan soldering.",
                "Membantu pengujian dan troubleshooting robot.",
                "Meningkatkan pemahaman siswa tentang robotika dan elektronika dasar.",
            ],
        },
        {
            "nama": "Roboschool",
            "jabatan": "Divisi Event",
            "tahun": "2024",
            "tugas": [
                "Merencanakan konsep acara dan eksekusi teknis.",
                "Mengelola alur acara dan koordinasi peserta.",
                "Memastikan kegiatan berjalan sesuai jadwal.",
            ],
        },
    ],

    "proyek": [
        {
            "nama": "Digital Door Lock System",
            "subjudul": "Menggunakan Keypad & Solenoid Lock",
            "tahun": "2024",
            "ikon": "🔐",
            "teknologi": ["Mikrokontroler", "Keypad", "Solenoid Lock", "PCB Design"],
            "deskripsi": "Merancang dan mengimplementasikan sistem kunci pintu digital berbasis mikrokontroler menggunakan autentikasi keypad dan aktuasi solenoid lock. Bertanggung jawab atas pemrograman, desain skematik, layout PCB, wiring, dan integrasi hardware.",
        },
        {
            "nama": "Analog Line Follower Robot",
            "subjudul": "Robot Pelacak Jalur Otomatis",
            "tahun": "2024",
            "ikon": "🤖",
            "teknologi": ["Rangkaian Analog", "Sensor", "PCB Layout", "Soldering"],
            "deskripsi": "Merancang dan membangun robot line follower analog yang mampu melacak jalur secara otomatis menggunakan sensor dan rangkaian elektronika analog. Bertanggung jawab atas desain skematik, layout PCB, perakitan, dan soldering.",
        },
    ],

    "prestasi": [
        {
            "nama": "Juara 2 – Kategori General Line Follower",
            "kompetisi": "Minangkabau Robot Contest IX",
            "tahun": "2025",
            "penyelenggara": "Politeknik Negeri Padang",
            "tingkat": "Nasional",
            "ikon": "🥈",
        },
    ],

    "hobi": [
        {"nama": "Membaca Novel",                    "ikon": "📚", "detail": "Aksi & Fantasi"},
        {"nama": "Mengoprek Elektronik",             "ikon": "🔧", "detail": "Hardware & Gadget"},
        {"nama": "Mempelajari Hal Baru",             "ikon": "💡", "detail": "Teknologi & Inovasi"},
        {"nama": "Mengikuti Perkembangan Teknologi", "ikon": "📱", "detail": "Tech News & Trends"},
    ],

    "minat": [
        "Elektronika", "Embedded System", "Otomasi Industri",
        "Teknologi Manufaktur", "Pengembangan Website", "TouchDesigner",
    ],

    "gallery": [
        {"judul": "Divisi Acara Roboschool",               "foto": "img/gallery/img1.jpg"},
        {"judul": "Siswa merakit robot",                   "foto": "img/gallery/img2.jpg"},
        {"judul": "Kunjungan tim ke SMAN 16",              "foto": "img/gallery/img3.jpg"},
        {"judul": "Pembuatan bahan ajar untuk ke SMAN 16", "foto": "img/gallery/img4.jpg"},
        {"judul": "Tim pengajar robotik SMAN 16",          "foto": "img/gallery/img5.jpg"},
        {"judul": "Dokumentasi siswa merakit robot",       "foto": "img/gallery/img6.jpg"},
        {"judul": "HIMIKA RoboCamp",                       "foto": "img/gallery/img7.jpg"},
        {"judul": "Alat yang dipamerkan saat RoboCamp",    "foto": "img/gallery/img8.jpg"},
    ],
}


@app.route("/")
def index():
    return render_template("index.html", d=DATA)


if __name__ == "__main__":
    app.run(debug=True)
