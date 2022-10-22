import turtle
import math
import random
from time import *

#Board state
board = ["0"] * 10

bob = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(400,300) #Screen size

#Color of shape
X_color = 'red'
O_color = 'blue'

#Coord of box
box: dict[int, tuple] = {
    1: (-50, 50),
    2: (0, 50),
    3: (50, 50),
    4: (-50, 0),
    5: (0, 0),
    6: (50, 0),
    7: (-50, -50),
    8: (0, -50),
    9: (50, -50),
}

#Win Conditions
wins = (
    *((1, 2, 3), (4, 5, 6), (7, 8, 9)),  # Horizontal
    *((1, 4, 7), (2, 5, 8), (3, 6, 9)),  # Vertical
    *((1, 5, 9), (3, 5, 7)),  # Diagonal
)

#goto function
def go_to(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()

#game state
game_over = False

#End game
def end():
    sleep(1)
    turtle.bye()

#Text font
fonts = ('Arial',20, 'normal')
turns = 0 
#Check winner or for a tie
def check():
    global game_over
    for l in wins:  
        if len(set([board[m] for m in l])) == 1 and board[l[0]] != "0": #once there is 3 in a row 
            go_to(0, -125)
            if board[l[0]] == 'X': #if 3 in a row is X
                bob.pencolor(X_color)
                bob.write('X is the winner!', align='center', font=fonts)
                game_over = True
                end()
            else: 
                bob.pencolor(O_color)
                bob.write('O is the winner!', align='center', font=fonts)
                game_over = True
                end()
        if turns == 9:
            go_to(0, -125)
            bob.pencolor('green')
            bob.write("It's a Tie!", align='center', font=fonts)
            game_over = True
            end()
            
            
                
#Board SetUp
def board_setup():
    bob.pencolor('white')
    bob.pensize(4)
    x1 = -25
    y1 = -25
    for i in range(4):
        bob.penup()
        if i < 2: #horizotnal line
            bob.goto(x1,75)
            bob.pendown()
            bob.goto(x1,-75)
            x1+=50
        else: #vertical lines
            bob.goto(-75, y1)
            bob.pendown()
            bob.goto(75,y1)
            y1+= 50
board_setup()

#Draw X
def draw_x():
    bob.speed(0)
    bob.pencolor(X_color)
    bob.setheading(135)
    bob.forward(20*math.sqrt(2))
    bob.pendown()
    bob.setheading(-45)
    bob.forward(40*math.sqrt(2))
    bob.penup()
    bob.setheading(90)
    bob.forward(40)
    bob.pendown()
    bob.setheading(225)
    bob.forward(40*math.sqrt(2))
    
#Draw o
def draw_o():
    bob.speed(0)
    bob.pencolor(O_color)
    bob.setheading(90)
    bob.forward(20)
    bob.setheading(0)
    bob.pendown()
    bob.circle(-20)

#Choose Who goes First
def go_first():
    first = random.randint(1, 2)
    go_to(0,100)
    if first == 1:
        bob.pencolor(X_color)
        bob.write('X goes first', align='center', font=fonts)
        global current_turn
        current_turn = True
    elif first == 2:
        bob.pencolor(O_color)
        bob.write('O goes first', align='center',font=fonts)
        current_turn = False
go_first()

#Turn
def turn():
    global turns
    turns +=1
    global current_turn
    global shape
    if current_turn:
        draw_x()
        current_turn = not current_turn
        shape = 'X'
    else:
        draw_o()
        current_turn = not current_turn
        shape = 'O'

#Check if there is already a shapebol there
def check_shape(x: int):
    bob.goto(box[x])
    if board[x] == '0':
        turn()
        board[x] = shape
    else:
        turtle.textinput('Spots taken', 'Please choose a different square')
    
#wDraw where the user click
def coords(x, y):
    if not game_over:
        bob.penup()
        leftInterval_x = [-75,-25,25]
        right_interval_x = [-25,25,75]
        leftInterval_y = [25,25,25,-25,-25,-25,-75,-75,-75]
        rightInterval_y = [75,75,75,25,25,25,-25,-25,-25]
        boxes = [(leftInterval_x[box%3],right_interval_x[box%3],leftInterval_y[box],rightInterval_y[box]) for box in range(9)]
        check_shape([box+1 for box,interval in enumerate(boxes) if interval[0] < x < interval[1] and interval[2] < y < interval[3]][0])
        check()
    
bob.hideturtle()
turtle.onscreenclick(coords)

wn.mainloop()