from pytube import YouTube
from moviepy.editor import *
import moviepy.editor as mp
import re, os
import utils

link = input("Digite o link do vídeo: ")
path = input("Digite o diretório pra salvar: ")
yt  = YouTube(link)

print("Baixando...")

ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download completo")

print("Convertendo arquivo")

for file in os.listdir(path):
    if re.search("mp4", file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+".mp3")
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("sucesso!")

audio = AudioFileClip(mp3_path)

start_time = input("Tempo inicial: ")
fstart_time = utils.converter(start_time)

end_time = input("Tempo final: ")
fend_time = utils.converter(end_time)

trimed_video = audio.subclip(fstart_time, fend_time)

trimed_video.write_audiofile("C:/Users/aless/OneDrive/Documentos/RaqYT/back-end/Downloads/SóOComeço.mp3")