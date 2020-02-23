from YouTube.PyTube import YouTubeHandler
from pydub import AudioSegment
from pygame import mixer as Mi
from os import remove , rename
import pafy, glob as G


Mi.init(48000)

def to_mp3(search):
    Y = YouTubeHandler(search)
    Y.get_individual_video_link()
    try: result = pafy.new(Y.link)
    except: pass
    print(result.title + " | " + Y.link,"\nDownload...")
    m4a = result.m4astreams[0]
    m4a.download()
    print("Completed!")
    name = G.glob("*.m4a")[0]
    Mp3 = AudioSegment.from_file(name, format="m4a")
    print("Converting...")
    Mp3.export("$music_temp.mp3", format="mp3" , bitrate='256')
    remove(name)
    print("Playing Music...")
    Mi.music.load("$music_temp.mp3")
    Mi.music.play()

def main():
    s = input("input: ")
    if s == "open":
        try:
            Mi.music.unload()
            remove("$music_temp.mp3")
        except: pass
        finally:
            to_mp3(input("Input Music: "))
            main()
    elif s == "close":
        Mi.music.stop()
        Mi.music.unload()
        remove("$music_temp.mp3")
        main()
    else:
        exit
