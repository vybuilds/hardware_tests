import lgpio
import time
import math

GPIO = 18

# Open GPIO chip
h = lgpio.gpiochip_open(0)

# Claim GPIO18 for PWM
lgpio.gpio_claim_output(h, GPIO)

# SG90 typical PWM:
# 50 Hz = 20 ms period
FREQUENCY = 50

# Conservative pulse range
MIN_US = 1000
MAX_US = 2000

def set_servo_us(pulse_us):
    """
    Set servo pulse width in microseconds.
    """

    duty_cycle = (pulse_us / 20000) * 100

    lgpio.tx_pwm(
        h,
        GPIO,
        FREQUENCY,
        duty_cycle
    )


def angle_to_us(angle):
    """
    Convert 0-180 degrees to pulse width.
    """

    return MIN_US + (angle / 180) * (MAX_US - MIN_US)


def move_smooth(start_angle, end_angle, duration):
    """
    Smooth acceleration and deceleration.
    """

    fps = 200
    steps = int(duration * fps)

    for i in range(steps + 1):

        t = i / steps

        # Cosine easing
        easing = (1 - math.cos(math.pi * t)) / 2

        angle = (
            start_angle
            + (end_angle - start_angle) * easing
        )

        pulse = angle_to_us(angle)

        set_servo_us(pulse)

        time.sleep(1 / fps)

try:

    print("Slow")
    move_smooth(10, 170, 5)
    move_smooth(170, 10, 5)

    time.sleep(1)

    print("Medium")
    move_smooth(10, 170, 3)
    move_smooth(170, 10, 3)

    time.sleep(1)

    print("Fast")
    move_smooth(10, 170, 1.5)
    move_smooth(170, 10, 1.5)

    time.sleep(1)

    print("Continuous oscillation")

    while True:
        move_smooth(10, 170, 3)
        move_smooth(170, 10, 3)


except KeyboardInterrupt:
    print("\nStopping servo")

finally:

    # Stop PWM
    lgpio.tx_pwm(h, GPIO, 0, 0)

    # Release GPIO
    lgpio.gpiochip_close(h)

    print("Servo stopped")
