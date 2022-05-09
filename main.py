import pytube
from pytube import YouTube
from pytube import Playlist
import math_stuff
import os
import youtube_dl
import time
import re

#url = "https://www.youtube.com/watch?v=cyq5-StPISU"
root = os.path.dirname(__file__)

def Captions(url,makefile,filename=type(None),language=type(None)):
    yt = YouTube(url)
    if language == type(None):
        language = "en"
    caption = yt.captions.get_by_language_code(language)
    if filename == type(None):
        filename = f"{yt.title} {language} Captions.txt"
    if makefile == True:
        f = open(filename, "w", encoding="utf-8")
        captions = caption.generate_srt_captions()
        f.write(captions)
        f.close()
    return captions

def Download(url,AudioOnly=type(None),UseCaptions=type(None),CaptionsLanguage="en",Filename=type(None)):
    yt = YouTube(url)
    if AudioOnly == True:
        stream = yt.streams.get_by_itag(140)
        print("Approximate size:")
        print(f"{math_stuff.HumanBytes.format(stream.filesize_approx)} | Will now be downloaded!")
        ts = time.perf_counter()
        if Filename == type(None):
            Filename=f"{yt.title}.mp3"
        stream.download(filename=Filename,output_path=f"{root}/Downloads")
        tf = time.perf_counter()
        print(f"Done in {tf - ts:0.4f} seconds!")
    else:
        stream = yt.streams.get_highest_resolution()
        ts = time.perf_counter()
        if Filename == type(None):
            Filename=f"{yt.title}.mp4"
        print(f"{math_stuff.HumanBytes.format(stream.filesize_approx)} | Will now be downloaded!")
        stream.download(filename=Filename,output_path=f"{root}/Downloads")
        tf = time.perf_counter()
        print(f"Done in {tf - ts :0.4f} seconds!")
    return Filename

def Stream(url,VideoBeta=type(None)):
    if VideoBeta == True:
        print("|WARNING|\n The video option is very unstable, as it's still on development\nTrust me I'm trying my best ¯\_(ツ)_/¯\n also... it has a shitty quality :D ENJOY!")
        ydl_options = {"format":"bestvideo"}

        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url'] # This is not working well with playlists... but who the hell is going to stream playlists outta this crap!?
            os.system(f"""youtube-dl "{url}" -o - | ffplay - -autoexit""")
    else:
        print("Loading...")
        ydl_options = {"format":"bestaudio"}
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            print("OK! Enjoy your music!")
            os.system(f"""ffplay "{url2}" -nodisp -autoexit""")

def PlaylistDownload(playlist, SoundOnly=False):
    p = Playlist(playlist)
    print(f"Downloading: {p.title}")
    if SoundOnly == True:
        for video in p.videos:
            video.streams.get_highest_resolution().download(filename=f"{video.title}.mp3",output_path=f"{root}/Downloads") #For any dumb reason this is only working with getting the highest resolution video and turning it into mp3, no idea why
    else:
        for video in p.videos:
            video.streams.get_highest_resolution().download(filename=f"{video.title}.mp4",output_path=f"{root}/Downloads")
        
        


#Download(url="https://www.youtube.com/watch?v=Qp3b-RXtz4w", AudioOnly=True)
#Captions(url, True)
#Stream(url)
#PlaylistDownload()

#Made with <3 by ZackTheKill3r using pytube(to gather info and do 99% of the stuff), ffmpeg(used for playing the streaming), youtube_dl(used for streaming) and HumanBytes(used to transform bytes to easily human readable numbers)