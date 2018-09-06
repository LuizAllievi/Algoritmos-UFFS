from turtle import *
speed(10000000000)
posi = [0,0]

def post(posi):
    penup()
    setpos(posi)
    pendown()


#Draw arms and legs
def draw_wings():
    left(45)
    forward(70)

    penup()
    left(180)
    forward(70)
    left(135)
    pendown()

    right(45)
    forward(70)

    penup()
    right(180)
    forward(70)
    left(45)

    left(180)


def draw_circle(size):
    for i in range(30):
        forward(size)
        right(12)



#head
draw_circle(15)


#eyes
posi[0] -= 35
posi[1] -= 35
post(posi)

#draw eye1
draw_circle(3)

posi[0] += 80
post(posi)

#draw eye2
draw_circle(3)

#nose
posi[0] = 5
posi[1] = -50
post(posi)

right(90)
forward(40)


#mouth
posi[0] -= 30
posi[1] -= 70
post(posi)

left(90)
right(15)
forward(20)
left(15)
forward(20)
left(15)
forward(20)
right(15)


#nose
posi[0] = 5
posi[1] = -143
post(posi)

right(90)
forward(100)

posi = [pos()[0], pos()[1]]


#legs
draw_wings()

#arms
posi[1] += 50
post(posi)

left(180)

draw_wings()







done()
