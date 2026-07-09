import statistics

# List untuk menyimpan data mahasiswa
mahasiswa = []

# =====================================
# FUNGSI INPUT DATA MAHASISWA
# =====================================
def input_mahasiswa():

    while True:
        nim = input("Masukkan NIM : ")

        if nim.isdigit():
            break

        print("NIM harus berupa angka!")

    nama = input("Masukkan Nama : ")

    prodi = input("Masukkan Prodi : ")

    while True:
        angkatan = input("Masukkan Angkatan : ")

        if angkatan.isdigit():
            break

        print("Angkatan harus berupa angka!")

    data = {
        "nim": nim,
        "nama": nama,
        "prodi": prodi,
        "angkatan": angkatan,
        "nilai": []
    }

    mahasiswa.append(data)
    print("Data berhasil disimpan")


# =====================================
# KONVERSI NILAI HURUF
# =====================================
def konversi_grade(nilai):
    if nilai >= 85:
        return "A", 4.0
    elif nilai >= 80:
        return "B+", 3.5
    elif nilai >= 75:
        return "B", 3.0
    elif nilai >= 70:
        return "C+", 2.5
    elif nilai >= 65:
        return "C", 2.0
    elif nilai >= 55:
        return "D", 1.0
    else:
        return "E", 0.0


# =====================================
# INPUT NILAI MAHASISWA
# =====================================
def input_nilai():

    nim = input("Masukkan NIM Mahasiswa : ")

    for mhs in mahasiswa:

        if mhs["nim"] == nim:

            while True:
                try:
                    jumlah_mk = int(input("Jumlah Mata Kuliah : "))

                    if jumlah_mk >= 5:
                        break
                    else:
                        print("Jumlah mata kuliah minimal 5.")

                except ValueError:
                    print("Masukkan angka yang benar.")

            for i in range(jumlah_mk):

                print(f"\nMata Kuliah ke-{i+1}")

                nama_mk = input("Nama Mata Kuliah : ")

                while True:
                    nilai = float(input("Nilai : "))

                    if 0 <= nilai <= 100:
                        break
                    
                    print("Nilai harus 0 sampai 100")

                while True:
                    sks = int(input("SKS : "))
                    if sks > 0:
                        break
                    print("SKS tidak boleh nol atau negatif")

                grade, bobot = konversi_grade(nilai)

                data_nilai = {
                    "matkul": nama_mk,
                    "nilai": nilai,
                    "sks": sks,
                    "grade": grade,
                    "bobot": bobot
                }

                mhs["nilai"].append(data_nilai)

            print("Nilai berhasil disimpan.")
            return

    print("NIM tidak ditemukan.")

# =====================================
# HITUNG IPK DAN RATA-RATA
# =====================================
def hitung_ipk(mhs):

    total_nilai = 0
    total_sks = 0
    total_bobot = 0

    for mk in mhs["nilai"]:

        total_nilai += mk["nilai"]
        total_sks += mk["sks"]
        total_bobot += mk["bobot"] * mk["sks"]

    if len(mhs["nilai"]) > 0:
        rata_rata = total_nilai / len(mhs["nilai"])
    else:
        rata_rata = 0

    if total_sks > 0:
        ipk = total_bobot / total_sks
    else:
        ipk = 0

    return rata_rata, ipk


# =====================================
# TAMPILKAN DATA MAHASISWA
# =====================================

def tampilkan_data():

    if not mahasiswa:
        print("\nBelum ada data mahasiswa.")
        return

    for mhs in mahasiswa:

        print("\n" + "="*70)
        print("             DATA MAHASISWA")
        print("="*70)
        print(f"NIM       : {mhs['nim']}")
        print(f"Nama      : {mhs['nama']}")
        print(f"Prodi     : {mhs['prodi']}")
        print(f"Angkatan  : {mhs['angkatan']}")

        if len(mhs["nilai"]) > 0:

            print("\n")
            print("-"*70)
            print("{:<3} {:<25} {:>8} {:>8} {:>8}".format(
                "No", "Mata Kuliah", "Nilai", "Grade", "SKS"))
            print("-"*70)

            for i, mk in enumerate(mhs["nilai"], start=1):
                print("{:<3} {:<25} {:>8} {:>8} {:>8}".format(
                    i,
                    mk["matkul"],
                    mk["nilai"],
                    mk["grade"],
                    mk["sks"]
                ))

            rata, ipk = hitung_ipk(mhs)

            print("-"*70)
            print(f"Rata-rata Nilai : {rata:.2f}")
            print(f"IPK             : {ipk:.2f}")

        else:
            print("\nBelum ada data nilai.")

        print("="*70)

# =====================================
# RANKING MAHASISWA
# =====================================
def ranking_mahasiswa():

    if not mahasiswa:
        print("Belum ada data mahasiswa.")
        return

    ranking = []

    for mhs in mahasiswa:
        rata, ipk = hitung_ipk(mhs)

        ranking.append({
            "nim": mhs["nim"],
            "nama": mhs["nama"],
            "ipk": ipk
        })

    ranking.sort(key=lambda x: x["ipk"], reverse=True)

    print("\n========== RANKING MAHASISWA ==========")

    for i, data in enumerate(ranking, start=1):
        print(f"{i}. {data['nama']}")
        print("   NIM :", data["nim"])
        print("   IPK :", round(data["ipk"], 2))


# =====================================
# STATISTIK KELAS
# =====================================
def statistik_kelas():

    if not mahasiswa:
        print("Belum ada data mahasiswa.")
        return

    daftar_ipk = []

    for mhs in mahasiswa:
        rata, ipk = hitung_ipk(mhs)
        daftar_ipk.append(ipk)

    print("\n========== STATISTIK KELAS ==========")
    print("Jumlah Mahasiswa :", len(mahasiswa))
    print("IPK Tertinggi :", round(max(daftar_ipk), 2))
    print("IPK Terendah :", round(min(daftar_ipk), 2))
    print("Rata-rata IPK :", round(statistics.mean(daftar_ipk), 2))

    if len(daftar_ipk) > 1:
        print("Standar Deviasi :", round(statistics.stdev(daftar_ipk), 2))
    else:
        print("Standar Deviasi : 0")
def rekap_kelas():

    if not mahasiswa:
        print("Belum ada data")
        return

    lulus = 0
    tidak_lulus = 0
    daftar_ipk = []

    grade_count = {
        "A": 0,
        "B+": 0,
        "B": 0,
        "C+": 0,
        "C": 0,
        "D": 0,
        "E": 0
    }

    print("\n========== REKAP KELAS ==========")

    for mhs in mahasiswa:

        rata, ipk = hitung_ipk(mhs)
        daftar_ipk.append(ipk)

        print(mhs["nama"], "-", round(ipk, 2))

        if ipk >= 2.00:
            lulus += 1
        else:
            tidak_lulus += 1

        for mk in mhs["nilai"]:
            grade_count[mk["grade"]] += 1

    print("\nJumlah Mahasiswa :", len(mahasiswa))
    print("Lulus :", lulus)
    print("Tidak Lulus :", tidak_lulus)
    print("IPK Tertinggi :", round(max(daftar_ipk), 2))
    print("IPK Terendah  :", round(min(daftar_ipk), 2))
    print("Rata-rata IPK :", round(statistics.mean(daftar_ipk), 2))

    print("\nDistribusi Grade")
    for grade, jumlah in grade_count.items():
        print(f"{grade} : {jumlah}")
# =====================================
# CETAK RAPOR
# =====================================
def cetak_rapor():

    nim = input("Masukkan NIM : ")

    for mhs in mahasiswa:

        if mhs["nim"] == nim:

            print("\n========== RAPOR MAHASISWA ==========")
            print("Nama      :", mhs["nama"])
            print("NIM       :", mhs["nim"])
            print("Prodi     :", mhs["prodi"])
            print("Angkatan  :", mhs["angkatan"])

            print("\nDaftar Nilai")

            for mk in mhs["nilai"]:
                print("--------------------------------")
                print("Mata Kuliah :", mk["matkul"])
                print("Nilai       :", mk["nilai"])
                print("Grade       :", mk["grade"])
                print("SKS         :", mk["sks"])

            rata, ipk = hitung_ipk(mhs)

            print("--------------------------------")
            print("Rata-rata :", round(rata, 2))
            print("IPK       :", round(ipk, 2))

            if ipk >= 3.50:
                predikat = "Cumlaude"
            elif ipk >= 3.00:
                predikat = "Sangat Memuaskan"
            elif ipk >= 2.50:
                predikat = "Memuaskan"
            else:
                predikat = "Cukup"

            print("Predikat :", predikat)
            return

    print("Mahasiswa tidak ditemukan.")

    # =====================================
# CARI MAHASISWA
# =====================================

def cari_mahasiswa():

    nim = input("Masukkan NIM : ")

    for mhs in mahasiswa:

        if mhs["nim"] == nim:

            print("\n===== DATA MAHASISWA =====")
            print("NIM :", mhs["nim"])
            print("Nama :", mhs["nama"])
            print("Prodi :", mhs["prodi"])
            print("Angkatan :", mhs["angkatan"])

            return

    print("Data tidak ditemukan.")
    # =====================================
# EDIT DATA
# =====================================

def edit_mahasiswa():

    nim = input("Masukkan NIM yang akan diedit : ")

    for mhs in mahasiswa:

        if mhs["nim"] == nim:

            print("Data ditemukan")

            mhs["nama"] = input("Nama Baru : ")
            mhs["prodi"] = input("Prodi Baru : ")

            while True:
                angkatan = input("Angkatan Baru : ")

                if angkatan.isdigit():
                    mhs["angkatan"] = angkatan
                    break

                print("Angkatan harus berupa angka!")

            print("Data berhasil diperbarui.")
            return

    print("Mahasiswa tidak ditemukan.")
# =====================================
# HAPUS DATA
# =====================================

def hapus_mahasiswa():

    nim = input("Masukkan NIM yang akan dihapus : ")

    for mhs in mahasiswa:

        if mhs["nim"] == nim:

            mahasiswa.remove(mhs)

            print("Data berhasil dihapus.")
            return

    print("Mahasiswa tidak ditemukan.")


# =====================================
# MENU UTAMA
# =====================================

while True:

    print("\n====================================")
    print(" SISTEM INFORMASI AKADEMIK ")
    print("====================================")
    print("1. Input Data Mahasiswa")
    print("2. Input Nilai Mahasiswa")
    print("3. Tampilkan Data Mahasiswa")
    print("4. Ranking Mahasiswa")
    print("5. Statistik Kelas")
    print("6. Cetak Rapor")
    print("7. Rekap Kelas")
    print("8. Cari Mahasiswa")
    print("9. Edit Mahasiswa")
    print("10. Hapus Mahasiswa")
    print("11. Keluar")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        input_mahasiswa()

    elif pilihan == "2":
        input_nilai()

    elif pilihan == "3":
        tampilkan_data()

    elif pilihan == "4":
        ranking_mahasiswa()

    elif pilihan == "5":
        statistik_kelas()

    elif pilihan == "6":
        cetak_rapor()

    elif pilihan == "7":
        rekap_kelas()

    elif pilihan == "8":
        cari_mahasiswa()

    elif pilihan == "9":
        edit_mahasiswa()

    elif pilihan == "10":
        hapus_mahasiswa()

    elif pilihan == "11":
        print("Program selesai")
        break