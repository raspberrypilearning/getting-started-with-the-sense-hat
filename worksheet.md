# Getting Started with Astro Pi

![Astro Pi banner](cover.png)

Astro Pi is a add on board for the Raspberry Pi Computer which adds the ability to sense all kinds of things and output information using a built in 8x8 LED matrix.
You can find out more about Astro Pi by following the [Astro Pi Guide](https://github.com/raspberrypilearning/guides/blob/master/astro-pi/README.md), this will show you how to connect and test your Astro Pi board.

Once you are set up and have run your first program using the guide you can begin to experiment further using this worksheet. In order to write your programs you will need to boot your Raspberry Pi up to the desktop and start a new program in IDLE3. (Like you did in the guide)

## Displaying Text
When following the guide you will have written a sample program which scrolls text across the LED matrix, the program contains two crucial lines, which import the Astro Pi software an create an `ap` object which represents the Astro Pi board.

    ```python
        from astro_pi import AstroPi
        ap = AstroPi()
    ```

The third line is the one that starts to make the Astro Pi do something:

    ```python
        ap.show_message("Hello my name is Tim Peake")
    ```

You have probably already discovered that you you can easily change the message to your own text, however there are more things that we can do.

1. We can expand the ap.show_message command to include some extra **parameters** which will change the behaviour of the message.

    | Parameter | Effect |
    | :---: | :---: |
    | **scroll_speed** | The *scroll_speed* parameter affects how quickly the text moves on the screen the default value is 0.1. The bigger the number the **slower** the speed |
    | **text_colour** | The *text_colour* parameter alters the colour of the text and is specified as 3 values for Red,Green,Blue. Each value can be between 0 - 255, so [255,0,255] would be Red + Blue = Purple |
