from pytube import YouTube
import pyfiglet
import os
# Print Banner menggunakan modul pyfiglet
print(pyfiglet.figlet_format("YT Downloader"))


print("Powered By. Dewan")
print("=" * 15, "Silahkan Pilih Opsi Dari Downloader Dewan", "=" * 15)
print("""[1] Download Video\n[2] Download Audio\n\n""")
print("Jika ingin keluar dari program tekan (CTRL + C)")

# mengambil inputan opsi dari user
# menggunakan eksepsi
try:
    opsi = int(input("Masukkan Opsi Anda [1/2]: "))
    if opsi == 1:

        link = input("Masukkan Link YouTube Yang Ingin Anda Download : ")
        youtube_a = YouTube(link)
    # Function untuk opsi download video

        def yt():
            video = youtube_a.streams.all()
            vidd = list(enumerate(video))
            for x in vidd:
                print(x)

            resolusi = int(
                input("Masukkan resolusi video yang ingin anda download : "))
            video[resolusi].download()
            print("Download Telah Selesai")
        yt()

    elif opsi == 2:
        link = input("Masukkan Link YouTube Yang Ingin Anda Download : ")
        youtube_a = YouTube(link)

    # Function untuk opsi download audio
        def ado():
            audio = youtube_a.streams.filter(only_audio=True)
            vidd = list(enumerate(audio))
            for x in vidd:
                print(x)

            resolusi = int(
                input("Masukkan ukuran video yang ingin anda download : "))
            audio[resolusi].download()
            print("Download Telah Selesai")
        ado()
    else:
        print("Maaf opsi Yang anda masukkan salah !")
    os.system("clear")
except ValueError:
    print("yang anda masukkan bukanlah opsi yang tersedia")
except KeyboardInterrupt:
    print("Anda telah keluar dari program (CTRL + C)")
