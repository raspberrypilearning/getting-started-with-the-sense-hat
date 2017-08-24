## Sensing the environment

The Sense HAT has a set of environmental sensors for detecting the conditions around it. It can detect:

- Pressure
- Temperature
- Humidity

We can collect these readings using three simple methods:

- `sense.get_temperature()` - this will return the temperature in Celsius.
- `sense.get_pressure()` - this will return the pressure in millibars.
- `sense.get_humidity()` - this will return the humidity as a percentage.

- Using these, we could create a simple scrolling text display which could keep people informed about current conditions.

    ```python
    from sense_hat import SenseHat
    sense = SenseHat()

    while True:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

        msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)

        sense.show_message(msg, scroll_speed=0.05)
    ```

- Click **File** and **Save As**, give your program a name e.g. [`env.py`](resources/env.py), then press `F5` to run.

    <iframe src="https://trinket.io/embed/python/a246815131" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

- You could now use some colour to let the astronauts know whether conditions are within sensible ranges.

    According to some [online documentation](http://wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf), the International Space Station maintains these conditions at the following levels:

    - Temperature (18.3 - 26.7 Celsius)
    - Pressure (979 - 1027 millibars)
    - Humidity (around 60%)

    You could use an `if` statement in your code to check these conditions, and set a background colour for the scroll:

    ```python
    if t > 18.3 and t < 26.7:
        bg = (0, 100, 0) # green
    else:
        bg = (100, 0, 0) # red
    ```

    Your complete program would look like this:

    ```python
    from sense_hat import SenseHat
    sense = SenseHat()

    while True:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

        if t > 18.3 and t < 26.7:
            bg = (0, 100, 0)  # green
        else:
            bg = (100, 0, 0)  # red

        msg = "Temperature = {0}, Pressure = {1}, Humidity - {2}".format(t, p, h)

        sense.show_message(msg, scroll_speed=0.05, back_colour=bg)
    ```

- Click **File** and **Save As**, give your program a name e.g. [`scrolling_env.py`](resources/scrolling_env.py), then press `F5` to run.

    <iframe src="https://trinket.io/embed/python/2f03745830" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Ideas

- Currently, the scrolling program only warns about abnormal temperature. Can you add the same behaviour for pressure and humidity?
- You could create a simple graphical thermometer which outputs different colours or patterns depending on the temperature.





