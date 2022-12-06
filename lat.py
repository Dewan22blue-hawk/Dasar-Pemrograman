# """nomor = [2, 4, 7, 8]

# i = -1
# while i < len(nomor):
#     no = int(input("Masukkan angka = "))
#     if no in nomor:
#         print("Benar. ketemu di index ", i+1)
#         break
#     else:
#         print("salah")
#     i += 1
# """

# import pandas as pd

# list_nim = []
# list_nama = []
# list_uts = []
# list_uas = []
# list_total = []

# ulang = 5
# for i in range(ulang):
#     print('data Ke - ' + str(i+1))
#     list_nim.append(input('Nim : '))
#     list_nama.append(input('Nama :'))
#     list_uts.append(int(input('Nilai UTS : ')))
#     list_uas.append(int(input('Nilai UAS : ')))

# for i in range(ulang):
#     list_total.append((list_uas[i] + list_uts[i])/2)

# tamu = {
#     'NIM': list_nim,
#     'Nama Lengkap': list_nama,
#     'Nilai UTS': list_uts,
#     'Nilai UAS': list_uas,
#     'Rata-rata': list_total
# }
# data_tamu = pd.DataFrame(tamu)

# print('==================== Daftar Nilai ====================')
# print(data_tamu)
# print('======================================================')


# import sys
# list = [1, 2, "a", 0, "b", 6]
# for i in range(list):
#     try:
#         print("angka = ", i)
#         a = 1/int(i)
#         break
#     except:
#         print("maaf terjadi ", sys.exc_info()[0])
#         print("masukkan berikutnya ", )
#         print()
# print("Kebalikan dari ", i, "=", a)


try:
    buka = open('demo.txt')
    try:
        buka.read("loren ipsum decode encode dengan menggunakan pbkdf-2")
    except:

        print("kita bisa menulis")
    finally:
        buka.close()
except:
    print("Bisa dibuka dan berhasil")
