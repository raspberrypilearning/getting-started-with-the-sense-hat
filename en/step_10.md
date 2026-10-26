## Challenge: putting it all together

Now that you've explored most of the features of the Sense HAT, you can combine them to create a project. Here's an example reaction game, which could be used by the astronauts to test their reflexes:

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-reaction-game" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise.

Rotate the board to make the arrow point up. If you match it in time, the arrow turns green and your score increases; if not, your arrow turns red and the game ends. The game keeps showing arrows in new orientations until you lose, and each turn gets faster.

If you're using the Code Editor, drag the Sense HAT model to tilt it: up or down first, then left or right. Tilting it in time is tricky, so the game is easier to play on a real Sense HAT.

This idea combines:

  - Showing messages and images on the LED matrix
  - Setting and detecting the orientation
  - Use of variables, randomisation, iteration, and selection

As this is more complicated than previous programs in this resource, it's worth planning out the steps involved in pseudo-code:

`Import` the required libraries (`sense_hat`, `time`, `random`)  
Create a sensehat object

Define variables for the colours needed (white, green, red, blank)  
Create three different arrows (white, green, red)  
Set a variable `pause` to 3 (the initial time between turns)  
Set variables `score` and `angle` to `0`  
Set a variable called `play` to `True` (this will be used to stop the game later)  

`while` `play == True`  
Choose a new `random` angle
Display the white arrow
`Sleep` for current pause length  
`If` orientation matches the arrow...  
  Add a point and turn the arrow green  
  Otherwise set play to `False` and display the red arrow

Shorten the pause duration slightly  
Pause before the next arrow  

When loop is exited, display a message with the score  

--- collapse ---
---
title: Solution
---

```python
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
```

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-reaction-game" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-reaction-game){:target="_blank"}

--- /collapse ---
