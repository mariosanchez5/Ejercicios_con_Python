import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0

#1.Configuracion de la ventana
wn = turtle.Screen() #Creamos la ventana
wn.title('Juego de la Serpiente') #Titulo de la ventana
wn.bgcolor('black') #Color de la ventana
wn.setup(width=600, height=600) #Dimensiones de la ventana
wn.tracer(0) #Hace las animaciones mas placenteras a nuestros ojos

#2.Cabeza de la serpiente
cabeza = turtle.Turtle() #Creamos la cabeza de la serpiente
cabeza.speed(0) #Cuando yo incicie la pantalla la cabeza ya este ahi
cabeza.shape('square') #La forma de la cabeza
cabeza.color('white') #Le damos color a la cabeza de la serpiente
cabeza.penup() #Cuando movamos el objeto no deje rastro
cabeza.goto(0,0) #Le damos las cordenadas donde comenzará la serpiente
cabeza.direction = 'stop' #Cuando aparezca la cabeza el programa espere y no se mueva a ningun lado

#6.Comida
comida = turtle.Turtle() 
comida.speed(0)
comida.shape('circle') 
comida.color('red') 
comida.penup() 
comida.goto(0,100) 

#7. Cuerpo de la serpiente
segmentos=[]

#Texto
texto = turtle.Turtle()
texto.speed(0)#Cuando abra la pantalla ya esté el texto
texto.color('white')
texto.penup()
texto.hideturtle()#Que esconda la pluma
texto.goto(0,260)
texto.write('Score: 0     High Score: 0', align='center', font=('Courier',24,'normal'))

#4.Ahora definiremos las funciones para conectar el teclado con el moviemiento de la serpiente
def arriba():
    cabeza.direction='up'
def abajo():
    cabeza.direction='down'
def izquierda():
    cabeza.direction='left'
def derecha():
    cabeza.direction='right'



#3.Ahora haremos que la serpiente se mueva y para esto debemos crear distintas funciones
def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor() #Con este comando le estamos diciendo que me de la coordenada y donde esta la serpiente
        cabeza.sety(y+20) #Aca le estamos diciendo que de donde esta se mueva 20 pixeles hacia arriba
    
    if cabeza.direction == 'down':
        y = cabeza.ycor() 
        cabeza.sety(y-20)

    if cabeza.direction == 'left':
        x = cabeza.xcor() 
        cabeza.setx(x-20)

    if cabeza.direction == 'right':
        x = cabeza.xcor() 
        cabeza.setx(x+20)

#5.Teclado
wn.listen()#Le digo a mi pantalla que este atenta a los movimientos del teclado
wn.onkeypress(arriba, 'Up') #Debe ir la u en mayuscula para indicar que es la flecha de mi teclado
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')

#Bucle infinito para que no se salga del juego hasta que se termine
while True:
    wn.update()

    #Colisiones Borde
    if cabeza.xcor() > 280 or cabeza.xcor() <-290 or cabeza.ycor() >290 or cabeza.ycor() <-290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction= ('stop')
        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
        #Limpiar lista de segmentos
        segmentos.clear()

        #Resetear marcador
        score = 0
        texto.clear()
        texto.write('Score: {}     High Score: {}'.format(score,high_score), align='center', font=('Courier',24,'normal'))

    if cabeza.distance(comida)<20: #Si la distancia entre cabeza y comida es menor a 20 que se cambie de lado, es 20 porque el cuadrado y la comida son de 20 pixeles
        x = random.randint(-280,280) #Cualquier posicion dentro de esas coordenandas
        y = random.randint(-280,280)
        comida.goto(x,y) #Para actualizar la posicion

        #Se crea un nuevo segmento cada vez que toco la comida
        nuevo_segmento = turtle.Turtle() 
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square') 
        nuevo_segmento.color('grey') 
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento) 

        #Aumentar marcador
        score = score + 10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write('Score: {}     High Score: {}'.format(score,high_score), align='center', font=('Courier',24,'normal'))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg-1,0,-1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg >0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)


    mov()

    #Colisiones cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = 'stop'

            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            
            #Limpiar los elementos de la lista
            segmentos.clear()

            #resetear marcador
            score=0
            texto.clear()
            texto.write('Score: {}     High Score: {}'.format(score,high_score), align='center', font=('Courier',24,'normal'))


    time.sleep(posponer)