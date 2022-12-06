# Program Absenesi

data = 'y'
while data == 'y':
    print("============================================================================")
    print("\t\t      Aplikasi Absensi Kelas SI - 1A")
    print("")
    print("\t\tUniversitas Bina Sarana Informatika")
    print("\t\t\t Jurusan Sistem Informasi")
    print("\t\t     D3/S1 - Sistem Informasi")
    print("============================================================================")

    nama = input("Masukkan Nama Anda \t: ")
    nim = input("Masukkan NIM Anda \t: ")

# Menentukan Hari

    hari = 1
    while hari != 0:
        print("1. Senin")
        print("2. Selasa")
        print("3. Rabu")
        print("4. Kamis")
        print("5. Jum'at")

        hari = input("Pilih hari \t\t: ")
        print("")

        if hari == '1':
            absen = float(input("Jam Masuk \t\t: "))
            if absen <= 12.35:
                print("")
                print("==============================================")
                print("Absen Berhasil, Kuliah akan dimulai pukul 12.30")
                print("==============================================")
                print("")

            elif absen >= 12.36:
                print("")
                print("=================================")
                print("Absen Gagal, Anda sudah terlambat")
                print("=================================")
                print("")
                break

            else:
                print("COBA LAGI")

            absen_pulang = input("Jam Keluar \t\t: ")
            print("")
            print("================================================")
            print("Semoga Harimu Menyenangkan, Hati - hati dijalan.")
            print("================================================")
            print("")
            break

        elif hari == '2':
            absen2 = float(input("Jam Masuk \t\t: "))
            if absen2 <= 07.05:
                print("")
                print("==============================================")
                print("Absen Berhasil, Kuliah akan dimulai pukul 07.00")
                print("==============================================")
                print("")

            elif absen2 >= 07.06:
                print("")
                print("=================================")
                print("Absen Gagal, Anda sudah terlambat")
                print("=================================")
                print("")
                break

            else:
                print("COBA LAGI")

            absen_pulang2 = input("Jam Keluar \t\t: ")
            print("")
            print("================================================")
            print("Semoga Harimu Menyenangkan, Hati - hati dijalan.")
            print("================================================")
            print("")
            break

        elif hari == '3':
            absen3 = float(input("Jam Masuk \t\t: "))
            if absen3 <= 10.25:
                print("")
                print("==============================================")
                print("Absen Berhasil, Kuliah akan dimulai pukul 10.20")
                print("==============================================")
                print("")

            elif absen3 >= 10.26:
                print("")
                print("=================================")
                print("Absen Gagal, Anda sudah terlambat")
                print("=================================")
                print("")
                break

            else:
                print("COBA LAGI")

            absen_pulang3 = input("Jam Keluar \t\t: ")
            print("")
            print("================================================")
            print("Semoga Harimu Menyenangkan, Hati - hati dijalan.")
            print("================================================")
            print("")
            break
        elif hari == '4':
            absen4 = float(input("Jam Masuk \t\t: "))
            if absen4 <= 14.05:
                print("")
                print("==============================================")
                print("Absen Berhasil, Kuliah akan dimulai pukul 14.00")
                print("==============================================")
                print("")

            elif absen4 >= 14.06:
                print("")
                print("=================================")
                print("Absen Gagal, Anda sudah terlambat")
                print("=================================")
                print("")
                break

            else:
                print("COBA LAGI")

            absen_pulang4 = input("Jam Keluar \t\t: ")
            print("")
            print("================================================")
            print("Semoga Harimu Menyenangkan, Hati - hati dijalan.")
            print("================================================")
            print("")
            break

        elif hari == '5':
            absen5 = float(input("Jam Masuk \t\t: "))
            if absen5 <= 07.05:
                print("")
                print("==============================================")
                print("Absen Berhasil, Kuliah akan dimulai pukul 07.00")
                print("==============================================")
                print("")

            elif absen5 >= 07.06:
                print("")
                print("=================================")
                print("Absen Gagal, Anda sudah terlambat")
                print("=================================")
                print("")
                break

            else:
                print("COBA LAGI")

            absen_pulang5 = input("Jam Keluar \t\t: ")
            print("")
            print("================================================")
            print("Semoga Harimu Menyenangkan, Hati - hati dijalan.")
            print("================================================")
            print("")
            break

        else:
            print("================================")
            print(">>>>>>>>>> Hari Libur <<<<<<<<<<")
            print("================================")
            print("")
            break
