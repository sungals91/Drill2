from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x, y = 130, 90

while True:

    while x < 600:
    
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.01)

    while y < 400:

        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y += 2
        delay(0.01)

    while y >= 90:

        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= math.sqrt(2)
        y -= math.sqrt(2)
        delay(0.01)


close_canvas()
