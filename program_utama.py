# ======================
#     PROGRAM UTAMA
# ======================

def main():
    while True:
        clear()
        print("======================================")
        print(" 🍽️  APLIKASI PILIH MAKANAN & MINUMAN  🥤 ")
        print("======================================\n")

        print("1. Pilih makanan (manual)")
        print("2. Pilih minuman (manual)")
        print("3. Acak makanan 1 item")
        print("4. Acak minuman 1 item")
        print("5. Acak combo 1 makanan + 1 minuman")
        print("6. Pilih beberapa makanan (manual)")
        print("7. Pilih beberapa minuman (manual)")
        print("8. Acak beberapa makanan")
        print("9. Acak beberapa minuman")
        print("10. Acak beberapa campuran")
        print("11. Pilih beberapa campuran (manual)")
        print("12. Keluar\n")

        pilihan = input("Pilih menu: ")

        # --------------------------- MENU 1 ---------------------------
        if pilihan == "1":
            clear()
            tampilkan_daftar("Makanan", menu_makanan)
            pilih_satu_manual(menu_makanan)
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 2 ---------------------------
        elif pilihan == "2":
            clear()
            tampilkan_daftar("Minuman", menu_minuman)
            pilih_satu_manual(menu_minuman)
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 3 ---------------------------
        elif pilihan == "3":
            clear()
            nama, harga = random.choice(list(menu_makanan.items()))
            print("Hasil acak makanan:")
            print(f"- {nama} (Rp{harga:,})")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 4 ---------------------------
        elif pilihan == "4":
            clear()
            nama, harga = random.choice(list(menu_minuman.items()))
            print("Hasil acak minuman:")
            print(f"- {nama} (Rp{harga:,})")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 5 ---------------------------
        elif pilihan == "5":
            clear()
            m1, h1 = random.choice(list(menu_makanan.items()))
            m2, h2 = random.choice(list(menu_minuman.items()))
            print("Combo acak:")
            print(f"- {m1} (Rp{h1:,})")
            print(f"- {m2} (Rp{h2:,})")
            print(f"\nTOTAL: Rp{h1+h2:,}")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 6 ---------------------------
        elif pilihan == "6":
            clear()
            try:
                jumlah = int(input("Berapa item makanan ingin dipilih? "))
                pilih_beberapa_manual(list(menu_makanan.items()), jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 7 ---------------------------
        elif pilihan == "7":
            clear()
            try:
                jumlah = int(input("Berapa item minuman ingin dipilih? "))
                pilih_beberapa_manual(list(menu_minuman.items()), jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 8 ---------------------------
        elif pilihan == "8":
            clear()
            try:
                jumlah = int(input("Berapa makanan acak? "))
                acak_beberapa(menu_makanan, jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 9 ---------------------------
        elif pilihan == "9":
            clear()
            try:
                jumlah = int(input("Berapa minuman acak? "))
                acak_beberapa(menu_minuman, jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 10 (CAMPUR ACAK) ---------------------------
        elif pilihan == "10":
            clear()
            try:
                campuran = list(menu_makanan.items()) + list(menu_minuman.items())
                jumlah = int(input("Berapa item campuran acak? "))
                acak_beberapa(dict(campuran), jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 11 (CAMPUR MANUAL) ---------------------------
        elif pilihan == "11":
            clear()
            try:
                campuran = list(menu_makanan.items()) + list(menu_minuman.items())
                jumlah = int(input("Berapa item ingin dipilih? "))
                pilih_beberapa_manual(campuran, jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 12 (EXIT) ---------------------------
        elif pilihan == "12":
            print("Terima kasih! 👋")
            break

        else:
            print("Input tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()