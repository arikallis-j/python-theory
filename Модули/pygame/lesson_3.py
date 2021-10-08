import pygame

#размеры окна
X_win = 500
Y_win = 500

#ширина границы
aboard = 5

pygame.init()
win = pygame.display.set_mode((X_win,Y_win))
pygame.display.set_caption("Cubes_game")


#переменные для объекта

#ширина и высота
weidht = 40
height = 60

#координаты
x = 50
y = 0 + (Y_win - aboard - height)

#скорость
speed = 5

#цвет
color = (0,0,255)
background_color = (0,0,0)


#прыжок

#условие прыжка
isJump = False

#счетчик
jumpCount = 10

#переменные цикла

#задержка в милисекнудах
t = 25

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

    #если зажата кнопка ВЛЕВО/ВПРАВО И не выходит за границы
    if keys[pygame.K_LEFT] and x > aboard:
        x -= speed

    if keys[pygame.K_RIGHT] and x < (X_win - aboard - weidht):
        x += speed
    
    #для случая НЕпрыжка
    if not(isJump):

        #если зажата кнопка ВВЕРХ/ВНИЗ И не выходит за границы
        if keys[pygame.K_UP] and y > aboard:
            y -= speed 

        if keys[pygame.K_DOWN] and y < (Y_win - aboard - height):
            y += speed

        #если зажата кнопка ПРОБЕЛ - прыжок
        if keys[pygame.K_SPACE]:
            isJump = True

    #для случая прыжка
    else:
        if jumpCount >= -10:
            if jumpCount > 0:
                y -= (jumpCount ** 2) / 2
            elif jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y += 0
            jumpCount -=  1

        else:
            isJump = False
            jumpCount = 10

    #отрисовка экрана
    win.fill(background_color)

    #отрисовка квадрата 
    pygame.draw.rect(win, color, (x,y, weidht, height))

    #функция обновления экрана
    pygame.display.update()

#функция завершения работы pygame
pygame.quit()