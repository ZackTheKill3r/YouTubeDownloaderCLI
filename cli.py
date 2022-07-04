import main
import os
import pytube
from pytube import YouTube
from settings import language

if language == "English":
    from Languages.english import *
elif language == "Portuguese":
    from Languages.portuguese import *
elif language == "Japanese":
    from Languages.japanese import *

cli_version="Alpha 0.5.0"

def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def cli_main():
    clearconsole()
    preurl = input(CLI[0])
    playlist = ""
    url = ""
    
    playlist_ids = ['playlist', 'list']
    if any([x in preurl for x in playlist_ids]):
        mediatype = "playlist"
    else:
        mediatype = "video"

    clearconsole() 
    #Graphics 'n shit makes everything fancy
    title = open("title.ascii", "r", encoding="utf-8")
    divider = open("divider.ascii", "r", encoding="utf-8")
    print(title.read())
    print(divider.read())
    version_header = CLI[1].replace("/cli_version",f"{cli_version}")
    version_header = version_header.replace("/core_version",f"{main.core_version}")
    print(version_header)
    if mediatype == "video":
        print(CLI[2])
    else:
        print(CLI[3])


    i = input(CLI[4])

    if i == "1":
        ic = input(CLI[5])
        if ic == "Y":       
            if "playlist" in preurl:
                mediatype = "playlist"
                playlist = preurl
                main.PlaylistDownload(playlist,True)
            if "video" in mediatype:
                mediatype = "video"
                url = preurl
                Filename = main.AutoDownload(url=url, AudioOnly=True)
                ic = input(CLI[6])
                if ic == "Y":
                    print(CLI[7])
                    playing = CLI[8].replace("/p",f"{Filename}")
                    print(CLI[8])
                    os.system(f"start ffplay {Filename} -nodisp -loglevel quiet -autoexit")
        else:
            if "playlist" in preurl:
                main.PlaylistDownload(playlist,False)
            elif "video" in mediatype:
                url = preurl
                ic = input(CLI[9])
                if ic == "Y":
                    Filename = main.Download(url=url, AudioOnly=False)
                else:
                    Filename = main.AutoDownload(url=url, AudioOnly=False)
        ic = input(CLI[10])
        if ic == "Y":
            cli_main()
        else:
            print(CLI[11])
            pass
        
    if i == "2":
        if "playlist" in preurl:
            print(CLI[12])
            cli_main()
        else:
            url = preurl
            ic = input(CLI[13])
            if ic == "Y":
                main.Stream(url,True)
            else:
                main.Stream(url,False)


if __name__ == "__main__":
    cli_main()

#Made with <3 by ZackTheKill3r using pytube(to gather info and do 99% of the stuff), ffmpeg(used for playing the streaming), youtube_dl(used for streaming) and HumanBytes(used to transform bytes to easily human readable numbers)
