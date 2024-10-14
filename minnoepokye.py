from random import randrange                               # Импортируем функцию генерации случайных чисел

rows, cols, mines = (int(i) for i in input().split())     # Количество строк, столбцов, мин.
field = [[0 for col in range(cols)] for row in range(rows)] # Заполняем поле нулями
mine_table = []
for mine in range(mines):                                 # Случайным образом ставим мины
    row = randrange(0, rows)
    col = randrange(0, cols)
    if (row, col) not in mine_table:                       # Если координат мин нет, добавляем их в таблицу
        mine_table.append((row, col))
        field[row][col] = "*"

for row, col in mine_table:                               # Перебираем таблицу координат мин
    for row_i in range(-1, 2):
        temp_row = row + row_i
        for col_j in range(-1, 2):
            temp_col = col + col_j
            if 0 <= temp_row < rows and 0 <= temp_col < cols and field[temp_row][temp_col] != '*': # Проверяем границу поля,
                field[temp_row][temp_col] += 1                                                     # а также что нет мины.

for i in range(rows):                                     # Печатаем поле
    for j in range(cols):
        if field[i][j] == 0:
            print(".", end=" ")
        else:
            print(field[i][j], end=" ")
    print()

mine_table.sort()                                         # Сортируем таблицу координат мин
print(mine_table)                                         # Печатаем таблицу координат для проверки

