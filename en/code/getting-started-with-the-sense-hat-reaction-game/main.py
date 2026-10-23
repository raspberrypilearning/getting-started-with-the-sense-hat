# IMPORT the required libraries (sense_hat, time, random) 
from sense_hat import SenseHat
from time import sleep
from random import choice

# CREATE a sense object
sense = SenseHat()

# Set up the colours (white, green, red, empty)

w = (150, 150, 150)
g = (0, 255, 0)
r = (255, 0, 0)
e = (0, 0, 0)

# Create images for three different coloured arrows

arrow = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]

arrow_red = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,e,r,r,e,r,e,
r,e,e,r,r,e,e,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

arrow_green = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e
]

# Set a variable pause to 3 (the initial time between turns)  
# Set variables score and angle to 0  
# Create a variable called play set to True (this will be used to stop the game later)  
pause = 3
score = 0
angle = 0
play = True

sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

# WHILE play == True 
while play:
  
    # CHOOSE a new random angle 
    last_angle = angle
    while angle == last_angle:
        angle = choice([0, 90, 180, 270])
        
    sense.set_rotation(angle)
    
    # DISPLAY the white arrow
    sense.set_pixels(arrow)
    
    # SLEEP for current pause length  
    sleep(pause)
    
    
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)

    print(angle)
    print(x)
    print(y)

    # IF orientation matches the arrow...
    if x == -1 and angle == 180:
        # ADD a point and turn the arrow green  
        sense.set_pixels(arrow_green)
        score += 1
    elif x == 1 and angle == 0:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == -1 and angle == 90:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == 1 and angle == 270:
      sense.set_pixels(arrow_green)
      score += 1
    else:
      # SET play to `False` and DISPLAY the red arrow
      sense.set_pixels(arrow_red)
      play = False

    # Shorten the pause duration slightly  
    pause = pause * 0.95
    
    # Pause before the next arrow 
    sleep(0.5)

# When loop is exited, display a message with the score  
msg = "Your score was %s" % score
sense.show_message(msg, scroll_speed=0.05, text_colour=[100, 100, 100])