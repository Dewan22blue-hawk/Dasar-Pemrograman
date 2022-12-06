import random
import pyfiglet

print(pyfiglet.figlet_format("PASSWORD GENERATOR"))


a = "abcdefghijklmnopqrstuvwxyz"
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
car = "[]{}#*;+_-%&$@!="

print("""Pilih Opsi :\n[1] Password kombinasi huruf alphabet (upper & lower)\n[2] Password kombinasi huruf kecil & angka\n[3] Password kombinasi huruf besar & angka\n[4] Password kombinasi huruf kecil & symbol\n[5] Password kombinasi huruf besar & symbol\n[6] Password kombinasi huruf alphabet (Upper & lower), angka, dan simbol
      
      
      
      
      """)
opsi = int(input("Masukkan opsi anda [1/2/3/4/5/6] : "))

if opsi == 1:
    pasw = a + upp
    panjang = 9
    password = "".join(random.sample(pasw, panjang))
    print("Password telah yang dibuat = ", password)
elif opsi == 2:
    semua = a + num
    length = 9
    password = "".join(random.sample(semua, length))
    print("Password telah yang dibuat = ", password)
elif opsi == 3:
    semua = upp + num
    length = 9
    password = "".join(random.sample(semua, length))
    print("Password telah yang dibuat = ", password)
elif opsi == 4:
    semua = a + car
    length = 9
    password = "".join(random.sample(semua, length))
    print("Password telah yang dibuat = ", password)
elif opsi == 5:
    semua = upp + car
    length = 9
    password = "".join(random.sample(semua, length))
    print("Password telah yang dibuat = ", password)
elif opsi == 6:
    semua = a + upp + num + car
    length = 9
    password = "".join(random.sample(semua, length))
    print("Password yang telah dibuat = ", password)
else:
    print("Opsi yang anda masukkan salah")
