import pygame

#размеры окна
X_win = 500
Y_win = 500

#начало отрисовки окна
x_win = 0
y_win = 0

#частота кадров
FPS = 30

#ширина границы
aboard = 5

pygame.init()
win = pygame.display.set_mode((X_win,Y_win))
pygame.display.set_caption("Cubes_game")


#загрузка изображений

#фон
bg = pygame.image.load('images/bg.jpg')

#профиль персонажа
playerStand = pygame.image.load('images/idle.png')

#персонаж идет вправо
walkRight = [pygame.image.load('images/right_1.png'), 
             pygame.image.load('images/right_2.png'), 
             pygame.image.load('images/right_3.png'), 
             pygame.image.load('images/right_4.png'), 
             pygame.image.load('images/right_5.png'), 
             pygame.image.load('images/right_6.png')]

#персонаж идет влево
walkLeft = [pygame.image.load('images/left_1.png'), 
            pygame.image.load('images/left_2.png'), 
            pygame.image.load('images/left_3.png'), 
            pygame.image.load('images/left_4.png'), 
            pygame.image.load('images/left_5.png'), 
            pygame.image.load('images/left_6.png')]


#отсчет прорисовки
clock = pygame.time.Clock()



#переменные для объекта

#ширина и высота
weidht = 60
height = 71

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


#анимация
left = False
right = False
animCount = 0


#пред-цикл

#функция отрисовки
def drawWindow():
    global animCount

    #отрисовка на экране картинки bg с координат (x_win,y_win)
    win.blit(bg, (x_win,y_win))

    #проверка для наличия нужных спрайтов
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount//6], (x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount//6], (x,y))
        animCount += 1
    else:
        win.blit(playerStand, (x,y))

    #функция обновления экрана
    pygame.display.update()

#задержка в милисекнудах
t = 25

#условие повторения цикла
run = True

#бесконечный цикл выполнения программы
while run:
    
    #метод часов по FPS кадров в секунду
    clock.tick(FPS)

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
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < (X_win - aboard - weidht):
        x += speed
        right = True
        left = False
    else:
        left = False
        right = False
        animCount = 0
    
    #для случая НЕпрыжка
    if not(isJump):

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

    drawWindow()

#функция завершения работы pygame
pygame.quit()