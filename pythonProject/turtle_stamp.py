import turtle

import random


# 왼쪽 마우스버튼 클릭하여 도장찍기 함수

def screenLeftClick(x, y):
    global r, g, b      # 전역변수(global) r, g, b 선언

    r = random.random()     # 변수 r,g,b 난수로 지정

    g = random.random()

    b = random.random()

    # 크기는 1부터 5까지

    tSize = random.randrange(1, 6)

    # 각도는 0부터 360도 까지

    tAngle = random.randrange(0, 361)

    # 크기, 색상, 각도

    turtle.shapesize(tSize) # 거북이의 크기를 tSize ( 1부터 5까지  ) 랜덤으로 크기 조정

    turtle.color(r, g, b)   # 거북이 색상도 난수 r,g,b로 무작위로 뽑히게 함

    turtle.right(tAngle)    # 거북이 각도를 오른쪽방향으로 ( 0 에서 360도까지 ) 무작위로 돌게함

    # 거북이 도장찍기

    turtle.stamp()  # 도장을 찍게 하는 메소드


# 거북이 이동 함수

def screenRightClick(x, y):     # 우클릭 함수
    turtle.penup()  #선이 보이지 않게 함

    turtle.goto(x, y)   # x,y 좌표로 이동시킴


# 변수 초기값

r, g, b = 0.0, 0.0, 0.0

# 메인 부분

turtle.title("Turtle_stamp")

turtle.shape("turtle")  # 커서 모양을 거북이로 지정

#onscreenclick 이벤트함수 사용법 (함수, 1 - 마우스 왼쪽클릭, 2 - 마우스 가운데클릭, 3 - 마우스 오른쪽클릭)
turtle.onscreenclick(screenLeftClick, 1)    #클릭 이벤트로 왼쪽 클릭 이벤트처리

turtle.onscreenclick(screenRightClick, 3)   #클릭 이벤트로 오른쪽 클릭 이벤트처리

turtle.done()