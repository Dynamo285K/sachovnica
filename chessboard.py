from PIL import Image, ImageDraw

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


circle_center = (20,20)
circle_radius = square_size
circle_color = (255, 0, 0)

draw.ellipse((circle_center[0], circle_center[1],circle_center[0] + circle_radius, circle_center[1] + circle_radius),fill=circle_color)


chessboard.show()
