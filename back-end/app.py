from pytube import YouTube
from moviepy.editor import *
import moviepy.editor as mp
import re, os
import utils
from PyQt5 import uic, QtWidgets

def converter():
    link = tela_principal.lineEdit.text()
    path = tela_principal.lineEdit_4.text()
    start_time = tela_principal.lineEdit_2.text()
    end_time = tela_principal.lineEdit_3.text()

# link = input("Digite o link do vídeo: ")
# path = input("Digite o diretório pra salvar: ")
    yt  = YouTube(link)

    print("Baixando...")

    ys = yt.streams.filter(only_audio=True).first().download("Downloads")
    print("Download completo")

    print("Convertendo arquivo")

    for file in os.listdir("Downloads"):
        if re.search("mp4", file):
            mp4_path = os.path.join("Downloads", file)
            mp3_path = os.path.join("Downloads", os.path.splitext(file)[0]+".mp3")
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("sucesso!")

    audio = AudioFileClip(mp3_path)

    #start_time = input("Tempo inicial: ")
    fstart_time = utils.converter(start_time)

    #end_time = input("Tempo final: ")
    fend_time = utils.converter(end_time)

    trimed_video = audio.subclip(fstart_time, fend_time)

    trimed_video.write_audiofile(f"Downloads/{path}.mp3")
    abrirDialog()

def abrirDialog():
    tela_dialog.show()

def fecharDialog():
    tela_dialog.close()

app = QtWidgets.QApplication([])
tela_principal = uic.loadUi("view.ui")
tela_dialog = uic.loadUi("dialog.ui")
tela_principal.pushButton.clicked.connect(converter)
tela_dialog.pushButton.clicked.connect(fecharDialog)

tela_principal.show()
app.exec()