import main
import os
import pytube
from pytube import YouTube

def clearconsole():
    os.system("cls")
def cli_main():
    clearconsole()
    preurl = input("\nInsert a Youtube Link!\n")
    playlist = ""
    url = ""
    
    if "playlist" not in preurl:
        mediatype = "video"

    clearconsole()  
    #Graphics 'n shit makes everything fancy
    title = open("title.ascii", "r", encoding="utf-8")
    divider = open("divider.ascii", "r", encoding="utf-8")
    print(title.read())
    print(divider.read())
    print("ALPHA 0.1 | A Lot of bugs may occur | Only the Download Option is working through the terminal ;-; |")
    print("\n1 - Download\n2 - Stream\n3 - Stream")


    i = input("\nSo, what are we doing?\n")

    if i == "1":
        ic = input("Do you want to Download only the sound? | Y/N | ")
        if ic == "Y":       
            if "playlist" in preurl:
                mediatype = "playlist"
                playlist = preurl
                main.PlaylistDownload(playlist,True)
            if "video" in mediatype:
                mediatype = "video"
                url = preurl
                Filename = main.Download(url=url, AudioOnly=True)
                ic = input("\nYour music is Ready! do you want to play it now? | Y/N | ")
                if ic == "Y":
                    print("Enjoy! Press Ctrl+C to stop or wait until the end :D")
                    print(f"Playing {Filename}")
                    os.system(f"ffplay {Filename} -nodisp -loglevel quiet -autoexit")
        else:
            if "playlist" in preurl:
                main.PlaylistDownload(playlist,False)
            elif "video" in mediatype:
                url = preurl
                main.Download(url,False)
        ic = input("\nDo you want to do anything else? | Y/N | ")
        if ic == "Y":
            cli_main()
        else:
            print("\nGoodbye!")
            pass
        

if __name__ == "__main__":
    cli_main()

#Made with <3 by ZackTheKill3r using pytube(to gather info and do 99% of the stuff), ffmpeg(used for playing the streaming), youtube_dl(used for streaming) and HumanBytes(used to transform bytes to easily human readable numbers)