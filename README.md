# Aplikasi Koleksi Buku

## 1. Nama Kelompok

**Nama kelompok:** [Isi nama kelompok]  
**Anggota:** [Isi nama dan NIM setiap anggota]

## 2. Deskripsi

Aplikasi konsol sederhana untuk mengelola koleksi buku. Data buku saat ini
disimpan sementara di dalam list `koleksi_buku` selama program berjalan.
Setiap buku memiliki ID otomatis, kode buku unik, judul, penulis, tahun terbit,
genre, dan status ketersediaan. Buku baru berstatus tersedia.

## 3. Cara Menjalankan

Pastikan Python 3 sudah terpasang. Buka terminal di folder proyek, lalu jalankan:

```bash
python main.py
```

Pada beberapa sistem, perintah yang digunakan adalah `python3 main.py`.
Pilih nomor menu dengan mengetik angka yang ditampilkan lalu tekan Enter.
Untuk keluar, pilih `0`. Data hanya tersimpan selama program berjalan; data
akan hilang saat aplikasi ditutup.

## 4. Fitur

| Menu | Cara pakai |
| --- | --- |
| 1. Tambah buku | Masukkan kode, judul, penulis, tahun terbit, dan genre. Semua kolom wajib diisi; kode harus unik dan tahun harus valid. |
| 2. Tampilkan buku | Menampilkan semua buku dalam tabel dan ringkasan jumlah total, tersedia, dan dipinjam. |
| 3. Cari buku | Masukkan kode untuk melihat detail buku yang cocok persis, atau masukkan kata kunci judul untuk mencari secara sebagian tanpa membedakan huruf besar/kecil. |
| 4. Update status buku | Masukkan ID buku. Status `Tersedia` dan `Dipinjam` akan ditukar setelah konfirmasi `y`. |
| 5. Filter buku berdasarkan genre | Masukkan kata kunci genre untuk mencari kecocokan sebagian tanpa membedakan huruf besar/kecil. |
| 6. Hapus buku | Masukkan ID buku. Detail dan konfirmasi ditampilkan sebelum menghapus; buku berstatus `Dipinjam` tidak dapat dihapus. |

Kata kunci pencarian dan genre tidak boleh kosong. Pada pertanyaan konfirmasi,
masukkan `y` untuk melanjutkan; jawaban lain membatalkan tindakan.

## 5. Pembagian Tugas

| Anggota | Tugas |
| --- | --- |
| [Nama dan NIM anggota 1] | Implementasi tambah buku, validasi data, dan tampilan koleksi. |
| [Nama dan NIM anggota 2] | Implementasi pencarian buku dan filter berdasarkan genre. |
| [Nama dan NIM anggota 3] | Implementasi update status, penghapusan buku, dan penanganan menu/input. |
