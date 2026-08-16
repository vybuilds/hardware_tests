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
# HELPER
# --------------------------------------------------

def show_text(text, x=5, y=32):
    group = displayio.Group()

    text_label = label.Label(
        terminalio.FONT,
        text=text,
        color=0xFFFFFF,
        x=x,
        y=y
    )

    group.append(text_label)
    display.root_group = group

# --------------------------------------------------
# TEST 1 — TEXT
# --------------------------------------------------

show_text("Hello Raspberry Pi!")

time.sleep(3)


# --------------------------------------------------
# TEST 2 — NUMBERS
# --------------------------------------------------

show_text("1234567890")

time.sleep(3)

# --------------------------------------------------
# TEST 3 — SYMBOLS
# --------------------------------------------------

show_text("! @ # $ % & * + - =")

time.sleep(3)


# --------------------------------------------------
# TEST 4 — MULTIPLE LINES
# --------------------------------------------------

group = displayio.Group()

lines = [
    "SG90 / MG996R",
    "OLED TEST",
    "I2C: 0x3C",
    "128 x 64",
]

for i, text in enumerate(lines):

    text_label = label.Label(
        terminalio.FONT,
        text=text,
        color=0xFFFFFF,
        x=5,
        y=8 + i * 16
    )

    group.append(text_label)

display.root_group = group

time.sleep(3)

# --------------------------------------------------
# TEST 5 — BORDER
# --------------------------------------------------

bitmap = displayio.Bitmap(128, 64, 2)

for x in range(128):
    bitmap[x, 0] = 1
    bitmap[x, 63] = 1

for y in range(64):
    bitmap[0, y] = 1
    bitmap[127, y] = 1

palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xFFFFFF

tile_grid = displayio.TileGrid(
    bitmap,
    pixel_shader=palette
)

group = displayio.Group()
group.append(tile_grid)

display.root_group = group

time.sleep(3)

# --------------------------------------------------
# TEST 6 — CROSSHAIR
# --------------------------------------------------

bitmap = displayio.Bitmap(128, 64, 2)

for x in range(128):
    bitmap[x, 32] = 1

for y in range(64):
    bitmap[64, y] = 1

palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xFFFFFF

tile_grid = displayio.TileGrid(
    bitmap,
    pixel_shader=palette
)

group = displayio.Group()
group.append(tile_grid)

display.root_group = group

time.sleep(3)

# --------------------------------------------------
# TEST 7 — ANIMATION
# --------------------------------------------------

print("Starting animation...")

bitmap = displayio.Bitmap(128, 64, 2)

palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xFFFFFF

tile_grid = displayio.TileGrid(
    bitmap,
    pixel_shader=palette
)

group = displayio.Group()
group.append(tile_grid)

display.root_group = group

try:

    for x in range(128):

        bitmap.fill(0)

        # Vertical moving line
        for y in range(64):
            bitmap[x, y] = 1

        time.sleep(0.02)

except KeyboardInterrupt:

    pass


# --------------------------------------------------
# DONE
# --------------------------------------------------

bitmap.fill(0)

show_text("OLED TEST DONE")

print("OLED tests completed.")
