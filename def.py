# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result


# i = int(input("masukan angka = "))
# print("\n\nRecursion Example Results")

# tri_recursion(i)

# def myfunc():
#     mat1 = [
#         [2, 3, 4],
#         [3, 4, 2]
#     ]

#     print(type(mat1[0]))


# myfunc()
# def harga_setelah_pajak(harga_dasar):
#     return harga_dasar + (harga_dasar * 10/100)


# harga_cilok = int(input("MAsukkan harga cilok = "))
# harga_final_cilok = harga_setelah_pajak(harga_cilok)
# print("Harga cilok 1 porsi Rp.", harga_final_cilok)

class Mobil:
    def __init__(self, roda, tipe, kecepatan):
        self.tipe = tipe
        self.roda = roda
        self.kecepatan = kecepatan

    def doMelaju(self):
        print("Melaju dengan kecepatan : ", self.kecepatan)

    def doKlakson(self):
        print("klakson")

    def doBelok(self, arah):
        print("Belok arah ", arah)


mobil1 = Mobil("4", 'Avanza', 'banter')
laju = mobil1.doMelaju
print()


class TheUnknown(object):

    @staticmethod
    def stat_method():
        print("Kan, gaada self yang diberikan disini!")


theObj = TheUnknown()
theObj.stat_method()

