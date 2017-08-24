## Setting orientation

So far, all our text and images have appeared the same way up, assuming that the HDMI port is at the bottom. However, this may not always be the case (especially in space) so you may want to change the orientation of the matrix. To do this, you can use the `sense.set_rotation()` method and inside the brackets enter one of four angles (0, 90, 180, 270).

To rotate your screen by 180 degrees you'd use this line:

```python
sense.set_rotation(180)
```

- When used in the rainbow program it would look like this:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

	r = (255, 0, 0)
	o = (255, 127, 0)
	y = (255, 255, 0)
	g = (0, 255, 0)
	b = (0, 0, 255)
	i = (75, 0, 130)
	v = (159, 0, 255)
	e = (0, 0, 0)

    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,r,r,o,o,r,r,e,
    r,o,o,y,y,o,o,r,
    o,y,y,g,g,y,y,o,
    y,g,g,b,b,g,g,y,
    b,b,b,i,i,b,b,b,
    b,i,i,v,v,i,i,b
    ]

    sense.set_pixels(image)
    sense.set_rotation(180)
    ```

- Click **File** and **Save As**, give your program a name e.g. [`rainbow_flip.py`](resources/rainbow_flip.py), then press `F5` to run.

2. You could also create spinning text using a **for** loop:

    ```python
    from sense_hat import SenseHat
    from time import sleep

    sense = SenseHat()

    sense.show_letter("J")

    angles = [0, 90, 180, 270, 0, 90, 180, 270]
    for r in angles:
        sense.set_rotation(r)
        sleep(0.5)
    ```

    This program displays the letter "J" and then sets the rotation to each value in the angles list with a 0.5 second pause.

- Click **File** and **Save As**, give your program a name e.g. [`spinning_j.py`](resources/spinning_j.py), then press `F5` to run.

    <iframe src="https://trinket.io/embed/python/2f48e31b56" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- You can also flip the image on the screen, either horizontally or vertically, using these lines:

    ```python
    sense.flip_h()
    ```

    or

    ```python
    sense.flip_v()
    ```

    With this example you could create a simple animation by flipping the image repeatedly:

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

- Click **File** and **Save As**, give your program a name e.g. [`eyes.py`](resources/eyes.py), then press `F5` to run.

<iframe src="https://trinket.io/embed/python/27b25ac047" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Ideas

- Create a spinning image, using one of the drawing techniques shown already, and then use the `sense.set_rotation` method to make it spin.
- Using what you've done so far, you should be able to make an electronic die like the one shown here:

[![Sense HAT Die](https://img.youtube.com/vi/v=UfP-R6ArMSk.jpg)](https://www.youtube.com/watch?v=UfP-R6ArMSk)

This die makes use of:

- Displaying text
- Timing
- Setting rotation
- Random numbers
- Variables

