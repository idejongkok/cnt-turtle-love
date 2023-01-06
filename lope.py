import turtle
from time import sleep
pen = turtle.Turtle()

def kurva():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
  
def lopelope():
    pen.fillcolor('red')
    pen.begin_fill()
    
    pen.left(140)
    pen.forward(113)

    kurva()
    pen.left(120)
  
    kurva()
    pen.forward(112)
  
    pen.end_fill()


lopelope()
sleep(10)


pen.ht()
