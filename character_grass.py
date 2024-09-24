from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.01)
    pass

def run_top():

    for x in range(0, 800, 5):
        draw_character(x, 550)
    pass

def run_right():
    for y in range(550, 0, -5):
        draw_character(800, y)    
    pass

def run_bottom():
    for x in range(800, 0, -5):
        draw_character(x, 50)    
    pass

def run_left():
    for y in range(0, 550, 5):
        draw_character(0, y)
    pass

def run_rectangle():

    run_top()
    run_right()
    run_bottom()
    run_left()

    pass

def run_circle():

    r = 300 # 원의 반지름
    cX = 800 // 2 # 캔버스 중심점 x, y
    cY = 600 // 2

    for degree in range(0, 360, 3):

        theta = math.radians(degree)
        x = (r * math.cos(theta)) + cX
        y = (r * math.sin(theta)) + cY

        draw_character(x, y)

    pass

def run_diagonal_up():

    for x in range(0, 400, 5):
        y = x * 1.5
        draw_character(x, y)

    pass

def run_diogonal_down():
    for x in range(400, 800, 5):
        y = 1200 - (x * 1.5)
        draw_character(x, y)

    pass

def run_triangle():
    run_bottom()
    run_diagonal_up()
    run_diogonal_down()
    pass

while(True):
    #run_rectangle()
    #run_circle()
    run_triangle()
    break

close_canvas()