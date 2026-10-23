"""Aplikasi sederhana untuk mengelola koleksi buku."""

from datetime import date

koleksi_buku: list[dict[str, str | int]] = []


def tambah_buku() -> None:
    """Meminta data buku lalu menambahkannya ke koleksi."""
    kode_buku = input("Kode buku: ").strip()
    judul = input("Judul: ").strip()
    penulis = input("Penulis: ").strip()
    tahun = input("Tahun terbit: ").strip()
    genre = input("Genre: ").strip()

    if not kode_buku:
        print("Kode buku wajib diisi.")
        return
    if any(
        str(buku["kode_buku"]).casefold() == kode_buku.casefold()
        for buku in koleksi_buku
    ):
        print("Kode buku sudah digunakan.")
        return
    if not judul or not penulis or not tahun.isdecimal() or not genre:
        print("Data tidak valid. Semua kolom wajib diisi dan tahun harus berupa angka.")
        return

    try:
        tahun_terbit = int(tahun)
    except ValueError:
        print("Data tidak valid. Tahun terbit harus berupa angka.")
        return
    if tahun_terbit <= 0 or tahun_terbit > date.today().year:
        print(f"Tahun terbit harus antara 1 dan {date.today().year}.")
        return

    id_buku = max((int(buku["id"]) for buku in koleksi_buku), default=0) + 1
    koleksi_buku.append(
        {
            "id": id_buku,
            "kode_buku": kode_buku,
            "judul": judul,
            "penulis": penulis,
            "tahun": tahun_terbit,
            "genre": genre,
            "status": "Tersedia",
        }
    )
    print("Buku berhasil ditambahkan.")


def tampilkan_buku(daftar_buku: list[dict[str, str | int]] | None = None) -> None:
    """Menampilkan semua buku atau daftar buku yang diberikan."""
    buku_yang_ditampilkan = koleksi_buku if daftar_buku is None else daftar_buku
    tampilkan_tabel(buku_yang_ditampilkan)


def tampilkan_tabel(daftar_buku: list[dict[str, str | int]]) -> None:
    """Menampilkan daftar buku dalam tabel beserta ringkasan status."""
    kolom = (
        ("ID", "id"),
        ("Kode Buku", "kode_buku"),
        ("Judul", "judul"),
        ("Penulis", "penulis"),
        ("Tahun", "tahun"),
        ("Genre", "genre"),
        ("Status", "status"),
    )
    lebar_kolom = [
        max(
            [
                len(judul),
                *(len(str(buku.get(kunci, "-"))) for buku in daftar_buku),
            ]
        )
        for judul, kunci in kolom
    ]
    format_baris = " | ".join(f"{{:<{lebar}}}" for lebar in lebar_kolom)

    print()
    print(format_baris.format(*(judul for judul, _ in kolom)))
    print("-+-".join("-" * lebar for lebar in lebar_kolom))
    for buku in daftar_buku:
        print(
            format_baris.format(
                *(str(buku.get(kunci, "-")) for _, kunci in kolom)
            )
        )

    tersedia = sum(
        str(buku.get("status", "")).casefold() == "tersedia"
        for buku in daftar_buku
    )
    dipinjam = sum(
        str(buku.get("status", "")).casefold() == "dipinjam"
        for buku in daftar_buku
    )
    print(
        f"\nRingkasan: Total {len(daftar_buku)} | "
        f"Tersedia {tersedia} | Dipinjam {dipinjam}"
    )


def tampilkan_detail_buku(buku: dict[str, str | int]) -> None:
    """Menampilkan detail satu buku."""
    print("\nDetail Buku")
    for label, kunci in (
        ("ID", "id"),
        ("Kode Buku", "kode_buku"),
        ("Judul", "judul"),
        ("Penulis", "penulis"),
        ("Tahun", "tahun"),
        ("Genre", "genre"),
        ("Status", "status"),
    ):
        print(f"{label}: {buku[kunci]}")


def cari_buku() -> None:
    """Mencari buku berdasarkan kode atau judul."""
    kata_kunci = input("Masukkan kode buku atau judul/kata kunci: ").strip()
    if not kata_kunci:
        print("Kata kunci pencarian tidak boleh kosong.")
        return

    buku_kode = next(
        (buku for buku in koleksi_buku if str(buku["kode_buku"]) == kata_kunci),
        None,
    )
    if buku_kode is not None:
        tampilkan_detail_buku(buku_kode)
        return

    kata_kunci = kata_kunci.casefold()
    hasil = [
        buku
        for buku in koleksi_buku
        if kata_kunci in str(buku["judul"]).casefold()
    ]
    tampilkan_buku(hasil)


def update_buku() -> None:
    """Mengubah status buku berdasarkan ID."""
    id_buku = input("Masukkan ID buku yang akan diperbarui: ").strip()
    buku = next(
        (item for item in koleksi_buku if str(item["id"]) == id_buku),
        None,
    )
    if buku is None:
        print("Buku dengan ID tersebut tidak ditemukan.")
        return

    status_saat_ini = str(buku["status"])
    status_baru = {
        "tersedia": "Dipinjam",
        "dipinjam": "Tersedia",
    }.get(status_saat_ini.casefold())
    if status_baru is None:
        print(f'Status buku "{status_saat_ini}" tidak dapat diperbarui.')
        return

    tampilkan_detail_buku(buku)
    konfirmasi = input(
        f"Ubah status menjadi {status_baru}? (y/n): "
    ).strip().casefold()
    if konfirmasi != "y":
        print("Perubahan status dibatalkan.")
        return

    buku["status"] = status_baru
    print(f"Status buku berhasil diubah menjadi {status_baru}.")


def filter_buku() -> None:
    """Memfilter buku berdasarkan genre."""
    genre = input("Masukkan genre: ").strip()
    if not genre:
        print("Kata kunci genre tidak boleh kosong.")
        return

    genre = genre.casefold()
    hasil = [
        buku
        for buku in koleksi_buku
        if genre in str(buku["genre"]).casefold()
    ]
    tampilkan_buku(hasil)


def hapus_buku() -> None:
    """Menghapus buku berdasarkan ID."""
    id_buku = input("Masukkan ID buku yang akan dihapus: ").strip()
    buku = next(
        (item for item in koleksi_buku if str(item["id"]) == id_buku),
        None,
    )
    if buku is None:
        print("Buku dengan ID tersebut tidak ditemukan.")
        return

    tampilkan_detail_buku(buku)
    if str(buku["status"]).casefold() == "dipinjam":
        print("Buku yang sedang dipinjam tidak boleh dihapus.")
        return

    konfirmasi = input("Yakin ingin menghapus buku ini? (y/n): ").strip().casefold()
    if konfirmasi != "y":
        print("Penghapusan buku dibatalkan.")
        return

    koleksi_buku.remove(buku)
    print("Buku berhasil dihapus.")


def main() -> None:
    """Menjalankan menu utama aplikasi."""
    menu = {
        "1": ("Tambah buku", tambah_buku),
        "2": ("Tampilkan buku", tampilkan_buku),
        "3": ("Cari buku", cari_buku),
        "4": ("Update status buku", update_buku),
        "5": ("Filter buku berdasarkan genre", filter_buku),
        "6": ("Hapus buku", hapus_buku),
    }

    while True:
        print("\n=== Aplikasi Koleksi Buku ===")
        for nomor, (nama, _) in menu.items():
            print(f"{nomor}. {nama}")
        print("0. Keluar")

        try:
            pilihan = input("Pilih menu: ").strip()
        except EOFError:
            print("\nInput berakhir. Program ditutup.")
            break
        if pilihan == "0":
            print("Terima kasih.")
            break
        if pilihan not in menu:
            print("Pilihan tidak tersedia.")
            continue
        try:
            menu[pilihan][1]()
        except EOFError:
            print("\nInput berakhir. Program ditutup.")
            break


if __name__ == "__main__":
    main()
