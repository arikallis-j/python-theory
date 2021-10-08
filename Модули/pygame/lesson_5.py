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



#переменные для персонажа

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

#функция координат центра персонажа
def center():
    x_c = round(x + weidht//2)
    y_c = round(y + height//2)
    return (x_c, y_c)


#переменные для снаряда

#скорость
V = 8

#максимальное число снарядов
maxBull = 5

#радиус снаряда
bull_radius = 5

#цвет снаряда
bull_color = (255,0,0)

#класс снарядов
class snaryad():
    """класс снарядов"""
    #функция инициализации
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = V * facing
    #функция отрисовки
    def draw(self, win):
        pygame.draw.circle(win, 
                           self.color, 
                           (self.x, self.y), 
                           self.radius)

#массив снарядов
bullets = []

#прыжок

#условие прыжка
isJump = False

#счетчик
jumpCount = 10


#анимация
left = False
right = False
animCount = 0
lastMove = "right"


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

    for bullet in bullets:
        bullet.draw(win)

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
    #цикл проверки вылета снарядов
    for bullet in bullets:
        if (bullet.x < X_win) and (bullet.x > 0):
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #массив всех зажатых кнопок сейчас
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:

        #проверка направления движения снаряда
        if lastMove == "right":
            facing = 1
        elif lastMove == "left":
            facing = -1
        else:
            facing = 0

        if len(bullets) < maxBull:
            bullets.append(snaryad(center()[0],
                                   center()[1], 
                                   bull_radius,
                                   bull_color,
                                   facing))

    #если зажата кнопка ВЛЕВО/ВПРАВО И не выходит за границы
    if keys[pygame.K_LEFT] and x > aboard:
        x -= speed
        left = True
        right = False
        lastMove = "left"

    elif keys[pygame.K_RIGHT] and x < (X_win - aboard - weidht):
        x += speed
        right = True
        left = False
        lastMove = "right"
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