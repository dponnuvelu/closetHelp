
import pygame
import webbrowser

pygame.init()
pygame.font.init()
import sys
#Display Set-Up
(width, height) = (412, 600)
screen = pygame.display.set_mode((width, height))
display = pygame.display.set_caption('ClosetHelp')
background_colour = (0, 0, 0)

pygame.display.flip()
running = True
openClicked = False
otherPage = False
title = pygame.image.load("title.png")
title = pygame.transform.scale(title, (240, 135))

open = pygame.image.load(("Open.png"))
open = pygame.transform.scale(open, (120, 67))

clicked = 0



clickCount = 0

accessed = False

def title_display (x,y):
	screen.blit(title, (x,y))

title_x = 75
title_y = 25

def open_display (x,y):
	screen.blit(open, (x,y))

open_x = 140
open_y = 290

def identity ():
	info = pygame.draw.rect(screen, (217, 70, 56), (115, 150, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('Info', True, (0,0,0), (217, 70, 56))
	screen.blit(text, [140, 170])

	chat =pygame.draw.rect(screen, (217, 137, 56), (215, 150, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('Chat', True, (0, 0, 0), (217, 137, 56))
	screen.blit(text, [235, 170])

	counselor = pygame.draw.rect(screen, (217, 190, 56), (115, 225, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('Counselor', True, (0, 0, 0), (217, 190, 56))
	screen.blit(text, [120, 245])

	news = pygame.draw.rect(screen, (80, 181, 54), (215, 225, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('News', True, (0, 0, 0), (80, 181, 54))
	screen.blit(text, [235, 245])

	genaffcare = pygame.draw.rect(screen, (54, 65, 181), (115, 300, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('Aff. Care', True, (0, 0, 0), (54, 65, 181))
	screen.blit(text, [125, 320])

	comingout = pygame.draw.rect(screen, (107, 54, 181), (215, 300, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 12)
	text = font.render('Coming Out', True, (0, 0, 0), (107, 54, 181))
	screen.blit(text, [217, 320])

	qtbipoc = pygame.draw.rect(screen, (212, 201, 184), (115, 375, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('QTBIPOC', True, (0, 0, 0), (212, 201, 184))
	screen.blit(text, [125, 395])

	pronouns = pygame.draw.rect(screen, (79, 79, 79), (215, 375, 75, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('Pronouns', True, (0, 0, 0), (79, 79, 79))
	screen.blit(text, [220, 395])

	escape = pygame.draw.rect(screen, (255, 0, 0), (115, 450, 175, 50))
	font = pygame.font.Font('freesansbold.ttf', 13)
	text = font.render('Easy Escape', True, (0, 0, 0), (255, 0, 0))
	screen.blit(text, [165, 470])

	pygame.display.update()
	return info, chat, counselor, news, genaffcare, comingout, qtbipoc, pronouns, escape

def identityClick(identity, otherPage):
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = event.pos

			if identity[0].collidepoint(pos):
				webbrowser.open(r"https://www.thetrevorproject.org/resources/")
			if identity[1].collidepoint(pos):
				webbrowser.open(r"https://www.trevorspace.org")
			if identity[2].collidepoint(pos):
				webbrowser.open(r"https://www.thetrevorproject.org/get-help/")
			if identity[3].collidepoint(pos):
				webbrowser.open(r"https://www.them.us")
			if identity[4].collidepoint(pos):
				webbrowser.open(r"https://www.healthline.com/health/what-is-gender-affirming-care#types")
			if identity[5].collidepoint(pos):
				webbrowser.open(r"https://www.thetrevorproject.org/resources/guide/the-coming-out-handbook/")
			if identity[6].collidepoint(pos):
				webbrowser.open(r"https://www.hrc.org/resources/communities-of-color")
			if identity[7].collidepoint(pos):
				webbrowser.open(r"https://pronouns.org")
			if identity[8].collidepoint(pos):
				quit()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN and otherPage == False:
			clicked = clicked + 1
			pygame.draw.rect(screen, (0, 0, 0), (150, 300, 100, 50))
			pygame.display.update()
			if clicked > 3:
				openClicked = True
			while openClicked == True:
				identityClick(identity(), otherPage)


	if openClicked == False:
		screen.fill(background_colour)
		pygame.draw.rect(screen, (0, 0, 255), (150, 300, 100, 50))
		title_display(title_x,title_y)
		open_display(open_x, open_y)
		pygame.display.update()


