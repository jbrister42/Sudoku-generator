# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:03:01 2020

@author: jbris
"""
import random
import turtle
###\###\### 0 to 8
###\###\### 9 to 17
###\###\### 18 to 26
#----------
###\###\### 27 to 35
###\###\### 36 to 44
###\###\### 45 to 53
#----------
###\###\### 54 to 62
###\###\### 63 to 71
###\###\### 72 to 80
    
class cell():
    def __init__(self, x, y, s, ans):
        self.x = x
        self.y = y
        self.s = s
        self.ans = ans
    
    def check(self):
        print(self.x, self.y, self.s, self.ans)
        
    def poss(self): # creates a list of possible answers for the given cell
        cand = [] # cand for can do
        if self.ans == 0:    
            for i in range(1,10):
                    if i in rows[self.x-1] and i in columns[self.y-1] and i in squares[self.s-1]:
                        cand.append(i)
        return(cand)
                
# Creates a list of cells with x,y,s coordinates filled with 0's
def create_cells():#
    global cells
    cells = []
    for i in range (1,10):
        for n in range (1,10):
            if i<=3 and n <=3:
                cells.append(cell(i,n,1,0))
            elif i<=3 and n <=6:
                cells.append(cell(i,n,2,0))
            elif i<=3 and n <=9:
                cells.append(cell(i,n,3,0))
            elif i<=6 and n <=3:
                cells.append(cell(i,n,4,0))
            elif i<=6 and n <=6:
                cells.append(cell(i,n,5,0))
            elif i<=6 and n <=9:
                cells.append(cell(i,n,6,0))
            elif i<=9 and n <=3:
                cells.append(cell(i,n,7,0))
            elif i<=9 and n <=6:
                cells.append(cell(i,n,8,0))
            elif i<=9 and n <=9:
                cells.append(cell(i,n,9,0))

def create_grid():
    global squares, rows, columns
    squares = []
    rows = []
    columns = []
    for i in range (9):
        squares.append([1,2,3,4,5,6,7,8,9]) # creates a list of 9 lists of 1-9, each represents a square
        rows.append([1,2,3,4,5,6,7,8,9])
        columns.append([1,2,3,4,5,6,7,8,9])

counter = 0
def genp():        
    global counter
    poss = [] # list of possible answers for each cell
    for ind in range(81):
        poss.append((cells[ind]).poss())
    lens = [] # list of the lenths of each possible answers for each cell
    for i in range(81):
        if poss[i]: # if possibles is empty, put a zero for len
            lens.append(len(poss[i])) # filling list "lens"
        else: 
            lens.append(0)
    #print("list of lengths of possibles", lens)
    place = []
    for i in range(81):
        if lens[i] != 0: # fills placeholder list with list of minimum lengths
            place.append(lens[i])
    if not place and counter < 80: # if place is empty, restart with new grid and cells
        counter = 0 # reset counter
        create_cells()
        create_grid()
        return  
    mint = min(place) # minimum length of possible answer lists that != 0
    mindices = []
    for i in range(81): # produces list of indices for cells with fewest poss's
        if lens[i] == mint:
            mindices.append(i)
    cellno = random.choice(mindices) # chooses from mindices list    
    ans = random.choice(poss[cellno])
    cells[cellno].ans = ans
    squares[cells[cellno].s-1].remove(ans)
    rows[cells[cellno].x-1].remove(ans)
    columns[cells[cellno].y-1].remove(ans)
    print("Cell number: ", cellno,"in square:", cells[cellno].s, "ans:", cells[cellno].ans)
    counter += 1
    for i in range(81):
        if cells[i].ans == 0:
            genp()
        else:
            return

# create initial empty cells and grid
create_cells()
create_grid()

# main loop       
while counter != 81:
    genp()
else:
    print("Puzzle generated")

# Draw out the completed puzzle
wn = turtle.Screen()
wn.title("Completed Sudoku Puzzle")
wn.bgcolor("White")
wn.setup(width=600, height=400)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.hideturtle()
startx = -150
starty = 150
pen.penup()
pen.goto(startx, starty)


for i in range(81):
    pen.penup()
    pen.goto(cells[i].y*30+startx, starty - 30*cells[i].x)
    pen.pendown()
    pen.write(cells[i].ans, align="center", font=("Courier", 24, "normal"))

pen.penup()    
pen.goto(-45,150)
pen.pendown()
pen.goto(-45,-115)

pen.penup()    
pen.goto(45,150)
pen.pendown()
pen.goto(45,-115)

pen.penup()    
pen.goto(-130,65)
pen.pendown()
pen.goto(130,65)

pen.penup()    
pen.goto(-130,-25)
pen.pendown()
pen.goto(130,-25)

while True:
    wn.update()