import range_finder
import motor_functions

motor_functions.startup_motor()
range_finder.startup_lidar()

for i in range(120):
    motor_functions.change_position(0.1, 0.1)
    distance = range_finder.distance()
    print(distance)