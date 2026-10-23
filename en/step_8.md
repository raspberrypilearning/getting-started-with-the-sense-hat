## Sensing the environment

The Sense HAT has a set of environmental sensors for detecting the surrounding conditions; it can measure pressure, temperature, and humidity.

[[[rpi-sensehat-pressure]]]

[[[rpi-sensehat-temperature]]]

[[[rpi-sensehat-humidity]]]

[[[rpi-sensehat-colour]]]

+ Create a scrolling text display which keeps people informed about the current pressure, temperature, and humidity readings. You can use the scrolling text display code you wrote in the 'Displaying text' step to help you.

--- collapse ---
---
title: Solution
---

```python
from sense_hat import SenseHat
sense = SenseHat()

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05)
```

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-step-8-a" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-step-8-a){:target="_blank"}

--- /collapse ---

According to [online documentation](http://wsn.spaceflight.esa.int/docs/Factsheets/30%20ECLSS%20LR.pdf){:target="_blank"}, the International Space Station maintains these conditions at the following levels:

Temperature: 18.3-26.7 Celsius

Pressure: 979-1027 millibars

Humidity: around 60%

+ Define variables for the colours green (0, 255, 0) and red (255, 0, 0).

+ Use an if statement in your code to check whether the temperature is between 18.3 and 26.7 degrees Celsius.

[[[generic-python-conditional-selection-with-boolean]]]

+ If the temperature is within this normal range, display the scrolling message with a green background. If not, display a red background.

--- collapse ---
---
title: Solution
---
```python
from sense_hat import SenseHat
sense = SenseHat()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  if t > 18.3 and t < 26.7:
    bg = green
  else:
    bg = red
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg)
```

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/getting-started-with-the-sense-hat-step-8-b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The Code Editor shows the Sense HAT on its side, so the picture is turned a quarter-turn clockwise.

[Open this code in the Code Editor](https://editor.raspberrypi.org/en/projects/getting-started-with-the-sense-hat-step-8-b){:target="_blank"}

--- /collapse ---

+ Add more if statements to test for normal pressure and humidity conditions as well.
