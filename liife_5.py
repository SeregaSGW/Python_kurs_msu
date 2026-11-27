import matplotlib.pyplot as plt

X = 16
Y = 16
TAKT = 25

pole = [[0]*Y for i in range(X)]

figura = [ #По сути это глайдер (других фигур не помню)
    (1,2),
    (2,3),
    (3,1),
    (3,2),
    (3,3),
]
for x,y in figura:
    pole[x][y] = 1

"""
Если клетка была «мёртвой», но 3 её соседа живы, то клетка стала «живой».
Если клетка была «живой» и у нее либо меньше 2, либо больше 3 соседей, то клетка становится «мёртвой».
В противном случае клетка сохранит предыдущее состояние.
"""
def spawn_sosed(setka,x,y):
    count = 0
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if dx == 0 and dy == 0:
                continue
            sosx = x + dx
            sosy = y + dy
            if 0 <= sosx < X and 0 <= sosy < Y:
                count += setka[sosx][sosy]
    return count

def generation(setka):
    new_setka = [[0]*Y for i in range(X)]
    for x in range(X):
            for y in range(Y):
                 live = setka[x][y] == 1
                 sosed = spawn_sosed(setka,x,y)

                 if not live and sosed == 3:
                      new_setka[x][y] = 1
                 elif live and (sosed < 2 or sosed > 3):
                        new_setka[x][y] = 0
                 else:
                      new_setka[x][y] = setka[x][y]
    return new_setka
# plt.imshow(c, cmap = plt.cm.Set3)
# plt.colorbar()
for i in range(TAKT):
    plt.imshow(pole, cmap = "binary")
    plt.pause(0.1) #Без этого цикл сразу переходил к концу. Об этой косанде я не знал. Подсказал ИИ :/
    pole = generation(pole)
plt.show()