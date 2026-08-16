import board
import busio
import displayio
import i2cdisplaybus
import adafruit_displayio_sh1106

displayio.release_displays()

i2c = busio.I2C(board.SCL, board.SDA)

display_bus = i2cdisplaybus.I2CDisplayBus(
    i2c,
    device_address=0x3C
)

display = adafruit_displayio_sh1106.SH1106(
    display_bus,
    width=128,
    height=64,
    colstart = 2
)

# Create a 1-bit bitmap
bitmap = displayio.Bitmap(128, 64, 2)

# Draw a border
# Draw within the 128 visible columns

for x in range(128):
    bitmap[x, 0] = 1
    bitmap[x, 63] = 1

for y in range(64):
    bitmap[0, y] = 1
    bitmap[127, y] = 1

for y in range(64):
    bitmap[64, y] = 1

for x in range(128):
    bitmap[x, 32] = 1

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

print("Pattern test running. Press Ctrl+C to stop.")

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
