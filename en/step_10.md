## Using the joystick
You can detect when the Sense HAT's joystick is pressed, held, and released in five different directions: up, down, left, right, and middle.

[[[rpi-sensehat-joystick]]]

+ Depending on which way the joystick was pressed, display one of the letters U, D, L, R or M on the LED matrix.

--- collapse ---
---
title: Solution
---
<iframe src="https://trinket.io/embed/python/e92f522f64" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /collapse ---

You can also call a function whenever the Sense HAT's joystick is moved in a particular direction.

[[[rpi-python-sensehat-joystick-event-functions]]]

+ Create functions to fill the LED matrix with four different colours. Add triggers to call one function for each possible direction in which the joystick can be pressed. 

--- collapse ---
---
title: Solution
---
<iframe src="https://trinket.io/embed/python/f937b52806" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

--- /collapse ---
