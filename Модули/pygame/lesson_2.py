import pygame

X_win = 500
Y_win = 500

pygame.init()
win = pygame.display.set_mode((X_win,Y_win))

#задание названия окна
pygame.display.set_caption("Cubes_game")


#переменные для объекта

#координаты
x = 50
y = 50

#ширина и высота
weidht = 40
height = 60

#скорость
speed = 5

#цвет
color = (0,0,255)
back_color = (0,0,0)

#переменные цикла

#задержка в милисекнудах
t = 100

#условие повторения цикла
run = True

#бесконечный цикл выполнения программы
while run:
    
    #функция задержки на t
    pygame.time.delay(t)

    #цикл проверки событий из набора pygame
    for event in pygame.event.get():

            #тип события ВЫХОД
            if event.type == pygame.QUIT:
                run = False

    #массив всех зажатых кнопок сейчас
    keys = pygame.key.get_pressed()

    #если зажата кнопка <name>
    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed
    #заливка окна цветом back_color
    win.fill(back_color)
    #отрисовка квадрата 
        #на поверхности win, 
        #цвета color
        #с координатами x,y
        #c размерами weidht, height
    pygame.draw.rect(win, color, (x,y, weidht, height))

    #функция обновления экрана
    pygame.display.update()

#функция завершения работы pygame
pygame.quit()
