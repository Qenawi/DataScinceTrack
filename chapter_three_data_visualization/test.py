import string

from pytube import Playlist, YouTube
from pytube.cli import on_progress

mUrl = "https://www.youtube.com/playlist?list=PL4_bo90i-4GItp18iodTK2cv-Mzn0k1es"


def download_vedio(str: string, pl_name):
    try:
        print("Downloading vid", str, "\n")
        u = YouTube(str, on_progress_callback=on_progress)
        u.streams.filter(progressive=True, file_extension='mp4').first().download(pl_name + "/")
    except:
        print("err")


def download_all(l: [string], pl_name):
    print("\n", "downloading started ;) ", pl_name, len(l))
    for i in l:
        download_vedio(i, pl_name)
    print("\n", "Done tjw")


#playlist = Playlist(mUrl)
download_vedio("https://www.youtube.com/watch?v=EYKyhCkvsTI","wo_12")
#download_all(playlist.video_urls, playlist.title)
