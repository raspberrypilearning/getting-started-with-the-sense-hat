## Displaying text

Start by opening Python 3 from the main menu.

When following the [guide](https://projects.raspberrypi.org/en/projects/astro-pi-guide/), you will have written a sample program which scrolls text across the LED matrix. The program contains two crucial lines, which import the Sense HAT software and create a `sense` object which represents the Sense HAT.

```python
from sense_hat import SenseHat

sense = SenseHat()
```

The third line is the one that makes the Sense HAT do something:

```python
sense.show_message("Hello my name is Tim Peake")
```

<iframe src="https://trinket.io/embed/python/308a373b5c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

You have probably already discovered that you can easily change the message to your own text, but there are more things that we can do.

- We can expand the `sense.show_message` command to include some extra **parameters** which will change the behaviour of the message.

    | Parameter | Effect |
    | --- | --- |
    | **scroll_speed** | The `scroll_speed` parameter affects how quickly the text moves on the screen. The default value is 0.1. The bigger the number, the **slower** the speed |
    | **text_colour** | The `text_colour` parameter alters the colour of the text and is specified using three values for red, green, blue. Each value can be between 0 and 255, so (255,0,255) would be red + blue = purple |
    | **back_colour** | The `back_colour` parameter alters the colour of the background and works in the same way as the `text_colour` |

    So this program would display the text `Astro Pi is awesome!!` more slowly, with the text in yellow **(255, 255, 0)** and the background in blue **(0, 0, 255)**:

    ```python
	from sense_hat import SenseHat

	sense = SenseHat()

	yellow = (255, 255, 0)
	blue = (0, 0, 255)

	message = "Astro Pi is awesome!!"

	speed = 0.05

	sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
    ```

    <iframe src="https://trinket.io/embed/python/d62aa7f30a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

    You could also make the message repeat using a while loop like this:

    ```python
	from sense_hat import SenseHat

	sense = SenseHat()

	yellow = (255, 255, 0)
	blue = (0, 0, 255)

	message = "Astro Pi is awesome!!"

	speed = 0.05

	while True:
		sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
    ```

    <iframe src="https://trinket.io/embed/python/f833a60218" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- Click **File** -- **Save As**, give your program a name e.g. [`loop_text.py`](resources/loop_text.py), then press **F5** to run.

- The LED matrix can also display a single character, rather than an entire message, using the `sense.show_letter` function which also has some optional **parameters**.

    | Parameter | Effect |
    | --- | --- |
    | **scroll_speed** | The `scroll_speed` parameter affects how quickly the text moves on the screen. The default value is 0.1. The bigger the number, the **slower** the speed |
    | **text_colour** | The `text_colour` parameter alters the colour of the text and is specified as three values for red, green, blue. Each value can be between 0 and 255, so (255, 0, 255) would be red + blue = purple |
    | **back_colour** | The `back_colour` parameter alters the colour of the background and is specified as three values for red, green, blue. Each value can be between 0 and 255, so (255, 0, 255) would be red + blue = purple |

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

