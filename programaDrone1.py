# Autor Pedro Henrique Santana Amaral
# Gredes

import libardrone,sys
from time import sleep
from os import system

drone = libardrone.ARDrone()

while True:
	print "******************************************************"
	print ""
	print "	Pressione T para o Drone Decolar"
	print "	Pressione H para o Drone Estabilizar"
	print "	Pressione U para o Drone Subir"
	print "	Pressione D para o Drone Abaixar"
	print "	Pressione L para o Drone Mover para a Esquerda "
	print "	Pressione R para o Drone Mover para a Direita "
	print " Pressione F para o Drone ir Para Frente "
	print " Pressione B para o Drone ir Para Atras"
	print "	Pressione P para o Drone Aterrizar"
	print "	Pressione X para Fechar o Programa"
	print ""
	print "******************************************************"

	entrada = raw_input("\n Comando:")
	if entrada == 'X' or entrada == 'x':	
		break
	
#	a = input("\n Segundos:")
	a=0
	
	if entrada == 'T' or entrada == 't':
			print "\n Aguarde %d Segundos" %a
			drone.takeoff()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")
		
	elif entrada == 'H' or entrada=='h':
			print "\n Aguarde %d Segundos" %a
			drone.hover()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")
			
	elif entrada == 'U' or entrada == 'u':
			print "\n Aguarde %d Segundos" %a
			drone.move_up()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")
			
	elif entrada == 'D' or entrada == 'd':
			print "\n Aguarde %d Segundos" %a
			drone.move_down()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")
			
	elif entrada == 'L' or entrada == 'l':
			print "\n Aguarde %d Segundos" %a
			drone.move_left()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")
			
 	elif entrada == 'R' or entrada == 'r':
			print "\n Aguarde %d Segundos" %a
			drone.move_right()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")

	elif entrada == 'F' or entrada == 'f':
			print "\n Aguarde %d Segundos" %a
			drone.move_forward()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")

	elif entrada == 'B' or entrada == 'b':
			print "\n Aguarde %d Segundos" %a
			drone.move_backward()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			drone.hover()
			system("clear")


	elif entrada == 'P' or entrada == 'p':
			print "\n Aguarde %d Segundos" %a
			drone.land()
			print "\n Comando enviado com Sucesso"
			sleep(a)
			system("clear")
			
				
print " Fechando o Programa"
drone.halt()
