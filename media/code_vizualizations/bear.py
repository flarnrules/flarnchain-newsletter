import turtle
import time

# Initialize turtle window
window = turtle.Screen()
window.bgcolor("white")

# Function to save frame as PostScript
def save_postscript(frame_number):
    canvas = turtle.getcanvas()
    canvas.postscript(file=f"frame_{frame_number}.eps")

# Function to draw circle
def draw_circle(color, x, y, radius, fill=False):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
    turtle.circle(radius)
    if fill:
        turtle.end_fill()

# Function to draw claw
def draw_claw(x, y):
    turtle.penup()
    turtle.color("black")
    turtle.goto(x, y)
    turtle.setheading(-30)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(20)
        turtle.left(120)
    turtle.end_fill()

# Function to draw bear
def draw_bear():
    # Draw the different parts of the bear
    draw_circle("brown", 0, -100, 100)
    draw_circle("brown", 0, -200, 120)
    draw_circle("black", -40, -50, 10)
    draw_circle("black", 40, -50, 10)
    draw_circle("black", 0, -70, 15)
    draw_circle("brown", -80, 0, 20)
    draw_circle("brown", 80, 0, 20)
    draw_circle("brown", -70, -200, 30)
    draw_circle("brown", 70, -200, 30)
    draw_claw(-75, -205)
    draw_claw(75, -205)

# Draw bear
draw_bear()

# Pause before fill animation
time.sleep(2)

# Animate the fill-in
frame_number = 0
parts = [
    {"color": "brown", "x": 0, "y": -100, "radius": 100},
    {"color": "brown", "x": 0, "y": -200, "radius": 120},
    {"color": "black", "x": -40, "y": -50, "radius": 10},
    {"color": "black", "x": 40, "y": -50, "radius": 10},
    {"color": "black", "x": 0, "y": -70, "radius": 15},
    {"color": "brown", "x": -80, "y": 0, "radius": 20},
    {"color": "brown", "x": 80, "y": 0, "radius": 20},
    {"color": "brown", "x": -70, "y": -200, "radius": 30},
    {"color": "brown", "x": 70, "y": -200, "radius": 30}
]

for part in parts:
    draw_circle(part["color"], part["x"], part["y"], part["radius"], fill=True)
    save_postscript(frame_number)
    frame_number += 1
    time.sleep(0.5)

# To keep the window open
turtle.done()
