from pico2d import *

# os.chdir('C:\\Github\\2dgame\\Drill2')
# 파이썬 실행파일이기 때문에 자기가 있는 위치가 Working Folder(Directory)가 됨

open_canvas()
# 항상 캔버스 오픈부터

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while (x < 800):
    # Game Rendering (시물레이션 결과를 보여줌)
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    # Game Logic (상호작용을 시뮬레이션)
    x += 2
    delay(0.01)

close_canvas()
# 끝날땐 반드시 캔버스 닫기
