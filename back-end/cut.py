from moviepy.editor import *
import utils

video = VideoFileClip("C:/Users/aless/OneDrive/Documentos/RaqYT/back-end/VocalLivre.mp4")
start_time = input("Tempo inicial: ")
fstart_time = utils.converter(start_time)

end_time = input("Tempo final: ")
fend_time = utils.converter(end_time)


trimed_video = video.subclip(fstart_time, fend_time)

trimed_video.write_videofile("C:/Users/aless/OneDrive/Documentos/RaqYT/back-end/VocalLivreCortado.mp4", codec="libx264" )