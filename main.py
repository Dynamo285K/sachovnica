import math
from PIL import Image, ImageDraw
import sys

sachovnica= []
for i in range(8):
    riadok = []
    for j in range(8):
        riadok.append(0)
    sachovnica.append(riadok)

def check(x:int,y:int) -> bool:
    for j in range(8):
        for i in range(8):
            if i == x or j == y or i + j == x + y or i - j == x - y:
                if sachovnica[j][i] == 1:
                    return False
    # draw.ellipse((x*square_size, y*square_size,  x*square_size +square_size, y*square_size+ square_size),fill=(0, 128, 0))
    return True

image_counter = 0

pocet = 0
def drticka(dama:int):
    global sachovnica, pocet, image_counter
    if dama == 8 :
        print(sachovnica)
        pocet += 1
        for i in range(8):
            for g in sachovnica:
                for r in g:
                    if r == 1:
                        r1 = g.index(r)
                        g1 = sachovnica.index(g)
                        draw.ellipse((r1*square_size, g1*square_size,  r1*square_size +square_size, g1*square_size+ square_size),fill=(0, 128, 0))
        image_counter += 1
        image_name = f'chessboard_{image_counter}.png'
        chessboard.save(image_name)
        chessboard.show()
        for i in range(8):
            for j in range(8):
                x0 = i * square_size
                y0 = j * square_size
                x1 = x0 + square_size
                y1 = y0 + square_size
                color = dark_color if (i + j) % 2 == 0 else light_color
                draw.rectangle([x0, y0, x1, y1], fill=color)
    for i in range(8):
        if check(i,dama):
            # draw.ellipse((i*square_size, dama*square_size,  i*square_size +square_size, dama*square_size+ square_size),fill=(0, 128, 0))
            sachovnica[dama][i] = 1
            drticka(dama+1)
            sachovnica[dama][i] = 0




board_size = 160
square_size = board_size // 8

chessboard = Image.new('RGB', (board_size, board_size), 'white')
draw = ImageDraw.Draw(chessboard)

dark_color = (0, 0, 0)
light_color = (255, 255, 255)



for i in range(8):
    for j in range(8):
        x0 = i * square_size
        y0 = j * square_size
        x1 = x0 + square_size
        y1 = y0 + square_size
        color = dark_color if (i + j) % 2 == 0 else light_color
        draw.rectangle([x0, y0, x1, y1], fill=color)

drticka(0)


# def create_and_save_image_with_drawings():
#     board_size = 160
#     square_size = board_size // 8
#
#     chessboard = Image.new('RGB', (board_size, board_size), 'white')
#     draw = ImageDraw.Draw(chessboard)
#
#     dark_color = (0, 0, 0)
#     light_color = (255, 255, 255)
#
#
#
#     for i in range(8):
#         for j in range(8):
#             x0 = i * square_size
#             y0 = j * square_size
#             x1 = x0 + square_size
#             y1 = y0 + square_size
#             color = dark_color if (i + j) % 2 == 0 else light_color
#             draw.rectangle([x0, y0, x1, y1], fill=color)





