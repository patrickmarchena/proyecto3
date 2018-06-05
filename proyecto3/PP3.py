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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#E:Recibe un frame y un identificador
#S:Destruye el frame y si el identificador es "atras" se envia a otra función
#R:No tiene
def destruir(frame,identificador):
    frame.destroy()
    if identificador=="atras":
        elegir_tipos()

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
#Entrada: una ventana
#salida: la ventana destruida
#restricciones:---
def salir(ventana):
    ventana.destroy()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def elige_tipos():
    frm_tipos=Frame(ventana_principal,bd=6,width=600,height=250,relief=RIDGE,bg="#677e93")
    frm_tipos.place(x=350,y=350)
    btn_cerrar=Button(frm_tipos,image=img_cerrar,highlightthickness=0,bd=0,activebackground="#677e93",bg="#677e93",command=lambda:destruir(frm_tipos,"cerrar"))
    btn_cerrar.place(x=540,y=5)
    btn_tipo1=Button(frm_tipos,image=img_tipo1,highlightthickness=0,bd=0,activebackground="#677e93",bg="#677e93",cursor="hand2")
    btn_tipo1.place(x=110,y=40)
    btn_tipo1.bind("<Enter>",  lambda event : cambiar_color(btn_tipo1,"#445a6d"))#445a6d
    btn_tipo1.bind("<Leave>", lambda  event : cambiar_color(btn_tipo1,"#677e93"))
    btn_tipo2=Button(frm_tipos,image=img_tipo2,highlightthickness=0,bd=0,activebackground="#677e93",bg="#677e93",cursor="hand2")
    btn_tipo2.place(x=340,y=40)
    btn_tipo2.bind("<Enter>",  lambda event : cambiar_color(btn_tipo2,"#445a6d"))#445a6d
    btn_tipo2.bind("<Leave>", lambda  event : cambiar_color(btn_tipo2,"#677e93"))
    
    lbl_titulo1=Label(frm_tipos,text="Normal",bg="#677e93",font=("Times New Roman",22),fg="black")
    lbl_titulo1.place(x=130,y=180)
    lbl_titulo2=Label(frm_tipos,text="Cant. Disparos",bg="#677e93",font=("Times New Roman",22),fg="black")
    lbl_titulo2.place(x=320,y=180)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#E:Recibe un boton y un color
#S:Le cambia el color al fondo del botón
#R:No tiene
def cambiar_color(boton,color,):
    boton.config(bg=color)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
                                                             #INTERFAZ GRAFICA
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Se crea la ventana
ventana_principal=Tk()       
#Se le agregan sus atributos
ventana_principal.title("BattleShip")         
ventana_principal.geometry("1300x650+20+20")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="#445a6d")
#Todas las imagenes para trabajar la interfaz grafica
img_titulo=PhotoImage(file="inicio/logo.png")
img_mute=PhotoImage(file="imagenes_programa/mute.png")
img_play=PhotoImage(file="imagenes_programa/play.png")
img_musica=PhotoImage(file="imagenes_programa/suena.png")
img_salir=PhotoImage(file="imagenes_programa/salir.png")
img_cala=PhotoImage(file="inicio/cala.png")
img_mira=PhotoImage(file="inicio/mira.png")
img_cerrar=PhotoImage(file="imagenes_programa/cerrar.png")
img_tipo1=PhotoImage(file="imagenes_programa/barco.png")
img_tipo2=PhotoImage(file="imagenes_programa/tanque.png")
#logo de titulo y decoracion 
lbl_logo=Label(ventana_principal,image=img_titulo,bg="#445a6d")
lbl_logo.place(x=600,y=480)
lbl_cala=Label(ventana_principal,image=img_cala,bg="#445a6d")
lbl_cala.place(x=165,y=380)
lbl_cala2=Label(ventana_principal,image=img_cala,bg="#445a6d")
lbl_cala2.place(x=950,y=380)
#botones de musica, de iniciar y de salir
btn_sigue=Button(ventana_principal,image=img_musica,bg="#445a6d",cursor="hand2",bd=0,highlightthickness=0,activebackground="#445a6d",command=lambda:continuar())
btn_sigue.place(x=5,y=1)
btn_pausa=Button(ventana_principal,image=img_mute,bg="#445a6d",cursor="hand2",bd=0,highlightthickness=0,activebackground="#445a6d",command=lambda:pause())
btn_pausa.place(x=5,y=80)
btn_jugar=Button(ventana_principal,image=img_play,bg="#445a6d",cursor="hand2",bd=0,highlightthickness=0,activebackground="#445a6d",command=lambda:elige_tipos())
btn_jugar.place(x=590,y=410)
btn_salir=Button(ventana_principal,image=img_salir,bg="#445a6d",bd=0,highlightthickness=0,activebackground="#445a6d",cursor="X_cursor",command=lambda:salir(ventana_principal))
btn_salir.place(x=1230,y=1)
#play("laita.mp3")

#----------------------------------------------
animacion(lbl_logo,-20,15,480)
ventana_principal.mainloop()





#pablo playazoooooo


#hola mundo









