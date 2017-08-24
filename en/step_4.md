## Displaying text

## Displaying a message

+ Display the text "Astro Pi is awesome" on your Sense HAT's LED display

[[[rpi-sensehat-show-message]]]

We can change how the message is displayed by adding some extra **parameters** to the `show_message` command.

### Extra parameters

**scroll_speed** - affects how quickly the text moves on the screen. The default value is 0.1. The bigger the number, the **slower** the speed

**text_colour** - alters the colour of the text and is specified using three values for red, green, blue.

**back_colour** - alters the colour of the background and works in the same way as the `text_colour`

+ Add a single line of code before your message to define a variable called `blue` with the value (0, 0, 255)

[[[rpi-sensehat-display-colour]]]

+ Add another line of code to define a variable called `yellow` with the value (255, 255, 0)

+ Add parameters to the `show_message` command to display the text in yellow with a blue background. The part to add is highlighted in blue.

![Coloured text](images/coloured-text.png)

+ Add a parameter called `speed` to the `show_message` command and set the speed equal to 0.05

+ Add a `while` loop to make your scrolling message repeat.

[[[generic-python-while-true]]]

+ Save and run your code and check your message repeats.

### Displaying a single character

The LED matrix can also display a single character, rather than an entire message, using the `show_letter` function which also has some optional **parameters**.

### Extra parameters

**scroll_speed** - affects how quickly the text moves on the screen. The default value is 0.1. The bigger the number, the **slower** the speed

**text_colour** - alters the colour of the text and is specified as three values for red, green, blue. Each value can be between 0 and 255, so (255, 0, 255) would be red + blue = purple

**back_colour** - alters the colour of the background and is specified as three values for red, green, blue. Each value can be between 0 and 255, so (255, 0, 255) would be red + blue = purple

So this program would display a single red "J":

```python
from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

sense.show_letter("J", red)
```

And this program would add the **sleep function** to display letters separated by a brief pause:

```python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

sense.show_letter("O", red)
sleep(1)
sense.show_letter("M", blue)
sleep(1)
sense.show_letter("G", green)
sleep(1)
sense.show_letter("!", black, white)
sleep(1)
sense.clear()
```

Click **File** and **Save As**, give your program a name eg [`omg.py`](resources/omg.py), then press `F5` to run.


<iframe src="https://trinket.io/embed/python/ccb58a3d9d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


For added interest you could use a random number generator to choose a number between 0 and 255 for the colours:

```python
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

r = randint(0,255)
sense.show_letter("O", (r, 0, 0))
sleep(1)

r = randint(0,255)
sense.show_letter("M", (0, 0, r))
sleep(1)

r = randint(0,255)
sense.show_letter("G", (0, r, 0))
sleep(1)

sense.show_letter("!", (0, 0, 0), (255, 255, 255))
sleep(1)
sense.clear()
```

- Click **File** and **Save As**, give your program a name eg [`random_omg.py`](resources/random_omg.py), then press `F5` to run.

    In both these programs the `sense.clear()` method has been used at the end to clear the matrix.

    <iframe src="https://trinket.io/embed/python/45b0f19b65" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


### Ideas

 - Could you use the ideas used so far to tell a joke via the LED screen?
 - All the examples so far could be made shorter, while still achieving the same thing. Can you find ways to make these shorter and more efficient?
 - How would you choose a totally random colour, rather than just a random shade of a colour?
 - If your Sense HAT is connected to the internet, you could use a Twitter library to make it display incoming tweets!
