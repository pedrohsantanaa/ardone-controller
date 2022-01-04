# -*- coding: UTF-8 -*-
import termios
import fcntl
from os import system
import os
import sys
import libardrone
from time import sleep

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def menu():
	print "\n				USE ESSES COMANDOS\n"
	print "\033[31m"+"	1-->SUBIR		2-->ESTABILIZAR		3-->DESCER"+"\033[0;0m"	
	print "\n"
	print "	\033[32m"+"			W-->FRENTE"+"\033[0;0m"
	print "	\033[32m"+"A-->L.ESQUERDO					D-->L.DIREITO""\033[0;0m"
	print "	\033[32m"+"			S-->ATRÁS""\033[0;0m"
	print "\n"
	print "	\033[34m"+"ENTER-->DECOLAR					X-->FECHAR""\033[0;0m"
	print "\n"
	print "	\033[34m"+"			ESPAÇO-->ATERISSAR""\033[0;0m"
	print "\nComando:"


fd = sys.stdin.fileno()
oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)
oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
drone = libardrone.ARDrone()
menu()

try:
	while True:
		try:
			entrada = sys.stdin.read(1)
			entrada = entrada.lower()
			flush_input()
			if entrada == 'x':
				break
			
			if entrada == 'a':
				drone.move_left()
				sleep(1)
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()

			if entrada == 'd':
				drone.move_right()
				sleep(1)
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()				
			
			if entrada == 'w':
				drone.move_forward()
				sleep(1)
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()				
			
			if entrada == 's':
				drone.move_backward()
				sleep(1)
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()				
			
			if entrada == ' ':
				drone.land()
				sleep(1)
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()				
			
			if entrada == '\n':
				drone.takeoff()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()				
			
			if entrada == '1':
				drone.move_up()
				sleep(1)
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()				
			
			if entrada == '2':
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()				
			
			if entrada == '3':
				drone.move_down()
				sleep(1)
				drone.hover()
				system("clear")
				print "Tecla Pressionada",entrada
				menu()
		
		except IOError:
			pass
finally:
	termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
	drone.halt()
