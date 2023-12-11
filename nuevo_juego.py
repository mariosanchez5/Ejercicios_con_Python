import sys, pygame

#Iniciamos pygame
pygame.init()

#Muestro una ventana
size = 800,600
screen = pygame.display.set_mode(size)

#Cambio el titulo de la ventana
pygame.display.set_caption('Juego Ball')

#Incializamos las variables
width, height = 800,600 
speed = [1,1] #Son las variables x e y como se movera el objeto
white = 255,255,255 #El cogido del color blanco

#Creamos un objeto imagen y obtengo su rectangulo
ball = pygame.image.load('ball.png')
ballrect = ball.get_rect()

#Comenzamos el bucle del juego
run = True
while run:
    #Esperamos un tiempo para que la pelota no vaya muy rapido
    pygame.time.delay(2)
    #Capturamos los eventos que se han producido
    for event in pygame.event.get():
        #Si el evento es salir de la ventana
        if event.type == pygame.QUIT: run = False

    #Muevo la pelota
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right >width:
        speed[1]=-speed[1]

    #Pinto el fondo, dibujo pelota y actualizo pantalla
    screen.fill(white)
    screen.blit(ball,ballrect)
    pygame.display.flip()

pygame.quit()
