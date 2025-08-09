class Indomie:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga


class Pesanan:
    def __init__(self):
        self.item = []

    def tambah_item(self, item):
        self.item.append(item)
        print(f"{item.nama} telah ditambahkan ke pesanan.")

    def total(self):
        return sum(item.harga for item in self.item)

    def tampilkan_pesanan(self):
        if not self.item:
            print("Pesanan Anda masih kosong.")
            return

        print("\nDaftar Pesanan:")
        for i, item in enumerate(self.item, 1):
            print(f"{i}. {item.nama} - Rp{item.harga:,.0f}")

        print(f"Total: Rp{self.total():,}")

    def checkout(self):
        if not self.item:
            print("Pesanan Anda masih kosong. Silakan tambahkan item terlebih dahulu.")
            return

        self.tampilkan_pesanan()
        konfirmasi = input("Apakah Anda ingin melanjutkan ke pembayaran? (ya/tidak): ").strip().lower()

        if konfirmasi == "ya":
            print("Terima kasih atas pesanan Anda!")
            self.item.clear()
        else:
            print("Pesanan dibatalkan. Tidak ada barang yang dibeli.")


def main():
    menu = [
        Indomie("Indomie Mi Goreng", 15000),
        Indomie("Indomie Ayam", 10000),
        Indomie("Indomie Sapi", 17000),
        Indomie("Indomie Sayur", 18000),
    ]

    pesanan = Pesanan()

    while True:
        print("\nMenu:")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.nama} - Rp{item.harga:,.0f}")

        print("5. Lihat Pesanan")
        print("6. Bayar")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan in ["1", "2", "3", "4"]:
            pesanan.tambah_item(menu[int(pilihan) - 1])

        elif pilihan == "5":
            pesanan.tampilkan_pesanan()

        elif pilihan == "6":
            pesanan.checkout()

        elif pilihan == "7":
            print("Terima kasih telah berkunjung! Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
