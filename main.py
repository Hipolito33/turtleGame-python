from turtle import *

speed(0)
distancia_movimento = 20

##Cor da areia no background.
bgcolor("#CBBD93") 

##Desenhando retângulo da areia e do mar, adicionando cor do mar e escondendo rastro da tartaruga.
penup()
goto(100,200)
pendown()
color("blue")
begin_fill()
goto(300,200)
goto(300,-200)
goto(100,-200)
goto(100,200)
end_fill()

##Cria a tartaruga e move ela ao centro do cenário.
penup()
goto(-160, 0)
shape("turtle")
color("green")

##Cria movimentação da tartaruga
def mover_cima():
    setheading(90)
    forward(distancia_movimento)
    confirma_fim()

def mover_baixo():
    setheading(270)
    forward(distancia_movimento)
    confirma_fim()

def mover_esquerda():
    setheading(0)
    forward(distancia_movimento)
    confirma_fim()

def mover_direita():
    setheading(180)
    forward(distancia_movimento)
    confirma_fim()

##Confirma se a tartaruga chegou ao mar(fim do jogo).
##Esconde a tartaruga -> pinta a tela de branco -> escreve que você venceu.
def confirma_fim():
    if xcor() > 100:
        hideturtle()
        color("white")
        write("VOCÊ VENCEU!")

        ##Desativa os controles ao vencer o game.
        Screen().onkey(None,"Up")
        Screen().onkey(None,"Down")
        Screen().onkey(None,"Right")
        Screen().onkey(None,"Left")

Screen().onkey(mover_cima,"Up")
Screen().onkey(mover_baixo,"Down")
Screen().onkey(mover_esquerda,"Right")
Screen().onkey(mover_direita,"Left")

Screen().listen()
done()