from tkinter import *
from PIL import Image,ImageTk
import time
import random
import pygame


#E:recibe la cancion
#S:retorna la cancion escogida 
#R:debe recibir la cancion en string
def play(cancion):#Esta funcion permite cargar una cancion poder reproducirla la libreria que se utilizo fue pygame ya que windsound no ejecutaba a la misma vez que la interfaz
    pygame.mixer.init()
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(-1)#el -1 esta ya que esto permite que la cancion no se detenga
 #-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#E:----ninguno---------
#S: pause la musica
#R:---ninguno---------
def pause():#esta funcion permite detener la cancion si el usuario ya no desea escucharla mas
    pygame.mixer.music.pause()
 #-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#E:----ninguno---------
#S: continua la musica
#R:---ninguno---------
def continuar():#esta funcion permite seguir con la cancion 
    pygame.mixer.music.unpause()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#E:recibe la imagen o label que desea realizar la animacion
#S:retorna una animacion del logo dado sumando al eje y
#R:debe recibir el nombre del label y un numero donde empezara la animacion
def animacion(label,x,y,hasta):
    while  x<hasta:
        label.place(x=x,y=y)
        x=x+10
        ventana_principal.update() #Esta función se encarga de actualizar la ventana principal para que se aprecie la animación
        time.sleep(0.010)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
                                                             #INTERFAZ GRAFICA
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Se crea la ventana
ventana_principal=Tk()       

#Se le agregan sus atributos
ventana_principal.title("Monopoly")     
ventana_principal.geometry("1000x650+150+20")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="#445a6d")
ventana_principal.attributes("-fullscreen",True)

#Todas las imagenes para trabajar la interfaz grafica
img_titulo=PhotoImage(file="inicio/logo.png")
img_mute=PhotoImage(file="imagenes_programa/mute.png")
img_play=PhotoImage(file="imagenes_programa/play.png")
img_musica=PhotoImage(file="imagenes_programa/suena.png")
#logi de tituilo
lbl_logo=Label(ventana_principal,image=img_titulo,bg="#445a6d")
lbl_logo.place(x=320,y=500)
#botones de musica
btn_sigue=Button(ventana_principal,image=img_musica,bg="#445a6d",bd=0,highlightthickness=0,activebackground="#445a6d",command=lambda:continuar())
btn_sigue.place(x=5,y=20)
btn_pausa=Button(ventana_principal,image=img_mute,bg="#445a6d",bd=0,highlightthickness=0,activebackground="#445a6d",command=lambda:pause())
btn_pausa.place(x=5,y=120)
btn_jugar=Button(ventana_principal,image=img_play,bg="#445a6d",bd=0,highlightthickness=0,activebackground="#445a6d")
btn_jugar.place(x=600,y=450)
#play("laita.mp3")

#----------------------------------------------
animacion(lbl_logo,-20,15,500)
ventana_principal.mainloop()





#pablo playazoooooo












