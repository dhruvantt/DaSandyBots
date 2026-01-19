import motor
import motor_pair
import runloop
from hub import port
import math

# ------------------------
# Robot / Wheel settings
# ------------------------
WHEEL_DIAMETER_INCH = 2.2
WHEEL_CIRCUMFERENCE = math.pi * WHEEL_DIAMETER_INCH


def inches_to_degrees(distance_inch):
    rotations = distance_inch / WHEEL_CIRCUMFERENCE
    return int(rotations * 360)

def turn_degrees(angle_degree):
    return int(angle_degree * 2.5)

# Wheel configurations
async def move_forward(distance_in_inches, velocity = 360):
    await move_wheels(distance_in_inches, velocity)

async def move_backward(distance_in_inches, velocity = 360):
    await move_wheels(distance_in_inches, -velocity)

async def move_wheels(distance_in_inches, velocity = 360):
    degrees = inches_to_degrees(abs(distance_in_inches))
    steering = 0
    await motor_pair.move_for_degrees(
        motor_pair.PAIR_1,
        degrees,
        steering,
        velocity = velocity
    )

async def turn_right_wheel(angle_degree, velocity):
    await turn_wheel(port.E, -angle_degree, velocity)

async def turn_left_wheel(angle_degree, velocity):
    await turn_wheel(port.A, angle_degree, velocity)

async def turn_wheel(port, angle_degree, velocity):
    await motor.run_for_degrees(port, turn_degrees(angle_degree), velocity)

# Attachment configurations
async def move_right_attachment(angle_degree, velocity, move_up = True):
    await move_attachment(port.B, angle_degree, velocity, move_up)

async def move_left_attachment(angle_degree, velocity, move_up = True):
    await move_attachment(port.F, angle_degree, velocity, move_up)

async def move_attachment(port, angle_degree, velocity, move_up = True):
    if move_up:
        angle_degree = angle_degree
    else:
        angle_degree = -angle_degree

    await motor.run_for_degrees(port, turn_degrees(angle_degree), velocity)


# ------------------------
# Main program
# ------------------------
async def main():
    # Pair drive motors ONLY
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.A)

    

    await move_forward(26, 5000)
    await turn_left_wheel(35, 5000)
    await move_forward(4,5000)
    await turn_left_wheel(42,5000)
    await move_backward(12,5000)
    await turn_right_wheel(115,5000)
    await move_backward(25, 5000)
runloop.run(main())

