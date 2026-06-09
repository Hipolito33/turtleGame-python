from turtle import *

speed(0)
distancia_movimento = 20

##Cor da areia no background
bgcolor("#CBBD93") 

##Desenhando retângulo da areia e do mar, adicionando cor do mar e escondendo rastro da tartaruga
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

done()