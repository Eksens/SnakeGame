import sys
import pygame
import random
import pygame_menu
import tkinter as tk
from tkinter import *
pygame.init()

BLOCK_SIZE = 20
FRAME_COLOR = [72, 217, 137]
RECT_COLOR = [0, 0, 0]
BLOCK_COUNT = 30
PADDING = 30
HEADER_MARGIN = 110
HEADER_COLOR = [47, 168, 101]
SNAKE_COLOR = [61, 45, 181]
APPLE_COLOR = [217, 48, 87]
SIZE_VALUE = 2
speed = 3

def set_window_size(size_option):
    global screen, BLOCK_COUNT, PADDING, HEADER_MARGIN, size
    if size_option == 1:
        BLOCK_COUNT = 20
    elif size_option == 2:
        BLOCK_COUNT = 30
    elif size_option == 3:
        BLOCK_COUNT = 40
        BLOCK_COUNT = 40
    size = [BLOCK_COUNT*20+PADDING*2, BLOCK_COUNT*20+PADDING*2+HEADER_MARGIN]


def set_size(value, size):
    global BLOCK_COUNT, SIZE_VALUE
    if size == 1:
        BLOCK_COUNT = 20
    elif size == 2:
        BLOCK_COUNT = 30
    elif size == 3:
        BLOCK_COUNT = 40
    SIZE_VALUE = size
    set_window_size(SIZE_VALUE)


def set_speed(valer, speed_set):
    global speed
    if speed_set == 1:
        speed = 5
    elif speed_set == 2:
        speed = 8
    elif speed_set == 3:
        speed = 12
    SPEED_VALUE = speed


set_window_size(SIZE_VALUE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake Game')
timer = pygame.time.Clock()
Score = pygame.font.SysFont('Impact', 36)
NICKNAME = 'Player 2'


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inside(self):
        return 0<=self.x<BLOCK_COUNT and 0<=self.y<BLOCK_COUNT

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def draw_rect(color, row, column):
    pygame.draw.rect(screen, color,
                     [PADDING + BLOCK_SIZE * column, HEADER_MARGIN + PADDING + BLOCK_SIZE * row, BLOCK_SIZE,
                      BLOCK_SIZE])


def start_the_game():
    screen = pygame.display.set_mode(size)


    def get_random_empty_block():
        x = random.randint(0, BLOCK_COUNT - 1)
        y = random.randint(0, BLOCK_COUNT - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, BLOCK_COUNT - 1)
            empty_block.y = random.randint(0, BLOCK_COUNT - 1)
        return empty_block
    snake_blocks = [SnakeBlock(10, 9), SnakeBlock(10, 10), SnakeBlock(10, 11)]
    apple = get_random_empty_block()

    total = 0
    d_row = 0
    d_col = 1


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1
        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, 1000, HEADER_MARGIN])

        text_total = Score.render(f"Total: {total}", 0, APPLE_COLOR)
        screen.blit(text_total, (BLOCK_SIZE, BLOCK_SIZE))

        for row in range(BLOCK_COUNT):
            for column in range(BLOCK_COUNT):
                if (row + column) % 2 == 0:
                    RECT_COLOR = [180, 237, 183]
                else:
                    RECT_COLOR = [162, 224, 164]
                draw_rect(RECT_COLOR, row, column)

        head = snake_blocks[-1]
        if not head.inside():
            with open("leaderboard.txt", "a") as leaderboard:
                leaderboard.write('\n'+NICKNAME+': '+str(total))
            break

        draw_rect(APPLE_COLOR, apple.x, apple.y)
        for block in snake_blocks:
            draw_rect(SNAKE_COLOR, block.x, block.y)

        if apple == head:
            total += 1
            snake_blocks.append(apple)
            apple = get_random_empty_block()

        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            with open("leaderboard.txt", "a") as leaderboard:
                leaderboard.write('\n'+NICKNAME+': '+str(total))
            break
        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        pygame.display.flip()
        timer.tick(speed)


def leaderboard():
    items = []
    count = 0
    leader_list=[]
    with open("leaderboard.txt", "r") as leaderboard:
        for count, line in enumerate(leaderboard):
            leader_list.append(line.strip())
    temp_list = []
    for playerscore in leader_list:
        temp_list = playerscore.split(': ')
        items.append({'name': temp_list[0], 'score': temp_list[1]})

    def sortFn(dict):
        return dict['score']

    items.sort(key=sortFn, reverse=True)
    text=''
    temp_list=[]
    for item in items:
        text = ''
        text += str(item['name'])
        text += ": "
        text += str(item['score'])
        text += "\n"
        temp_list.append(text)
    print(temp_list)
    root = tk.Tk()
    root.title("Leaderboard")
    root.columnconfigure(0, weight=1)
    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(column=1, row=1, sticky='ns', padx=0, pady=0)
    mylist = Listbox(root, yscrollcommand=scrollbar.set, font=("Courier", 14))
    for line in range(len(temp_list)):
        mylist.insert(END, temp_list[line])
    mylist.grid(column=0, row=1)
    scrollbar.config(command=mylist.yview)
    root.geometry("250x300+600+300")
    l = tk.Label(root, text="Leaderboard", font=("Courier", 14))
    l.grid(column=0, row=0)
    tk.mainloop()


def change_name(name):
    global NICKNAME
    NICKNAME = name




menu = pygame_menu.Menu('Snake Game', BLOCK_COUNT*20+PADDING*2, BLOCK_COUNT*20+PADDING*2+HEADER_MARGIN, theme=pygame_menu.themes.THEME_GREEN)

menu.add.text_input('Name :', default='Player 1', onchange=change_name)
menu.add.selector('Size :', [('Small', 1), ('Medium', 2), ('Large', 3)], onchange=set_size)
menu.add.selector('Speed :', [('Slow', 1), ('Medium', 2), ('Fast', 3)], onchange=set_speed)
menu.add.button('Leaderboard', leaderboard)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)