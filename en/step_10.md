## Challenge: Putting it all together

Now that you've explored most of the features of the Sense HAT, you could combine them to create a project. Here's an example reaction game, which could be used by the astronauts to test their reflexes.

<iframe src="https://trinket.io/embed/python/5634ef8bd6?toggleCode=true&runOption=run" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Rotate the board to make the arrow point up. If you match it in time the arrow turns green and your score increases; if not your arrow turns red and the game ends. The game keeps showing arrows in new orientations until you lose, and each turn gets faster.

This idea combines:

  - Showing messages and images on the LED matrix
  - Setting and detecting the orientation
  - Use of variables, randomisation, iteration, and selection

As this is more complicated than previous programs it's worth planning out the steps involved in **pseudocode**.

IMPORT the required libraries (sense_hat, time, random)  
CREATE a sense object

DEFINE variables for the colours needed (white, green, red, blank)  
CREATE three different arrows (white, green, red)  
SET a variable **pause** to 3 (the initial time between turns)  
SET variables **score** and **angle** to 0  
SET a variable called **play** to `True` (this will be used to stop the game later)  

WHILE `play == True`  
CHOOSE a new random angle
DISPLAY the white arrow
SLEEP for current pause length  
IF orientation matches the arrow...  
---ADD a point and turn the arrow green  
---otherwise SET play to `False` and DISPLAY the red arrow

Shorten the pause duration slightly  
Pause before the next arrow  

When loop is exited, display a message with the score  
