## Detecting movement

The Sense HAT has an IMU (**I**nertial **M**easurement **U**nit) chip which includes a set of sensors that detect movement:

- A gyroscope (for detecting which way up the board is)
- An accelerometer (for detecting movement)
- A magnetometer (for detecting magnetic fields)

[[[rpi-sensehat-what-is-imu]]]

[[[generic-theory-pitch-roll-yaw]]]

+ Write a program to detect the current pitch, roll, and yaw. Run the program and move the Sense HAT around. Watch how the values change as the Sense HAT moves.

[[[rpi-sensehat-pitch-roll-yaw]]]


**Note:** When using the movement sensors, it is important to take frequent readings. If you take readings too slowly, for example by putting `time.sleep(0.5)` in your loop, you will see strange results. This is because the code needs lots of measurements in order to successfully combine the data coming from the gyroscope, accelerometer, and magnetometer.

### Which way up?

The `sense.get_accelerometer_raw()` method tells you the amount of G-force acting on each axis (x, y, z). If any axis has ±1G, then you know that axis is pointing downwards.

In this example, the amount of gravitational acceleration for each axis is extracted and is then rounded to the nearest whole number:

<iframe src="https://trinket.io/embed/python/f714d301d3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

+ Rotate the Sense HAT. You should see the values for `x` and `y` change between `-1` and `1`. If you place the Pi flat or turn it upside down, the value for the `z` axis will be `1` and then `-1`.

Use this information to set the orientation of the LED matrix.

+ Starting with the code above, add some code before the while loop to display the letter "J" on the LED matrix. Use the `show_letter` method you already learned about.

+ After the code which displays the G-force values for the x, y and z axes , add an if statement to check which way up the Sense HAT is pointing. Update the orientation of the display using the `set_rotation` method you learned about earlier. Here is some pseudo-code to get you started:

`If` the `x` axis has `-1` G, `rotate` `180` degrees
`Else if` the `y` axis has `1` G, `rotate` `90` degrees
`Else if` the `y` axis has `-1` G, `rotate` `270` degrees
`Else` `rotate` `0` degrees

--- collapse ---
---
title: Solution
---
<iframe src="https://trinket.io/embed/python/c2b483d8ea" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
--- /collapse ---

### Shake the board

If the board is only rotated, it will only ever experience 1 G of acceleration in any direction; if we were to shake it, the sensor would experience more than 1 G. We could then detect that rapid motion and respond.

For this program we will introduce the `abs()` function, which is not specific to the Sense HAT library but instead is part of standard Python. `abs()` gives us the absolute figure of a value and ignores whether the actual value is positive or negative — for example, `abs(1)` and `abs(-1)` both return `1`. This function is helpful because we don't care in which direction the sensor is being shaken, just that it is shaken.

```python
from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear()
```

This is a little tricky to emulate, so you should try this one using a real Sense HAT if you can. If you find the program is too sensitive (that is, it thinks the Sense HAT is constantly being shaken), try changing the value `1` to a larger value to raise the threshold of what is defined as a "shake".
