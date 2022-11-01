import turtle
import random

#Board state
board = ["0"] * 10

#Create a 400x300 screen with black background
bob = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(400,300)
turtle.title('Activity 1.1.9 Test: Tic Tac Toe Game')
bob.pensize(4)

#Color of shape
X_color = 'red'
O_color = 'blue'

#Coord of box 1-9
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

#Creat Star
star_cor = 70
def star():
    global star_cor
    trtl.setheading(0)
    trtl.goto(-30, star_cor)
    trtl.pendown()
    trtl.pencolor('gold')
    trtl.fillcolor('gold')
    trtl.begin_fill()
    for side in range(5):
        trtl.forward(60)
        trtl.right(144)
    trtl.end_fill()
    star_cor -=120

#Border Outline + Star
index = 0
border_color = ['light blue', 'yellow', 'orange'] #Border Color
def end_deco():
    y_cor = 130
    vert_angle = 270
    x_cor = 175
    hort_angle = 180
    global index
    index = 0
    global bobs
    bob2 = turtle.Turtle()
    bob2.hideturtle()
    bobs = [bob, bob2]
    global trtl
    for trtl in bobs:
        trtl.penup()
        trtl.shape('triangle')
        trtl.speed(0)
        for border_side in range(2):
            if border_side < 1: #Top and Bottom Triangles
                trtl.goto(-182, y_cor)
                while trtl.xcor() < 182:
                    trtl.setheading(vert_angle)
                    stamp(0)
                y_cor -=250
                vert_angle = -vert_angle
            else:
                trtl.goto(x_cor, 100)
                while trtl.ycor() > -110: #The Side Triangles
                    trtl.setheading(hort_angle)
                    stamp(-90)
                trtl.setheading(hort_angle)
                hort_angle -=180
                x_cor -=357
        star()
        
#Alternate Color and Stamp Turtle
def stamp(x):
    global index
    trtl.color(border_color[index])
    trtl.stamp()
    index += 1
    if index > 2:
        index = 0
    trtl.setheading(x)
    trtl.forward(25)

#Draws Textbox for winner 
def textbox():
    bob.setheading(0)
    wn.clear()
    wn.bgcolor('black')
    bob.speed(0)
    bob.pencolor('pink')
    go_to(-100,-20)
    for text_box in range(2): #Draws text box for win message
        bob.forward(200)
        bob.circle(20, 180)
    go_to(0,-15)

#Text font
fonts = ('Arial',20, 'normal')

#Check winner or for a tie
def check_winner():
    global game_over
    for win_con in wins:  
        if len(set([board[spot] for spot in win_con])) == 1 and board[win_con[0]] != "0": #once there is 3 in a row 
            if board[win_con[0]] == 'X': #if 3 in a row is X
                textbox()
                bob.pencolor(X_color)
                bob.write('X is the winner!', align='center', font=fonts)
                end_deco()
                game_over = True
            elif board[win_con[0]] == 'O': #if 3 in a row is O
                textbox()
                bob.pencolor(O_color)
                bob.write('O is the winner!', align='center', font=fonts)
                end_deco()
                game_over = True
        
#Draws the board
def board_setup():
    bob.pencolor('white')
    x1 = -75
    y1 = -75
    for side in range(8):
        bob.penup()
        if side < 4: #Vertical line
            bob.goto(x1,75)
            bob.pendown()
            bob.goto(x1,-75)
            x1+=50
        else: #Horitzontal lines
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
    bob.forward(20*2**(1/2))
    bob.pendown()
    bob.setheading(-45)
    bob.forward(40*2**(1/2))
    bob.penup()
    bob.setheading(90)
    bob.forward(40)
    bob.pendown()
    bob.setheading(225)
    bob.forward(40*2**(1/2))
    
#Draw o
def draw_o():
    bob.speed(0)
    bob.pencolor(O_color)
    bob.setheading(90)
    bob.forward(20)
    bob.setheading(0)
    bob.pendown()
    bob.circle(-20)

#Choose who goes first
def go_first():
    player_1 = turtle.textinput('Name', 'Who is X?: ') #Ask for name
    player_2 = turtle.textinput('Name', 'Who is O?: ') #Ask for name
    first = random.randint(1, 2)
    go_to(0,100)
    if first == 1:
        bob.pencolor(X_color)
        bob.write(f'{player_1} goes first!', align='center', font=fonts)
        global turn_x
        turn_x = True
    elif first == 2:
        bob.pencolor(O_color)
        bob.write(f'{player_2} goes first!', align='center',font=fonts)
        turn_x = False
go_first()

#Current turn
turns = 0 

#Turn Change and Draw shape based on whose turn it is
def turn():
    global turns
    global turn_x
    global shape
    if turn_x:
        draw_x()
        turn_x = not turn_x
        shape = 'X'
    else:
        draw_o()
        turn_x = not turn_x
        shape = 'O'
    turns +=1
    if turns == 9:
        game_over = True

#Check if spot is already taken by another box
def check_shape(x):
    bob.goto(box[x])
    if board[x] == '0':
        turn()
        board[x] = shape
    else:
        pass
    
#Draw shape where the user click
def coords(x, y):
    if not game_over:
        bob.penup()
        leftInterval_x = [-75,-25,25]
        right_interval_x = [-25,25,75]
        leftInterval_y = [25,25,25,-25,-25,-25,-75,-75,-75]
        rightInterval_y = [75,75,75,25,25,25,-25,-25,-25]
        boxes = [(leftInterval_x[box%3],right_interval_x[box%3],leftInterval_y[box],rightInterval_y[box]) for box in range(9)] #List of intervals for all boxes
        for box, interval in enumerate(boxes, start= 1):
            if interval[0] < x < interval[1] and interval[2] < y < interval[3]:
                check_shape(box)
            else:
                pass
        check_winner()

    
bob.hideturtle()
turtle.onscreenclick(coords)

wn.mainloop()