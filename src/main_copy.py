from wl_request import get_rt_data
from wifi import connect_to_wifi

from lcd_i2c import LCD
from machine import I2C, Pin
import const as Const

I2C_ADDR = 0x27  # DEC 39, HEX 0x27
NUM_COLS = 20
NUM_ROWS = 4

# define custom I2C interface, default is 'I2C(0)'
# check the docs of your device for further details and pin infos
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=800000)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()


offsets = [0, 0x3C, 0x14, 0x54]

for i, val in enumerate(offsets):
    lcd._command(value=(Const.LCD_SETDDRAMADDR | val))
    lcd.print(f"{i}")
