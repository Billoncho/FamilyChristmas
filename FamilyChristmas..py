# FamilyChristmas.py
# Billy Ridgeway
# Draws an interactive Christmas tree where the user can click to add ornaments with members of their family's names on them.

from turtle import *      # Import all names from the turtle library.
import random             # Imports the random library.
colormode(255)            # Allows the use of r, g, b values for color.

# Creates a list of the user's family.
family = ["Bobbie", "Carolynn", "Solome", "Billy", "Lourdes", "Natalia", "Mr. Griz"]
random.shuffle(family)    # Randomly shuffles the family members names.
fnum = 0                  # Sets the variable fnum to 0.
shape("turtle")           # Sets the shape of the pen to a turtle.
color("brown")            # Sets the color to brown.
penup()                   # Lifts the pen to prevent drawing.
goto(-20, -175)           # Moves the pen to the x y coordinates.
pendown()                 # Sets pen to draw.
forward(40)               # Moves the pen 40 pixels.
left(90)                  # Turn the pen left 90 degrees.
forward(40)               # Moves the pen 40 pixels. 
left(90)                  # Turn the pen left 90 degrees.
forward(40)               # Moves the pen 40 pixels.
left(90)                  # Turn the pen left 90 degrees.
forward(40)               # Moves the pen 40 pixels.
left(90)                  # Turn the pen left 90 degrees.
color("green")            # Sets color to green.
penup()                   # Lifts the pen to prevent drawing.
goto(-150,-135)           # Moves the pen to the x y coordinates.
pendown()                 # Sets pen to draw.
forward(300)              # Moves the pen 300 pixels.
left(120)                 # Turn the pen left 120 degrees.
forward(300)              # Moves the pen 300 pixels.
left(120)                 # Turn the pen left 120 degrees.
forward(300)              # Moves the pen 300 pixels.
color("gold")             # Sets the color to green.
penup()                   # Lifts the pen to prevent drawing.
right(180)                # Turn the pen right 180 degrees.
forward(300)              # Moves the pen 300 pixels.
pendown()                 # Sets pen to draw.
dot(60)                   # Draw a dot 60 pixels.

def draw_name(x,y):                           # Define the functio draw name.
  global fnum                                 # Declare fnum global.
  fname = family[fnum % len(family)]          # Cycles repeatedly through the list of family names by setting fname to the family element fnum mod the length of family.
  fnum = fnum+1                               # Increase fnum's value by 1.
  r = random.randint(0,256)                   # Pick a random shade of red.
  g = random.randint(0,256)                   # Pick a random shade of green.
  b = random.randint(0,256)                   # Pick a random shade of blue.
  color((r, g, b))                            # Sets color to our randomly generated r, g, b.
  penup()                                     # Lifts the pen to prevent drawing.
  goto(x,y)                                   # Moves the pen to the x y coordinates.
  pendown()                                   # Sets pen to draw.
  dot(20)                                     # Draw a dot 20 pixels.
  penup()                                     # Lifts the pen to prevent drawing.
  forward(8)                                  # Moves the pen 8 pixels.
  pendown()                                   # Sets pen to draw.
  write(fname, font=("Arial", 12, "normal"))  # Writes the student's name using normal Arial font size 12.
  penup()                                     # Lifts the pen to prevent drawing.
  goto(0,110)                                 # Moves the pen to the x y coordinates.
  color("gold")                               # Sets color to gold.
getscreen().onscreenclick(draw_name)          # Returns the object the pen is drawing on and when the screen is clicked writes a name.
