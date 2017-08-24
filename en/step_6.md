## Displaying images

The LED matrix can display more than just text! We can control each LED individually to create an image.

[[[rpi-sensehat-led-coordinates]]]

+ Light up the pixels in the four corners of the matrix in a colour of your choice.

Can you guess what this code creates?

<iframe src="https://trinket.io/embed/python/dc4f166247?toggleCode=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

+ Change the code to make a different pixel picture

Setting pixels individually can work brilliantly, but it gets rather complex when you want to set more pixels. You can set all the pixels in one go with the `set_pixels` command.

+ Create three variables to define three different colours:

```python
b = (0, 0, 255)
g = (0, 255, 0)
y = (255, 255, 0)
```

+ Add code to represent the LED matrix by creating a list of colour names:

```python
image = [
b,b,b,b,b,b,b,b,
b,g,g,g,g,b,b,b,
g,g,g,g,g,g,b,b,
b,g,g,g,g,b,b,b,
b,b,w,w,b,b,b,b,
b,b,w,w,b,b,b,b,
b,b,w,w,b,b,b,b,
g,g,g,g,g,g,g,g
]

```

+ Call the `set_pixels` method to display the image on the LED matrix

[[[rpi-sensehat-multiple-pixels]]]


--- collapse ---
---
title: Solution
---

<iframe src="https://trinket.io/embed/python/1325b597bb" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- /collapse ---
