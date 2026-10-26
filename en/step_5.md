## Displaying a single character

+ Display the letter "A" on your Sense HAT's LED display.

[[[rpi-sensehat-show-letter]]]

We can change how the letter is displayed by using two of the same parameters we used for the `show_message` command: `text_colour` and `back_colour`. Letters do not scroll, so there is no `scroll_speed` parameter.

+ Display the letter "J" in red on a white background.

+ Use the `sleep` function to display the letters of your name one at a time, each in a different colour, with a one-second pause between each.

[[[generic-python-sleep]]]

--- collapse ---
---
title: Solution
---
```python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

sense.show_letter("L", red)
sleep(1)
sense.show_letter("a", blue)
sleep(1)
sense.show_letter("u", green)
sleep(1)
sense.show_letter("r", white)
sleep(1)
sense.show_letter("a", yellow)
```

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-step-5-a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise. The first letter can be missed the first time you click **Run**, so click it again to see every letter.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-step-5-a){:target="_blank"}

--- /collapse ---

+ Randomly generate a colour by using `randint` to choose a number between `0` and `255` for each of the three RGB values that make up a colour.

[[[generic-python-random]]]

--- collapse ---
---
title: Solution
---
```python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

sense.show_letter("L", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)
sense.show_letter("u", pick_random_colour())
sleep(1)
sense.show_letter("r", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)

sense.clear()
```

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-step-5-b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise. The first letter can be missed the first time you click **Run**, so click it again to see every letter.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-step-5-b){:target="_blank"}

--- /collapse ---

+ Use `sense.clear()` at the end of your code to clear the LED matrix.
