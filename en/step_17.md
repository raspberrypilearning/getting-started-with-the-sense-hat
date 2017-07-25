## Putting it all together

Now that you've explored most of the features of the Sense HAT, you could combine them to create a project. Here's an example reaction testing game, which could be used by the astronauts to test their reflexes.

The game will display an arrow on the LED matrix and select a random orientation for it. The player must rotate the board to match the arrow. If they match it in time the arrow turns green and their score increases; if not their arrow turns red and the game ends, telling them their score. The game keeps showing arrows in new orientations until the player loses, and each turn gets faster.

This idea combines:

  - Showing messages and images on the LED matrix
  - Setting and detecting the orientation
  - Use of variables, randomisation, iteration, and selection

As this is more complicated than previous programs it's worth planning out the steps involved in **pseudocode**.

  > import the required libraries (sense_hat, time, random)  
  > create a sense object
  >
  > Set up the colours needed  
  > Create 3 different arrows (white, green, red)  
  > Set a variable **pause** to 3 (the initial time between turns)  
  > Set variables **score** and **angle** to 0  
  > Create a variable called **play** set to `True` (this will be used to stop the game later)  
  >  
  > Begin a loop which continues while `play == True`  
  > Set a new random angle (use **random.choice()** method)  
  > Show the white arrow and sleep for current pause length  
  > Check whether orientation matches the arrow  
  > ---if it does then add a point and turn the arrow green  
  > ---otherwise set play to `False` and turn the arrow red  
  > Shorten the pause duration slightly  
  > Pause before the next arrow  
  >  
  > When loop is exited, display a message with the score  

If you turned this into Python it could look like this:

```python
from sense_hat import SenseHat
from time import sleep
from random import choice

sense = SenseHat()

# set up the colours (white, green, red, empty)

w = [150, 150, 150]
g = [0, 255, 0]
r = [255, 0, 0]
e = [0, 0, 0]

# create images for three different coloured arrows

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

pause = 3
score = 0
angle = 0
play = True

sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

while play:
    last_angle = angle
    while angle == last_angle:
        angle = choice([0, 90, 180, 270])
    sense.set_rotation(angle)
    sense.set_pixels(arrow)
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

    if x == -1 and angle == 180:
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
      sense.set_pixels(arrow_red)
      play = False

    pause = pause * 0.95
    sleep(0.5)

msg = "Your score was %s" % score
sense.show_message(msg, scroll_speed=0.05, text_colour=[100, 100, 100])
```

Click **File** -- **Save As**, give your program a name e.g. [`reaction_game.py`](resources/reaction_game.py), then press **F5** to run.

Here's a video showing it being demonstrated:

[![Sense HAT Dice](https://img.youtube.com/vi/k1ZB8jORb74/0.jpg)](https://www.youtube.com/watch?v=k1ZB8jORb74)

### Ideas

There are lots of potential developments for this game:
- Include shake actions as well as orientation.
- Make use of the humidity sensor to detect breath; the player could be prompted to breathe on the board as an action.
- Include more than 4 directions; players have to hold at 45 degrees.

