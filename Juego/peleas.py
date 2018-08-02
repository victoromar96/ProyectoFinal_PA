#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

pygame.init()
pygame.mixer.init()
music = pygame.mixer.Sound('canPoder.wav')
pygame.mixer.music.load('cancion.mp3')
pygame.mixer.music.play(-1,0.0)


class Personaje(Sprite):
	def __init__(self):
		self.image = personaje = pygame.image.load("goku.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(50, 300)
		self.muerto = 0

	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_SPACE]:
			self.image = personaje = pygame.image.load("gokukamehameha.png").convert_alpha()
		elif kamehameha.rect.x > 860:
			self.image = personaje = pygame.image.load("goku.png").convert_alpha()

		if teclas[K_a]:
			self.image = personaje = pygame.image.load("gokuleft.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 10
		elif teclas[K_d]:
			self.image = personaje = pygame.image.load("gokuright.png").convert_alpha()
			if self.rect.x < 740:
				self.rect.x += 10

		if teclas[K_w]:
			self.image = personaje = pygame.image.load("gokuup.png").convert_alpha()
			if self.rect.y > 32:
				self.rect.y -= 10
		elif teclas[K_s]:
			if self.rect.y < 530:
				self.image = personaje = pygame.image.load("gokudown.png").convert_alpha()
				self.rect.y += 10

class Kamehameha(Sprite):
	def __init__(self):
		self.image = kamehameha = pygame.image.load("kamehameha.gif").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(900, 700)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x > 840:
			if teclas[K_SPACE]:
				self.rect.x = (personaje.rect.x + 40)
				self.rect.y = (personaje.rect.y + 14)
				music.play()
		if self.rect.x < 870:
			self.rect.x += 20

class Barravidagoku(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("barravidagoku.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(18, 4)
	def update(self):
		if barravidagoku.rect.x <= -152:
			personaje.muerto = 1
		if disparo.rect.y >= (personaje.rect.y - 56):
			if disparo.rect.y <= (personaje.rect.y + 62):
				if disparo.rect.x >= personaje.rect.x:
					if disparo.rect.x <= (personaje.rect.x + 43):
						barravidagoku.rect.x -= 26
						disparo.rect.x = -400

class Minicell(Sprite):
	def __init__(self):
		self.image = personaje = pygame.image.load("minicell.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(670, 300)
		self.muerto = 0

	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_KP_ENTER]:
			self.image = personaje = pygame.image.load("minicell.png").convert_alpha()
		elif kamehameha.rect.x > 860:
			self.image = personaje = pygame.image.load("minicell.png").convert_alpha()

		if teclas[K_LEFT]:
			self.image = personaje = pygame.image.load("minicell.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 10
		elif teclas[K_RIGHT]:
			self.image = personaje = pygame.image.load("minicell.png").convert_alpha()
			if self.rect.x < 740:
				self.rect.x += 10

		if teclas[K_UP]:
			self.image = personaje = pygame.image.load("minicell.png").convert_alpha()
			if self.rect.y > 32:
				self.rect.y -= 10
		elif teclas[K_DOWN]:
			if self.rect.y < 530:
				self.image = personaje = pygame.image.load("minicell.png").convert_alpha()
				self.rect.y += 10


class Disparo(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("disparominicell.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(-400, -400)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x < 400:
			if teclas[K_KP_ENTER]:
				self.rect.x = (minicell.rect.x - 40)
				self.rect.y = (minicell.rect.y - 14)
				music.play()
		if self.rect.x > -400:
			self.rect.x -= 20

class Barravidaminicell(Sprite):
	def __init__(self):
		self.image = barravidaminicell = pygame.image.load("barravidaminicell.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(612, 4)
	def update(self):
		if self.rect.x >= 780:
			minicell.muerto = 1
		if kamehameha.rect.y >= (minicell.rect.y  ):
			if kamehameha.rect.y <= (minicell.rect.y + 62):
				if kamehameha.rect.x >= minicell.rect.x:
					if kamehameha.rect.x <= (minicell.rect.x + 43):
						self.rect.x += 26
						kamehameha.rect.x = 900

if __name__ == '__main__':
	# Variables.
	salir = False

	# Establezco la pantalla.
	screen = pygame.display.set_mode((800,600))

	# Establezco el título.
	pygame.display.set_caption("DRADON'S CATCH")

	# Creo dos objetos surface.
	fondo = pygame.image.load("namek.jpg").convert()
	cuadrovidagoku = pygame.image.load("cuadrovidagoku.png").convert_alpha()
	cuadrovidaminicell = pygame.image.load("cuadrovidaminicell.png").convert_alpha()
	hasperdido = pygame.image.load("Hasperdido.png").convert()
	hasganado = pygame.image.load("Hasganado.png").convert()
	# .convert() convierten la superficie a un formato de color que permite imprimirlas mucho mas rápido.
	# Objetos
	temporizador = pygame.time.Clock()
	personaje = Personaje()
	kamehameha = Kamehameha()
	minicell = Minicell()
	disparo = Disparo()
	barravidagoku = Barravidagoku()
	barravidaminicell = Barravidaminicell()

	# Movimiento del personaje.
	while not salir:
		personaje.update()
		kamehameha.update()
		if barravidaminicell.rect.x < 900:
			minicell.update()
		else:
			minicell.dificil()
		disparo.update()
		barravidagoku.update()
		barravidaminicell.update()

		# actualizacion grafica
		screen.blit(fondo, (0, 0))
		screen.blit(personaje.image, personaje.rect)
		screen.blit(kamehameha.image, kamehameha.rect)
		screen.blit(minicell.image, minicell.rect)
		screen.blit(disparo.image, disparo.rect)
		screen.blit(barravidagoku.image, barravidagoku.rect)
		screen.blit(barravidaminicell.image, barravidaminicell.rect)
		screen.blit(cuadrovidagoku, (0,0))
		screen.blit(cuadrovidaminicell, (608,0))
		if personaje.muerto == 1:
			screen.blit(hasperdido, (250,264))
		if minicell.muerto == 1:
			screen.blit(hasganado, (250,264))
		pygame.display.flip()

		if personaje.muerto == 1:
			pygame.time.delay(3000)
			salir = True
		elif minicell.muerto == 1:
			pygame.time.delay(3000)
			salir = True
		temporizador.tick(60)

		# gestion de eventos
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
