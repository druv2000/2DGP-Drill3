from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

while(True):
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x = x + 5

        delay(0.01)

    while(y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        y = y + 5

        delay(0.01)

    while(x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x = x - 5

        delay(0.01)

    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        y = y - 5  

        delay(0.01)

    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x = x + 5

        delay(0.01)

    i = 0
    while(i < 720):
        #print(math.sin(i / 360 * math.pi))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x = x + math.cos(i / 360 * math.pi) * 2
        y = y + math.sin(i / 360 * math.pi) * 2
        i = i + 1

        delay(0.01)

close_canvas()


