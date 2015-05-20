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
    | **back_colour** | The *back_colour* parameter alters the colour of the background and is specified as 3 values for Red,Green,Blue. Each value can be between 0 - 255, so [255,0,255] would be Red + Blue = Purple |

    So this program would display the text `Astro Pi is awesome!!` more slowly with the text in yellow **[255,255,0]** and the background in blue **[0,0,255]**.

    ```python
    from astro_pi import AstroPi
    ap = AstroPi()
    ap.show_message("Astro Pi is awesome!!",scroll_speed=0.05,text_colour=[255,255,0],back_colour=[0,0,255])
    ```
    You could also make the message repeat using a while loop like this:

    ```python
    from astro_pi import AstroPi
    ap = AstroPi()
    while True:
        ap.show_message("Astro Pi is awesome!!",scroll_speed=0.05,text_colour=[255,255,0],back_colour=[0,0,255])
    ```
2. The LED matrix can also display a single character rather than an entire message using the `ap.show_letter` function which also has some optional **parameters**.

    | Parameter | Effect |
    | :---: | :---: |
    | **scroll_speed** | The *scroll_speed* parameter affects how quickly the text moves on the screen the default value is 0.1. The bigger the number the **slower** the speed |
    | **text_colour** | The *text_colour* parameter alters the colour of the text and is specified as 3 values for Red,Green,Blue. Each value can be between 0 - 255, so [255,0,255] would be Red + Blue = Purple |
    | **back_colour** | The *back_colour* parameter alters the colour of the background and is specified as 3 values for Red,Green,Blue. Each value can be between 0 - 255, so [255,0,255] would be Red + Blue = Purple |

    So this program would display a single Red "J":

    ```python
    from astro_pi import AstroPi
    ap = AstroPi()
    ap.show_letter("J",text_colour=[255,0,0])
    ```

    Whilst this program would add the **sleep library** to display letters seperated by a brief pause.

    ```python
    from astro_pi import AstroPi
    import time

    ap = AstroPi()
    ap.show_letter("O",text_colour=[255,0,0])
    time.sleep(1)
    ap.show_letter("M",text_colour=[0,0,255])
    time.sleep(1)
    ap.show_letter("G",text_colour=[0,255,0])
    time.sleep(1)
    ap.show_letter("!",text_colour=[0,0,0],back_colour=[255,255,255])
    time.sleep(1)
    ap.clear()
    ```

### Ideas
 - Could you use the ideas used so far to tell a joke via the LED screen?
 - If your Astro Pi is connected to the internet you could use a twitter library to make it display incoming tweets!
