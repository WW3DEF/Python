import turtle

turtle.setup(width=500, height=500)    # 창크기 조정
turtle.shape("turtle")
turtle.speed(0)
turtle.pensize(20)  #선 사이즈
# turtle.pencolor("blue") #선 색상
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.bgcolor() 백그라운드 컬러

# for i in range(1,5):
#     turtle.circle(100)
#     turtle.forward(20)
turtle.pencolor("black")
turtle.circle(100)

turtle.up()
turtle.forward(240)
turtle.down()
turtle.pencolor("Red")
turtle.circle(100)

turtle.up()
turtle.backward(220)
turtle.right(90)
turtle.down()
turtle.pencolor("green")
turtle.circle(100)

turtle.up()
turtle.right(90)
turtle.forward(270)
turtle.left(180)
turtle.down()
turtle.pencolor("blue")
turtle.circle(100)

turtle.up()
turtle.forward(20)
turtle.right(90)
turtle.down()
turtle.pencolor("yellow")
turtle.circle(100)

turtle.done()