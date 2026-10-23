## Setting orientation

So far, all our text and images have appeared the same way up, with the HDMI port at the bottom. However, this may not always be the true orientation of the Sense HAT (especially in outer space), so sometimes you might want to change the orientation of the LED matrix.

[[[rpi-sensehat-rotate-led]]]

+ Change the orientation of the pixel picture from the previous step by adding code to rotate the display below the code you wrote to connect to the Sense HAT:

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

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-step-6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise. If you see a white smiley face, click **Run** again.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-step-6){:target="_blank"}

You can create a simple animation by flipping an image repeatedly:

```python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h()
```

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-step-7" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-step-7){:target="_blank"}
