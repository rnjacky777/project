import turtle ,random

#class ricer(object):
def ricer():
    global color
    main = turtle.Turtle()
    main.color(color[0])
    main.shape('turtle')
    try:
        del color[0]
    except:
        pass
    main.speed(1)
    return main
        
color = ['red','green','blue','pink','orange']

line = turtle.Turtle()
line.pensize(5)
line.shape('circle')
line.speed(1000)
line.penup()
line.left(90)
line.forward(260)
line.right(90)
line.forward(250)
line.pendown()
line.backward(500)
line.color('white')


r1 = ricer()

r2 = ricer()

r3 = ricer()

r4 = ricer()

r5 = ricer()

ricer = [r1,r2,r3,r4,r5]
for i in ricer:
    i.penup()

r1.forward(100)
r2.forward(200)
r4.backward(100)
r5.backward(200)

for i in ricer:
    i.left(90)
#print(type(r2))

for i in ricer:
    i.pendown()




end = False
winner = None
while True:
    if end == True:
        break
    for i in ricer:
        i.forward(random.randint(1,10))
        if i.ycor() > 250:
            end = True
            winner,aaa = i.color()
            break
print(winner)
b = turtle.Screen()
b.exitonclick()

