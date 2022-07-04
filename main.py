from pytube import YouTube
from pytube import Playlist
import math_stuff
import os
import youtube_dl
import time
import re
from settings import language

if language == "English":
    from Languages.english import *
elif language == "Portuguese":
    from Languages.portuguese import *
elif language == "Japanese":
    from Languages.japanese import *

def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

root = os.path.dirname(__file__) 
core_version="Alpha 0.6.0"


def yt_title_converter(title): # This makes sure the filename doesn't piss the OS and also Python off
    safe_title = title
    safe_title = re.sub('[(){}<>/|*;:?]', ' ', safe_title)
    safe_title = safe_title.replace('"', "'")
    return safe_title
    
def Captions(url,makefile,filename=type(None),language=type(None)): #Downloads Captions
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

def AutoDownload(url,AudioOnly=type(None),UseCaptions=type(None),CaptionsLanguage="en",Filename=type(None)): #Downloads without asking for quality
    yt = YouTube(url)
    if AudioOnly == True:
        stream = yt.streams.get_by_itag(140)
        print(Main[0])
        print(f"{math_stuff.HumanBytes.format(stream.filesize_approx)} | {Main[1]}")
        ts = time.perf_counter()
        if Filename == type(None):
            Filename=f"{yt.title}"
            Filename=f"{yt_title_converter(title=Filename)}.mp3"
        stream.download(filename=Filename,output_path=f"{root}/Downloads")
        tf = time.perf_counter()
        timer_result = Main[2].replace('/s', f"{tf - ts:0.4f}")
        print(timer_result)
    else:
        stream = yt.streams.get_highest_resolution()
        ts = time.perf_counter()
        if Filename == type(None):
            Filename=f"{yt.title}"
            Filename=f"{yt_title_converter(Filename)}.mp4"
        print(f"{math_stuff.HumanBytes.format(stream.filesize_approx)} | {Main[1]} ")
        stream.download(filename=Filename,output_path=f"{root}/Downloads")
        tf = time.perf_counter()
        timer_result = Main[2].replace('/s', f"{tf - ts:0.4f}")
        print(timer_result)
    return Filename

def Download(url,AudioOnly=type(None),UseCaptions=type(None),CaptionsLanguage="en",Filename=type(None)): #Regular Download (Asks for quality)
    yt = YouTube(url)
    if AudioOnly == True:
        stream = yt.streams.get_by_itag(140)
        print(Main[0])
        print(f"{math_stuff.HumanBytes.format(stream.filesize_approx)} | {Main[1]}")
        ts = time.perf_counter()
        if Filename == type(None):
            Filename=f"{yt.title}"
            Filename=f"{yt_title_converter(title=Filename)}.mp3"
        stream.download(filename=Filename,output_path=f"{root}/Downloads")
        tf = time.perf_counter()
        timer_result = Main[2].replace('/s', f"{tf - ts:0.4f}")
        print(timer_result)
    else:
        print("| 144p |")
        print("| 360p |")
        print("| 480p |")
        print("| 720p |")
        print("| 1080p |")
        ic = input(Main[3])
        if "144" in ic:
            Uitag=17
            split = False
        elif "360" in ic:
            Uitag=22
            split = False
        elif "480" in ic:
            Uitag=135
            split = True
        elif "720" in ic:
            Uitag=22
            split = False
        elif "1080" in ic:
            Uitag=248
            split = True
        else:
            print(Main[4])
            return "Err1NQ"
        stream = yt.streams.get_by_itag(Uitag)
        audio = yt.streams.get_by_itag(140)
        ts = time.perf_counter()
        if Filename == type(None):
            Filename=f"{yt.title}"
            Raw_Filename=f"{yt_title_converter(Filename)} raw.mp4"
            Filename=f"{yt_title_converter(Filename)}.mp4"
            audioname=f"{yt_title_converter(Filename)}.mp3"
        try:
            print(f"{math_stuff.HumanBytes.format(stream.filesize_approx + audio.filesize_approx)} | {Main[1]}")
        except:
            print(Main[4])
            return "Err1NQ"
        stream.download(filename=Raw_Filename,output_path=f"{root}/Downloads")
        if split == True:
            audio.download(filename=audioname,output_path=f"{root}/Downloads")
            os.system(f"""ffmpeg -loglevel quiet -y -i "Downloads/{Raw_Filename}" -i "Downloads/{audioname}" -c:v copy -c:a aac "Downloads/{Filename}" """) #Calls ffmpeg to mix the audio and video together
            os.remove(f"{root}/Downloads/{Raw_Filename}") #Deletes the mute videofile
            os.remove(f"{root}/Downloads/{audioname}") #Deletes the audiofile
        tf = time.perf_counter()
        timer_result = Main[2].replace("/s",f"{tf - ts:0.4f}")
        print(timer_result)
    return Filename

def Stream(url,VideoBeta=type(None)): #Video/Audio Streaming
    if VideoBeta == True:
        print(Main[5])
        ydl_options = {"format":"bestvideo"}

        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][6]['url'] # This is not working well with playlists... but who the hell is going to stream playlists outta this crap!?
            os.system(f"""youtube-dl "{url}" -o - | ffplay - -autoexit""")
    else:
        print(Main[8])
        ydl_options = {"format":"bestaudio"}
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            print(Main[6])
            os.system(f"""ffplay "{url2}" -nodisp -autoexit""")

def PlaylistDownload(playlist, SoundOnly=False): #Downloads playlists using the AutoDownload Method
    p = Playlist(playlist)
    playlist_title = Main[7].replace("/pt",f"{p.title}")
    print(playlist_title)
    if SoundOnly == True:
        for video in p.videos:
            safe_title = yt_title_converter(video.title) # Forgot to add this oops
            video.streams.get_audio_only().download(filename=f"{safe_title}.mp3",output_path=f"{root}/Downloads")
    else:
        for video in p.videos:
            safe_title = yt_title_converter(video.title)
            video.streams.get_highest_resolution().download(filename=f"{safe_title}.mp4",output_path=f"{root}/Downloads")


#Made with <3 by ZackTheKill3r using pytube(to gather info and do 99% of the stuff), ffmpeg(used for playing the streaming), youtube_dl(used for streaming) and HumanBytes(used to transform bytes to easily human readable numbers)