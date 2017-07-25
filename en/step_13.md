## Displaying images

The LED matrix can display more than just text! We can control each LED individually to create an image. We can accomplish this in a couple of ways.

- The first approach is to set pixels (LEDs) individually; we can do this using the `sense.set_pixel()` method. First, we need to be clear about how we describe each pixel.

    The Sense HAT uses a coordinate system like the one shown below; crucially the numbering begins at **0**, not 1. Also, the origin is in the **top left** rather than the bottom left as you may be used to.

    ![Coordinates](images/coordinates.png)

    - the blue pixel is at coordinates (0, 2)
    - the red pixel is at coordinates (7, 4)

    To replicate the above diagram you would enter a program like this:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.set_pixel(0, 2, [0, 0, 255])
    sense.set_pixel(7, 4, [255, 0, 0])
    ```

    <iframe src="https://trinket.io/embed/python/9a4266d360" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

    Can you guess what the following code creates? Have a go at editing the code.

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.set_pixel(2, 2, [0, 0, 255])
    sense.set_pixel(4, 2, [0, 0, 255])
    sense.set_pixel(3, 4, [100, 0, 0])
    sense.set_pixel(1, 5, [255, 0, 0])
    sense.set_pixel(2, 6, [255, 0, 0])
    sense.set_pixel(3, 6, [255, 0, 0])
    sense.set_pixel(4, 6, [255, 0, 0])
    sense.set_pixel(5, 5, [255, 0, 0])
    ```

- Click **File** -- **Save As**, give your program a name e.g. [`simple_image.py`](resources/simple_image.py), then press **F5** to run.

- Setting pixels individually can work brilliantly, but it gets rather complex when you want to set more pixels. There is another method which can set all the pixels in one go called `sense.set_pixels`. Its use is quite straightforward; we just give a list of colour values for each pixel in the matrix.

    We could enter something like...

    ```python
    sense.set_pixels([[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0],......])
    ```

    ...but this would take ages and be really complex.

    Instead, you can use some variables to define your colour palette (in this example we're using the 7 colours of the rainbow):

    ```python
    r = [255, 0, 0]
    o = [255, 127, 0]
    y = [255, 255, 0]
    g = [0, 255, 0]
    b = [0, 0, 255]
    i = [75, 0, 130]
    v = [159, 0, 255]
    e = [0, 0, 0]  # e stands for empty/black
    ```

    We can then describe our matrix by creating a 2D list of colour names:

    ```python
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
    ```

    We then give the `image` list to the `sense.set_pixels` method and draw the image. The finished program would look like this:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    r = [255,0,0]
    o = [255,127,0]
    y = [255,255,0]
    g = [0,255,0]
    b = [0,0,255]
    i = [75,0,130]
    v = [159,0,255]
    e = [0,0,0]

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
    ```
    
- Click **File** -- **Save As**, give your program a name e.g. [`rainbow.py`](resources/rainbow.py), then press **F5** to run.

    You should have a beautiful rainbow displayed on your LED matrix.
    
    
    <iframe src="https://trinket.io/embed/python/8f36929035" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


### Ideas

- Now you can create images on your LED matrix in two different ways, try creating your own images or sprites.
- Can you alternate between images to create an animation? Check out this [Geek Gurl Diaries](https://www.youtube.com/watch?v=b84EywkQ3HI) video for some inspiration.

