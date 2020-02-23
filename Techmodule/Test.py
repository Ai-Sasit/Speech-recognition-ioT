import glob,os
G=glob.glob('*.m4a')[0]
os.system(f"ffmpeg -i {G} -map 0:a:0 -b:a 96k {G[:-4]}.mp3")