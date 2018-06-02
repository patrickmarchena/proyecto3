from tkinter import *
from PIL import Image,ImageTk
import time
import random
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
#btn_sigue=Button(ventana_principal)
#btn_pausa=Button(ventana_principal)

#----------------------------------------------
animacion(lbl_logo,-20,15,500)
ventana_principal.mainloop()


















