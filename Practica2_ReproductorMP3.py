from tkinter import *
import pygame, sys
from pygame.locals import*
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image

raiz = Tk()

pygame.init() # Iniciamos modulo de pygame

#Funcion Boton Abrir Cancion
def abrirArchivo():
    cancion= filedialog.askopenfile() #guardar el nomnbre de la cancion que vamos a reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)

def PlaySong():
  pygame.mixer.music.play()
def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()


def resumeSong():
    pygame.mixer.music.unpause()

def volumenUp():
    volumenLevel=pygame.mixer.music.get_volume() + 0.5
    print(volumenLevel)
    pygame.mixer.music.set_volume(volumenLevel)

def volumenDown():
    volumenLevel=pygame.mixer.music.get_volume() - 0.5
    print(volumenLevel)
    pygame.mixer.music.set_volume(volumenLevel)

raiz.title("Reproductor MP3 = GUI")


raiz.geometry("600x600")
raiz.resizable(0,0)


#Crear Frame

framePricipal=Frame(raiz,bg="#FFFACD")
framePricipal.pack(fill="both", expand=1)#permite visualizar el archivo



#Titulo Reproductor
tituloReproductor = Label(framePricipal,text="Reproductor MP3 - Umbear labs",font=("Comic Sans Ms",20,"bold"),bg="#FFFACD",fg="#000000")
tituloReproductor.pack()

imagTom= Image.open('C:\\Users\\Junio\\OneDrive\\Escritorio\\PROGRAMAS DE PYTHON\\INTERFAZ_GRAFICA\\tom.jpg')
#Variable que contiene el nombre de la imagen
imagenMusica = imagTom.resize((200,200))
imagTom = ImageTk.PhotoImage(imagenMusica)
miTitulo = Label(raiz,image=imagTom)
miTitulo.place(relx=0.35,rely=0.1)


#Boton Open Song
botonAbrirOpenSong=Button(framePricipal,text="Open Song", bg="#000000",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=12,height=1,command=abrirArchivo)
botonAbrirOpenSong.place(relx=0.2,rely=0.5)


botonAbrirPlaySong=Button(framePricipal,text="Play song", bg="#800080",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=12,height=1,command=PlaySong)
botonAbrirPlaySong.place(relx=0.2,rely=0.6)

botonAbrirStopSong=Button(framePricipal,text="Stop Song", bg="#FF0000",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=12,height=1,command=stopSong)
botonAbrirStopSong.place(relx=0.55,rely=0.5)

botonAbrirResumeSong=Button(framePricipal,text="Resume song", bg="#008000",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=12,height=1,command=resumeSong)
botonAbrirResumeSong.place(relx=0.55,rely=0.6)

botonAbrirResumePause=Button(framePricipal,text="Pause", bg="#008000",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=12,height=1,command=pauseSong)
botonAbrirResumePause.place(relx=0.35,rely=0.75)

Volumen_mas=Button(framePricipal,text="Volumen mas", bg="#008000",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=12,height=1,command=volumenUp)
Volumen_mas.place(relx=0.10,rely=0.90)


Volumen_menos=Button(framePricipal,text="Volumen menos", bg="#008000",fg="#FFFACD",font=("Comic Sans Ms",15,"bold"),width=12,height=1,command=volumenDown)
Volumen_menos.place(relx=0.60,rely=0.90)





raiz.mainloop()