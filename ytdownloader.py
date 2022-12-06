

# from pytube import YouTube
# import youtube_dl


# def run():
#     video_url = input("please enter youtube video url:")
#     video_info = youtube_dl.YoutubeDL().extract_info(
#         url=video_url, download=False
#     )
#     filename = f"{video_info['title']}.mp3"
#     options = {
#         'format': 'bestaudio/best',
#         'keepvideo': False,
#         'outtmpl': filename,
#     }

#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([video_info['webpage_url']])

#     print("Download complete... {}".format(filename))


# if __name__ == '__main__':
#     run()


# Mengimpor modul dari pytube
from pytube import YouTube

# mengambil input link dari user
link = input("Masukkan tautan/link video YouTube yang ingin anda unduh :  ")
yt = YouTube(link)


# Menampilkan detail dengan menggunakan property


def youtube():
    ("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)
    # Mprintendapatkan resolusi setinggi mungkin
    ys = yt.streams.get_highest_resolution()

    # mulai mengunduh
    print("Mendownload...")
    ys.download()
    print("Download Selesai!!")


youtube()
