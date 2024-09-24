from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    print("rectangle")
    pass

def run_circle():

    r = 300 # 원의 반지름
    cX = 800 // 2 # 캔버스 중심점 x, y
    cY = 600 // 2

    for degree in range(0, 360, 3):

        theta = math.radians(degree)
        x = (r * math.cos(theta)) + cX
        y = (r * math.sin(theta)) + cY

        clear_canvas_now()
        character.draw_now(x, y)

        delay(0.01)
    pass

while(True):
    run_rectangle()
    run_circle()
    break



close_canvas()


