import random
import tkinter as tk


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()



def generator(heigth, columns, array_2d):
    colors = ["red", "white", "yellow", "blue", "green", "purple", "pink", "orange", "brown"]
    accept_colors = []

    for i in range(columns-2):
        accept_colors.append(random.choice(colors))

    accept_colors *= (columns - 2)
    random.shuffle(accept_colors)

    for i in range(heigth):
        array_2d.append([0] * columns)

    first_random_empty = second_random_empty = random.randint(0, columns-1)

    while second_random_empty == first_random_empty:
        second_random_empty = random.randint(0, columns-1)

    print(first_random_empty, second_random_empty)

    for i in range(heigth):
        for j in range(columns):
            if j == first_random_empty or j == second_random_empty:
                array_2d[i][j] = 0
            else:
                rand_color = random.choice(accept_colors)
                array_2d[i][j] = rand_color
                accept_colors.remove(rand_color)


def check_complite(heigth, columns, array):
    for i in range(columns):
        for j in range(heigth):
            if array[j][i] != array[0][i]:
                return False
    return True

# a = [
#     [8, 8, 1, 7],
#     [8, 8, 5, 7],
#     [8, 8, 1, 7],
# ]

# print(check_complite(3,4,a))
