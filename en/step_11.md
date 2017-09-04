## Challenge: putting it all together

Now that you've explored most of the features of the Sense HAT, you can combine them to create a project. Here's an example reaction game, which could be used by the astronauts to test their reflexes:

<iframe src="https://trinket.io/embed/python/5634ef8bd6?outputOnly=true&start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Rotate the board to make the arrow point up. If you match it in time, the arrow turns green and your score increases; if not, your arrow turns red and the game ends. The game keeps showing arrows in new orientations until you lose, and each turn gets faster.

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

<iframe src="https://trinket.io/embed/python/5634ef8bd6?toggleCode=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- /collapse ---
