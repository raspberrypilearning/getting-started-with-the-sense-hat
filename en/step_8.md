## Sensing the environment

The Sense HAT has a set of environmental sensors for detecting the conditions around it. It can detect pressure, temperature and humidity.

[[[rpi-sensehat-pressure]]]

[[[rpi-sensehat-temperature]]]

[[[rpi-sensehat-humidity]]]

+ Using these, we could create a simple scrolling text display which could keep people informed about current conditions.

<iframe src="https://trinket.io/embed/python/a246815131" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

+ According to [online documentation](http://wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf){:target="_blank"}, the International Space Station maintains these conditions at the following levels:

- Temperature: 18.3 - 26.7 Celsius
- Pressure: 979 - 1027 millibars
- Humidity: around 60%

You could use an `if` statement in your code to check these conditions, and set a background colour for the scroll:

```python
if t > 18.3 and t < 26.7:
    bg = (0, 100, 0) # green
else:
    bg = (100, 0, 0) # red
```

<iframe src="https://trinket.io/embed/python/2f03745830" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
