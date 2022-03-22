import turtle

turtle.setup(width=500, height=500)    # 창크기 조정 ( 넓이, 높이 )
turtle.shape("turtle")  # 커서 모양 ( 거북이 )
turtle.speed(0) # 그리는 속도 ( 0으로 설정시 바로 완성됨 )
turtle.pensize(20)  #선 사이즈, 굵기
# turtle.pencolor("blue") #선 색상
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.bgcolor() 백그라운드 컬러

# for i in range(1,5):
#     turtle.circle(100)
#     turtle.forward(20)
turtle.pencolor("black")
turtle.circle(100)      # 선 색상을 검정색으로 잡고 circle()로 반지름이 ( 100 )인 원을 그림

turtle.up()     # up으로 이동할때 선이 안그려짐
turtle.forward(240) # 보고있는 방향에서 앞으로 ( 240 )만큼 전진
turtle.down()   # down으로 다시 선이 그려지게 함
turtle.pencolor("Red")
turtle.circle(100)  # 색상을 빨간색으로 하고 원을 그림

turtle.up()   # 마찬가지로 위와 동일하게 이동을 위해 up을 설정함
turtle.backward(220)    # 뒤로 ( 220 )만큼 이동
turtle.right(90)    # 원활하게 원을 그리기 위해 오른쪽으로 방향을 ( 90 )도 꺾음
turtle.down()   # up 설정을 down으로 품
turtle.pencolor("green")
turtle.circle(100)  # 색상을 초록색으로 바꾸고 원을 그려줌

# 나머지 과정은 위와 동일함
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