# 🌿 Portfolio Aliyya Zhafirah — Flask

Website portofolio pribadi dengan tema Hijau-Putih modern.

## Struktur Folder

```
aliyya/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── img/
        ├── profile.jpg       ← foto profil (sudah ada)
        └── gallery/          ← taruh foto kegiatan di sini
```

## Cara Menjalankan

```cmd
D:
cd "Semester 4\Mikro teori\aliyya"
python app.py
```

Buka browser: http://127.0.0.1:5000

## Cara Ganti Foto Gallery

1. Buat folder `static/img/gallery/`
2. Taruh foto kegiatan di sana (jpg/png)
3. Edit bagian `gallery` di `app.py` dan tambahkan path foto

## Fitur

- Hero dengan foto profil
- Dark mode toggle
- Animasi scroll
- Responsive (HP, tablet, desktop)
- Semua section lengkap
- Form kontak dummy
- Scroll to top button
