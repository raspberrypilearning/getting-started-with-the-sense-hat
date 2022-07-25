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

<iframe src="https://trinket.io/embed/python/e3f7d0412c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

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
<iframe src="https://trinket.io/embed/python/875ceb5402" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /collapse ---

+ Add more if statements to test for normal pressure and humidity conditions as well.
