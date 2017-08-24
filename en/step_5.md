## Displaying a single character

+ Display the letter "A" on your Sense HAT's LED display

[[[rpi-sensehat-show-letter]]]

We can change how the letter is displayed by using two of the same extra **parameters** as we used for the `show_message` command - **text_colour** and **back_colour**. Letters do not scroll, so there is no scroll_speed parameter.

+ Display the letter "J" in red on a white background.

+ Use the sleep function to display the letters of your name one at a time, each in a different colour, with a one second pause between each.

[[[generic-python-sleep]]]

<iframe src="https://trinket.io/embed/python/cae33bc332?toggleCode=true" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

+ Randomly generate a colour by using `randint` to choose a number between 0 and 255 for each of the RGB values making up a colour.

[[[generic-python-random]]]

```python
random_red = randint(0, 255)
random_green = randint(0, 255)
random_blue = randint(0, 255)

random_colour = (random_red, random_green, random_blue)
```

+ Use the `sense.clear()` at the end of your code to clear the LED matrix.
