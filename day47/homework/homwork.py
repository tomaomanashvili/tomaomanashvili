import turtle

# Initialisation de la fenêtre Turtle
window = turtle.Screen()
window.title("Académie d'informatique")
window.bgcolor("skyblue")

# Initialisation de la tortue
builder = turtle.Turtle()
builder.speed(0)

# Fonctions pour dessiner des parties du bâtiment
def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_window(t, width, height):
    t.begin_fill()
    t.fillcolor("lightblue")
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

    t.penup()
    t.forward(width / 4)
    t.left(90)
    t.forward(height / 2)
    t.pendown()

    t.begin_fill()
    t.fillcolor("white")
    for _ in range(2):
        t.forward(height / 2)
        t.left(90)
        t.forward(width / 2)
        t.left(90)
    t.end_fill()

    t.penup()
    t.backward(height / 2)
    t.right(90)
    t.backward(width / 4)
    t.pendown()

def draw_door(t, width, height):
    draw_rectangle(t, width, height, "brown")
    t.penup()
    t.forward(width / 2)
    t.left(90)
    t.forward(height / 4)
    t.pendown()
    t.dot(width / 5, "yellow")
    t.penup()
    t.backward(height / 4)
    t.right(90)
    t.backward(width / 2)
    t.pendown()

def draw_roof(t, width):
    t.begin_fill()
    t.fillcolor("darkred")
    t.forward(width / 2)
    t.left(120)
    t.forward(width / 2)
    t.left(120)
    t.forward(width / 2)
    t.left(120)
    t.end_fill()

def draw_building(t, x, y, width, height, floors, windows_per_floor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    floor_height = height / floors
    window_width = width / (windows_per_floor * 1.5)
    window_height = floor_height / 1.5
    
    # Dessin du bâtiment
    draw_rectangle(t, width, height, "lightgrey")

    # Dessin des fenêtres
    for floor in range(floors):
        for window in range(windows_per_floor):
            t.penup()
            t.goto(x + window * window_width * 1.5 + window_width / 2, y + floor * floor_height + floor_height / 4)
            t.pendown()
            draw_window(t, window_width, window_height)
            t.penup()
    
    # Dessin de la porte
    t.penup()
    t.goto(x + width / 2 - window_width, y)
    t.pendown()
    draw_door(t, window_width * 2, floor_height * 1.5)
    
    # Dessin du toit
    t.penup()
    t.goto(x, y + height)
    t.pendown()
    draw_roof(t, width)

# Dessin de l'immeuble
draw_building(builder, -150, -200, 300, 400, 10, 5)

# Finalisation
builder.hideturtle()
window.mainloop()
