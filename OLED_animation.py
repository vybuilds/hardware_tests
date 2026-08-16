import time
import board
import busio
import displayio
import terminalio

from i2cdisplaybus import I2CDisplayBus
from adafruit_display_text import label
import adafruit_displayio_sh1106

# --------------------------------------------------
# OLED SETUP
# --------------------------------------------------

displayio.release_displays()

i2c = busio.I2C(board.SCL, board.SDA)

display_bus = I2CDisplayBus(
    i2c,
    device_address=0x3C
)

display = adafruit_displayio_sh1106.SH1106(
    display_bus,
    width=128,
    height=64,
    colstart=2
)

# --------------------------------------------------
# CREATE TEXT
# --------------------------------------------------

def create_text(text, x, y, scale=1):

    text_label = label.Label(
        terminalio.FONT,
        text=text,
        color=0xFFFFFF,
        x=x,
        y=y,
        scale=scale
    )

    return text_label

# --------------------------------------------------
# LOVE ANIMATION
# --------------------------------------------------

try:

    while True:

        # ------------------------------
        # I LOVE YOU
        # ------------------------------

        group = displayio.Group()

        group.append(
            create_text(
                "I LOVE YOU",
                x=32,
                y=32,
                scale=1
            )
        )
        
        display.root_group = group

        time.sleep(1)


        # ------------------------------
        # I ♥ YOU
        # ------------------------------

        group = displayio.Group()

        group.append(
            create_text(
                "I",
                x=45,
                y=32,
                scale=2
            )
        )

        group.append(
            create_text(
                "♥",
                x=60,
                y=32,
                scale=2
            )
        )
        group.append(
            create_text(
                "YOU",
                x=78,
                y=32,
                scale=2
            )
        )

        display.root_group = group

        time.sleep(0.7)


        # ------------------------------
        # HEART AGAIN
        # ------------------------------

        group = displayio.Group()

        group.append(
            create_text(
                "I",
                x=45,
                y=32,
                scale=2
            )
        )

        group.append(
            create_text(
                "♥",
                x=60,
                y=32,
                scale=3
            )
        )

        group.append(
            create_text(
                "YOU",
                x=82,
                y=32,
                scale=2
            )
        )

        display.root_group = group

        time.sleep(0.25)

        # ------------------------------
        # BACK TO NORMAL
        # ------------------------------

        group = displayio.Group()

        group.append(
            create_text(
                "I LOVE YOU",
                x=32,
                y=32,
                scale=1
            )
        )

        display.root_group = group

        time.sleep(0.8)

except KeyboardInterrupt:

    display.root_group = displayio.Group()

    print("\nLove animation stopped.")
