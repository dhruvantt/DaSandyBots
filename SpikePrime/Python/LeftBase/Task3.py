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

# ------------------------
# Drive functions (A & E)
# ------------------------
async def drive_distance(distance_in_inch, velocity=360):
    degrees = inches_to_degrees(abs(distance_in_inch))
    steering = 0# straight

    speed = velocity if distance_in_inch > 0 else -velocity
    await motor_pair.move_for_degrees(
        motor_pair.PAIR_1,
        degrees,
        steering,
        velocity=speed
    )

async def attachment_right(angle_deg, velocity=200):
    TURN_FACTOR = 2.5
    degrees = int(abs(angle_deg) * TURN_FACTOR)

    speed = velocity if angle_deg > 0 else -velocity
    await motor.run_for_degrees(port.B, degrees, speed)

async def attachment_left(angle_deg, velocity=200):
    TURN_FACTOR = 2.5
    degrees = int(abs(angle_deg) * TURN_FACTOR)

    speed = velocity if angle_deg > 0 else -velocity
    await motor.run_for_degrees(port.F, degrees, speed)

async def right_turn(angle_deg, velocity=200):
    TURN_FACTOR = -2.5
    degrees = int(abs(angle_deg) * TURN_FACTOR)

    speed = velocity if angle_deg > 0 else -velocity
    await motor.run_for_degrees(port.E, degrees, speed)

async def left_turn(angle_deg, velocity=200):
    TURN_FACTOR = 2.5
    degrees = int(abs(angle_deg) * TURN_FACTOR)

    speed = velocity if angle_deg > 0 else -velocity
    await motor.run_for_degrees(port.A, degrees, speed)

# ------------------------
# Main program
# ------------------------
async def main():
    # Pair drive motors ONLY
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.A)
    
    await drive_distance(26, 5000)
    await left_turn(35, 5000)
    await drive_distance(4,5000)
    await left_turn(42,5000)
    await drive_distance(-12,5000)
    await right_turn(115,5000)
    await drive_distance(-25, 5000)
runloop.run(main())
