import pygame
pygame.init()
x = 640
y = 480
xS = 5
yS = 3
screen = pygame.display.set_mode([640,480])

screenState = []
def init(screenState):
	for i in range(xS):
		screenState.append([])
		for j in range(yS): 
			screenState[i].append([1,1,1])
def drawPic(screen):
	for i in range(xS):
		for j in range(yS):
			pygame.draw.rect(screen,[screenState[i][j][0]%255,screenState[i][j][1]%255,screenState[i][j][2]%255],[int(x/xS)*i,int(y/yS)*j,int(x/xS),int(y/yS)])
	pygame.display.flip()

init(screenState)
while True:
	for event in pygame.event.get(): # User did somethin
		if event.type == pygame.KEYDOWN:
			print event.unicode
			screenState[event.key%xS][event.key%yS][0] = (screenState[event.key%xS][event.key%yS][0] + 63)%255
			screenState[event.key%xS][event.key%yS][1] = (screenState[event.key%xS][event.key%yS][1] + 10)%255
			screenState[event.key%xS][event.key%yS][2] = (screenState[event.key%xS][event.key%yS][2] + 23)%255
			drawPic(screen)	
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
