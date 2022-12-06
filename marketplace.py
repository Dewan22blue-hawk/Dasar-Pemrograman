import pandas as pd
import os
os.system('cls')


data_product = {
    1: "Laptop ",
    2: "Mouse  ",
    3: "Monitor",
    4: "Charger",
    5: "Mouse Pad",
    6: "Cassing"


}

data_harga = {
    1: 12000000,
    2: 55000,
    3: 650000,
    4: 120000,
    5: 25000,
    6: 1200000,
}

data = pd.DataFrame(data_harga)
print(data)
dict_trx = {}
daftar_metode_pembayaran = {
    1: "Transfer Bank",
    2: "Virtual Account",
    3: "Cash On Delivery",
    4: "Kartu Kredit"

}
print("==================================== List Product ===============================")
for i in data_product:
    print("id Product : ", i, "\t Nama Product :",
          data_product[i], "\t Harga Product : ", data_harga[i])

while True:
    print("\n\n")

    pilih_id = int(input("Pilih Id Product : "))

    if pilih_id in data_product:
        pilih_beli = input("Ingin beli ? (Y/N):")
        if pilih_beli == "y" or pilih_beli == "Y":
            nama_penerima = input("Nama Penerima     : ")
            alamat_penerima = input("Alamat Penerima : ")
            telepon = input("No. Hp                 : ")
            kurir_pengiriman = input("Kurir Pengiriman  : ")
            dict_trx = {
                "nama penerima": nama_penerima,
                "alamat penerima": alamat_penerima,
                "No Hp": telepon,
                "Kurir Pengiriman": kurir_pengiriman,
                "Product Id": data_product,

            }
        else:
            pass
        if len(dict_trx) > 0:
            print(
                "=======================Metode Pembayaran===============================")
        for i in daftar_metode_pembayaran:
            print("id :", i, "\t Metode Pembayaran : ",
                  daftar_metode_pembayaran[i])
        pilih_metode = int(input("Pilih ID Merode Pembayaran : "))
        if pilih_metode in daftar_metode_pembayaran:
            print("Nama Penerima : ", dict_trx["nama penerima"])
            print("Alamat Penerima : ", dict_trx["alamat penerima"])
            print("No HP : ", dict_trx["No Hp"])
            print("Kurir Pengiriman : ", dict_trx["Kurir Pengiriman"])
            print("Product : ", data_product[pilih_id])
            print("Harga : ", data_harga[pilih_id])
            print("Metode Pembayaran : ",
                  daftar_metode_pembayaran[pilih_metode])
            konfirmasi = input(
                "Apakah Anda Yakin Ingin Melakukan Pembayaran? (Y/N) : ")
            if konfirmasi == "y" or konfirmasi == "Y":
                print("Anda Sudah Berhasil Melakukan Pembayaran!")
            else:
                pass
        else:
            print("Id Metode Pembayaran Tidak Tersedia")
    else:
        print("Id Product Tidak Tersedia")
