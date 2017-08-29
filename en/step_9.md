## Detecting movement

The Sense HAT has a set of sensors that can detect movement. It has an IMU (inertial measurement unit) chip which includes:

- A gyroscope (for detecting which way up the board is)
- An accelerometer (for detecting movement)
- A magnetometer (for detecting magnetic fields)

[[[rpi-sensehat-what-is-imu]]]

[[[generic-theory-pitch-roll-yaw]]]

+ You can explore these values with a simple program:

```python
from sense_hat import SenseHat

sense = SenseHat()

while True:
	orientation = sense.get_orientation()
	pitch = orientation['pitch']
	roll = orientation['roll']
	yaw = orientation['yaw']
	print("pitch={0}, roll={1}, yaw={2}".format(pitch, roll, yaw))
```

<iframe src="https://trinket.io/embed/python/883c34059d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Note: When using the movement sensors it is important to poll them often in a tight loop. If you poll them too slowly, for example with `time.sleep(0.5)` in your loop, you will see strange results. This is because the code behind needs lots of measurements in order to successfully combine the data coming from the gyroscope, accelerometer and magnetometer.**

+ You can click and drag around the Sense HAT in the emulator to see the values change.

+ Another way to detect orientation is to use the `sense.get_accelerometer_raw()` method which tells you the amount of g-force acting on each axis. If any axis has ±1g then you know that axis is pointing downwards.

In this example, the amount of gravitational acceleration for each axis (x, y, and z) is extracted and is then rounded to the nearest whole number:

```python
from sense_hat import SenseHat

sense = SenseHat()

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)

	print("x={0}, y={1}, z={2}".format(x, y, z))
```

<iframe src="https://trinket.io/embed/python/f714d301d3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

As you rotate the Sense HAT, you should see the values for x and y change between -1 and 1. If you place the Pi flat or turn it upside down, the z axis will be 1 and then -1.

- If we know which way round the Raspberry Pi is, then we can use that information to set the orientation of the LED matrix. First you would display something on the matrix, then continually check which way round the board is, and use that to update the orientation of the display.

```python
from sense_hat import SenseHat

sense = SenseHat()

sense.show_letter("J")

while True:
	x = sense.get_accelerometer_raw()['x']
	y = sense.get_accelerometer_raw()['y']
	z = sense.get_accelerometer_raw()['z']

	x = round(x, 0)
	y = round(y, 0)

	if x == -1:
		sense.set_rotation(180)
	elif y == 1:
		sense.set_rotation(90)
	elif y == -1:
		sense.set_rotation(270)
	else:
		sense.set_rotation(0)
```


<iframe src="https://trinket.io/embed/python/ecd677033b" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In this program you are using an `if, elif, else` structure to check which way round the Raspberry Pi is. The `if` and `elif` test three of the orientations, and if the orientation doesn't match any of these then the program assumes it is the "right" way round. By using the `else` statement we also catch all those other situations, like when the board is at 45 degrees or sitting level.

- If the board is only rotated, it will only experience 1 g of acceleration in any direction; if we were to shake it, the sensor would experience more than 1 g. We could then detect that rapid motion and respond. For this program we will introduce the `abs()` function which is not specific to the Sense HAT library and is part of standard Python. `abs()` gives us the size of a value and ignores whether the value is positive or negative. This is helpful as we don't care which direction the sensor is being shaken, just that it is shaken.

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

- This is a little tricky to emulate, so you should try this one using IDLE and a real Sense HAT. Click **File** and **Save As**, give your program a name e.g. [`shake.py`](resources/shake.py), then press `F5` to run.

You might find this is quite sensitive, but you could change the value from 1 to a higher number.
