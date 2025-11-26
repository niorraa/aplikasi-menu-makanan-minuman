# ======================
#       FUNGSI UMUM
# ======================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_daftar(jenis, data):
    print(f"\n=== DAFTAR MENU {jenis.upper()} ===")
    for i, (nama, harga) in enumerate(data.items(), start=1):
        print(f"{i}. {nama} - Rp{harga:,}")
    print()

def pilih_satu_manual(data):
    try:
        nomor = int(input("Pilih nomor item: "))
        daftar = list(data.items())
        if 1 <= nomor <= len(daftar):
            nama, harga = daftar[nomor - 1]
            print(f"\nKamu memilih: {nama} (Rp{harga:,})")
            print(f"TOTAL: Rp{harga:,}")
        else:
            print("Nomor tidak ada!")
    except ValueError:
        print("Input harus angka!")

def pilih_beberapa_manual(data, jumlah):
    daftar = list(data)

    print("\n=== PILIH BEBERAPA ITEM ===")
    for i, (nama, harga) in enumerate(daftar, start=1):
        print(f"{i}. {nama} - Rp{harga:,}")

    total = 0
    dipilih = []

    for i in range(jumlah):
        try:
            nomor = int(input(f"Pilih item ke-{i+1}: "))
            if 1 <= nomor <= len(daftar):
                nama, harga = daftar[nomor - 1]
                dipilih.append((nama, harga))
                total += harga
            else:
                print("Nomor tidak ada!")
        except ValueError:
            print("Input harus angka!")
            return

    print("\n=== HASIL PILIHAN ===")
    for nama, harga in dipilih:
        print(f"- {nama} (Rp{harga:,})")

    print(f"\nTOTAL HARGA: Rp{total:,}")

def acak_beberapa(data, jumlah):
    hasil = random.sample(list(data.items()), jumlah)
    total = sum([h for _, h in hasil])

    print("\n=== HASIL ACAK ===")
    for nama, harga in hasil:
        print(f"- {nama} (Rp{harga:,})")

    print(f"\nTOTAL HARGA: Rp{total:,}")