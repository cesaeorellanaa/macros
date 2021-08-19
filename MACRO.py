#! python3
import pywintypes
import pyautogui as pg, sys, PIL.ImageGrab, win32gui
from time import sleep
import keyboard

# Este programa se realiza netamente para dar eficacia al metodo de capturar padrones electorales
# Dejando en claro que no se realiza ningun registro de los mismos en el

#Grabar Padron
xGrabar = 727
yGrabar = 100

#Aceptar cambios
xAceptar = 717
yAceptar = 300


#Eliminar padron
xFail = 200
yFAil = 500


#Click para Grabar y Aceptar
def clickGrabarAceptar():
	pg.moveTo(xGrabar, yGrabar, 1)
	pg.click()


#Click Para aceptar
def clickAceptar():
	pg.moveTo(xAceptar, yAceptar, 1)
	pg.click()

#Click Para Eliminar
def clickFail():
	pg.moveTo(xFail, yFAil, 1)
	pg.click()


#Contador de padrones
numero = 1
def contador():
    global suma_a
    suma_a=numero+1

#Contador de errores
numero2 = 0
def contador2():
    global suma_a2
    suma_a2=numero2+1

try:
	while True:
		sleep(1)
		print("Hola, Bienvenido al programa :D")
		numero = int(input("Cuantos padrones hiciste la ultima vez?"))

		while True:
			if keyboard.is_pressed("q"):
				contador()
				numero = suma_a
				print("Comenzaremos un nuevo padrón. En total con este serán", numero)
				clickGrabarAceptar()

			if keyboard.is_pressed("a"):
				contador2()
				numero2 = suma_a2
				print("Te haz equivocado D: ten cuidado a la proxima! te haz equivocado un total de;)", numero2)
				clickFail()
    #

except KeyboardInterrupt:
	print('\n')
keyboard.on_press_key