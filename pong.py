import pygame, sys # import the pygame libraries for access
from pygame.locals import *


FPS = 200		# speed of the game 

WINDOWWIDTH = 400 # keep track of the window size
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20



# main function

def main():
	pygame.init()
	global DISPLAYSURF

	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('Pong')

	while True: # main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		FPSCLOCK.tick(FPS)



if __name__=='__main__':
	main()