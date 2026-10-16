# Pasang studio Ryan

Paket ini belum di-push atau di-deploy. README siap diunggah; tautan game sengaja menuju **source**, sampai alamat GitHub Pages benar-benar diuji.

## 1. Unggah ke profile repository

1. Ekstrak ZIP. Buka folder `ryanazryan` di dalamnya.
2. Simpan cadangan README lama jika ingin mempertahankannya.
3. Buka [repository profil](https://github.com/ryanazryan/ryanazryan), lalu **Add file → Upload files**.
4. Unggah **isi** folder `ryanazryan` ke root repository, bukan folder pembungkusnya. `README.md`, `assets/`, dan `docs/` harus berada di level yang sama. Pertahankan `design/`, `scripts/`, serta dokumen pendukung jika ingin mengedit dan memperbarui desain.
5. Periksa perubahan dan commit secara manual ke branch yang Anda pilih. Contoh instruksi berikut menggunakan `main`.
6. Kunjungi [profil GitHub](https://github.com/ryanazryan). Periksa gambar, tautan, tampilan terang/gelap, dan tampilan ponsel.

Gambar menggunakan SVG mandiri dengan gambar raster tertanam dan teks berbentuk path. Font kustom tidak perlu terpasang di perangkat pengunjung. `picture` menyediakan komposisi ponsel; gambar desktop tetap menjadi fallback. Teks Markdown di luar gambar memakai font asli GitHub.

<a id="game"></a>
## 2. Mainkan game lokal

Untuk cara paling sederhana, buka `docs/index.html` di browser modern. Semua CSS, JavaScript, dan font berada di folder lokal. Tidak ada server backend, akun, atau proses build.

Alternatif dengan server lokal, dari root folder hasil ekstrak:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Buka `http://127.0.0.1:8000/docs/`. Hentikan server dengan Ctrl+C. Pada Windows, gunakan `py` jika perintah `python` tidak tersedia.

**Kontrol:** klik atau Tab ke area ruangan, lalu WASD/panah untuk bergerak; E/Space untuk berinteraksi. Tombol arah dan Interact tersedia untuk layar sentuh. Text mode menyediakan seluruh permainan lewat tombol berlabel. Quiet motion mengikuti preferensi reduced motion perangkat dan bisa diubah. Tidak ada timer atau game-over; jawaban yang salah boleh dicoba lagi. Keberhasilan deployment adalah simulasi di dalam game.

## 3. Aktifkan GitHub Pages secara manual

1. Setelah `docs/` ada di repository, buka **Settings → Pages**.
2. Pada **Build and deployment**, pilih **Deploy from a branch**.
3. Pilih branch `main` (atau branch tempat Anda mengunggah) dan folder **`/docs`**, kemudian **Save**.
4. Tunggu proses Pages GitHub selesai. Gunakan alamat yang ditampilkan GitHub, lalu buka dan selesaikan satu permainan di desktop serta ponsel.

Alamat yang **diperkirakan**, bukan deployment terverifikasi dalam paket ini, adalah `https://ryanazryan.github.io/ryanazryan/`. Repository profil `ryanazryan` menggunakan path project; ini berbeda dari repository bernama `ryanazryan.github.io`.

Dokumentasi resmi: [creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site). Ketersediaan pengaturan dapat bergantung pada visibilitas repository dan akun.

## 4. Ganti tautan source menjadi play setelah berhasil

Setelah alamat Pages terbukti menampilkan game:

1. Di bagian **Explore my little world** pada `README.md`, ubah `<a href="docs/">` menjadi alamat Pages terverifikasi.
2. Ubah tautan **Browse the game source** menjadi **Play Ryan's Little Coding Studio**, dengan URL Pages yang sama. Tautan source terpisah boleh tetap dipertahankan.
3. Hapus kalimat bahwa game belum dipublikasikan. Perbarui alt text preview agar tidak lagi menyebut source-only.
4. Untuk memperbarui tulisan dalam gambar, edit fungsi `preview()` pada `design/build-assets.py`: ganti kedua tulisan `Game source included · Pages setup required` menjadi `Play the studio · Keyboard & touch`. Sesuaikan deskripsi SVG source-only di fungsi yang sama, lalu jalankan generator seperti di bawah.

Sebelum langkah ini, README tidak mengklaim game live. Jangan gunakan URL raw HTML GitHub sebagai tautan Play.

## 5. Edit visual atau perbarui kontribusi

Game dan README tidak memerlukan dependensi runtime eksternal. **Hanya untuk membangun ulang aset**, gunakan Python 3.10+ dan:

```sh
python -m pip install fonttools
python design/build-assets.py
```

Teks, warna, tata letak, dan jenis huruf ada di `design/build-assets.py`; hasilnya masuk ke `assets/`. Font berlisensi SIL OFL beserta lisensinya ada di `docs/fonts/`. Ilustrasi input yang sudah dioptimalkan ada di `design/renders/`. Prompt asli ada di `design/art-prompts.md`.

Untuk menghasilkan versi SVG dengan teks yang masih bisa diedit:

```sh
python design/build-assets.py --editable
```

Hasil di `design/editable/` memerlukan font yang sesuai dalam aplikasi desain. README harus tetap memakai versi outlined di `assets/`, bukan versi editable.

Untuk memperbarui kalender kontribusi:

```sh
python scripts/update-contributions.py
python design/build-assets.py --activity-only
```

Perintah pertama hanya membaca kalender publik GitHub dan menyimpan `design/contributions.json`. Tanggal default mengikuti UTC+8. Perintah kedua membuat ulang gambar kontribusi dan blok statistik bertanda `activity:start` / `activity:end` pada README, termasuk tanggal, alt text, dan link. Periksa perubahan lalu unggah secara manual. Jika struktur kalender GitHub berubah, generator menolak data yang tidak lengkap; snapshot lama tetap tersedia. Jangan menghapus penanda blok.

Tidak ada GitHub Actions kustom dalam paket ini: snapshot sudah disertakan dan pembaruan manual tidak memerlukan token, izin tulis, service badge, atau commit bot. GitHub tetap menjalankan proses Pages bawaannya jika Anda mengaktifkan Pages. Achievements berbeda dari statistik: verifikasi ulang di profil sebelum mengganti nama atau tiernya.

## 6. Catatan penting

- Ilustrasi hero/proyek adalah karya konseptual yang dibuat dengan alat image generation, bukan screenshot aplikasi atau file Blender. Source tata letak dan aset raster tersedia; scene Blender tidak dibuat.
- Animasi hero hanya berupa cahaya lampu lembut di SVG desktop. Frame statis tetap utuh. SVG yang dianimasikan bisa ditampilkan statis oleh sebagian renderer/proxy; game menyediakan ambient motion secara langsung dan menghormati reduced motion.
- Ukiran achievement adalah ilustrasi tidak resmi. Pull Shark ×2 dan tiga nama achievement lain diverifikasi dari profil live; tidak ada tier tambahan yang ditebak.
- Statistik adalah snapshot kalender publik, bukan penghitung live atau data lengkap aktivitas privat. Data awal mencakup 1 Januari–16 Oktober 2026.
- Link Discord dipertahankan dari profil lama dan instruksi Anda, tetapi validitas undangannya tidak dapat diverifikasi dalam sesi ini. Periksa dan ganti secara manual jika sudah kedaluwarsa.
- [VERIFICATION.md](VERIFICATION.md) mencatat bukti source dan batas verifikasi. [QA.md](QA.md) mencatat pengujian aktual. [CREDITS.md](CREDITS.md) mencatat font dan artwork.
