## Displaying images

You can fill the whole LED matrix with a single colour by using the `clear` method with the colour you've picked. 

[[[rpi-sensehat-display-colour]]]

### Setting single pixels

The LED matrix can display more than just text! We can control each LED individually to create an image.

[[[rpi-sensehat-led-coordinates]]]

+ Light up the pixels (LEDs) in the four corners of the matrix in a colour of your choice.

Can you guess what this code creates?

```python
from sense_hat import SenseHat

sense = SenseHat()

sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))
```

Click **Run** to check your guess.

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-step-6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise. If you see a white smiley face, click **Run** again.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-step-6){:target="_blank"}

+ Change the code to make a different pixel picture.

### Setting multiple pixels

Setting pixels individually can work brilliantly, but it gets rather complex when you want to set multiple pixels. To change all the pixels in one go with the `set_pixels` command.

+ Use the `set_pixels` method to display an image on the LED matrix.

[[[rpi-sensehat-multiple-pixels]]]
