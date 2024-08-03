import random
from tkinter import *

window = Tk()
window.title("Minesweeper")
buttons = []
now_state = "normal"
q = 0

# random_map = [random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8], k = 2) for i in range(10)] 
random_map = [[0,0], [4,8], [6,1], [6,8], [1,7], [1,4], [7,8], [7,3], [7,5], [8,8]]
calculate_map = [[0]*11 for i in range(11)] 
history = [[0]*9 for i in range(9)] 

def p_C():
    for i in range(1,10): 
        # print(calculate_map[i])
        for j in range(1,10): 
            print(calculate_map[i][j], end = "  ")
        print("")

for [map_x, map_y] in random_map:
    for cal_x in range(3):   
        for cal_y in range(3):
            calculate_map[map_x + cal_x][map_y + cal_y] += 1      
for [map_x, map_y] in random_map:
    calculate_map[map_x + 1][map_y + 1] = "x"
   
# p_C()
def print_lose():
    t = StringVar()
    for [mines_x, mines_y] in random_map:
        buttons[mines_x][mines_y].destroy()
        t.set(str(calculate_map[mines_x+1][mines_y+1]))
        print("x: ",f"{calculate_map[mines_x+1][mines_y+1]}, ({mines_x+1}, {mines_y+1})")
        Label(window, width = 2, fg = "blue", bg = "#F87B29", 
            font = ("bole", 14), textvariable = t, 
            justify = RIGHT).grid(row = mines_x, column = mines_y)
        Label(window, fg = "blue", 
            font = ("bole", 16), text = "you lose.", 
            justify = LEFT).grid(row = 10, columnspan = 4)

def destroy_button(i, j):
    t = StringVar()
    buttons[i][j].destroy()
    t.set(str(calculate_map[i+1][j+1]))
    print(calculate_map[i+1][j+1])
    Label(window, width = 2, fg = "blue", bg = "#F87B29", 
          font = ("bole", 14), textvariable = t, 
          justify = RIGHT).grid(row = i, column = j)
    if [i, j] in random_map:
        print_lose()

def change_text(i, j):
    if history[i][j] == 0:
        button_mark = "▲"
        history[i][j] = 1
    else:
        button_mark = ""
        history[i][j] = 0
    # print(f"text{i}, {j},  {button_mark}")
    buttons[i][j].config(text = button_mark)

def mark(i, j):
    global now_state

    change_text(i, j)
   
    # state button 狀態(normal, active, disabled)

def trigger(i, j):
    global q
    if q == 1:
        mark(i, j)
    else:
        destroy_button(i, j)


def change():
    global q
    print(q, "0q")

    if q == 0:
        print(q, "2q")
        now_state = "normal"
        q = 1
        m.config(bg = "red")
    else:
        print(q, "1q")
        now_state = "disabled"
        q = 0  
        m.config(bg = "#FFFFFF")
        
    for ii in range(9):
        for jj in range(9):
            if history[ii][jj] == 1:
                buttons[ii][jj].config(state = now_state)

for i in range(9):
    row = []
    for j in range(9):
        b = Button(window, text = "", width = 2, height = 1, command = lambda i = i, j = j: trigger(i, j))
        b.grid(row = i, column = j)
        row.append(b)
    buttons.append(row)

m = Button(window, text = "chanage", width = 8, height = 2, command = change)
m.grid(row = 9, column = 0, columnspan= 3 )

mainloop()
# test add