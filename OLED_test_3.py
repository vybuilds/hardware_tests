import time
import board
import busio
import displayio

from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_sh1106


displayio.release_displays()

i2c = busio.I2C(board.SCL, board.SDA)

display_bus = I2CDisplayBus(
    i2c,
    device_address=0x3C
)

display = adafruit_displayio_sh1106.SH1106(
    display_bus,
    width=128,
    height=64
)

bitmap = displayio.Bitmap(128, 64, 2)

palette = displayio.Palette(2)
palette[0] = 0x000000
palette[1] = 0xFFFFFF

tilegrid = displayio.TileGrid(
    bitmap,
    pixel_shader=palette
)

group = displayio.Group()
group.append(tilegrid)

display.root_group = group


# Draw four lines at known coordinates
for y in range(64):
    bitmap[0, y] = 1
    bitmap[1, y] = 1

    bitmap[64, y] = 1

    bitmap[126, y] = 1
    bitmap[127, y] = 1


print("Mapping test running.")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    pass
