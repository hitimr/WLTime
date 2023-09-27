from wl_request import get_rt_data
from wifi import connect_to_wifi
import time
from lcd_i2c import LCD
from machine import I2C, Pin

I2C_ADDR = 0x27  # DEC 39, HEX 0x27
NUM_COLS = 20
NUM_ROWS = 4
UPDATE_INTERVAL = 30  # seconds


di_btn_sens = Pin(34, Pin.IN)
do_keep_alive = Pin(23, Pin.OUT)
do_keep_alive.value(1)


# define custom I2C interface, default is 'I2C(0)'
# check the docs of your device for further details and pin infos
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=800000)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()
lcd.clear()

lcd.print("Connecting to WiFi..")
connect_to_wifi()
lcd.print("Connected to WiFi!")


def print_rt_data():
    data = get_rt_data()

    outwards_list = []
    center_list = []

    for item in data:
        if item["direction"] == "outwards":
            outwards_list.append(item)
        elif item["direction"] == "center":
            center_list.append(item)

    # Sort each list by countdown
    outwards_list = sorted(outwards_list, key=lambda x: int(x["countdown"]))
    center_list = sorted(center_list, key=lambda x: int(x["countdown"]))

    for i in range(3):  # Display the first 3 lines of data for each direction
        # Initialize an empty 20-character string
        formatted_str = " " * 20

        # Add data for the center direction
        if i < len(center_list):
            center_name = center_list[i]["name"]
            center_countdown = str(center_list[i]["countdown"])
            formatted_str = formatted_str[:0] + center_name + formatted_str[len(center_name) :]
            formatted_str = formatted_str[:5] + center_countdown + formatted_str[5 + len(center_countdown) :]

        # Add data for the outward direction
        if i < len(outwards_list):
            outwards_name = outwards_list[i]["name"]
            outwards_countdown = str(outwards_list[i]["countdown"])
            formatted_str = formatted_str[:9] + outwards_name + formatted_str[9 + len(outwards_name) :]
            formatted_str = formatted_str[:15] + outwards_countdown + formatted_str[15 + len(outwards_countdown) :]

        lcd.set_cursor(0, i)
        lcd.print(formatted_str)


lcd.print("Fetching initial data..")
print_rt_data()

iter = 1
max_iter = 10

while True:
    if iter % UPDATE_INTERVAL == 0:
        print_rt_data()

    do_keep_alive.value(iter % 2)
    # if iter >= max_iter:
    #     do_keep_alive.value(0)

    lcd.set_cursor(0, 4)
    lcd.print(" " * 20)
    lcd.set_cursor(0, 4)
    lcd.print(f"Next update: {UPDATE_INTERVAL - iter}s")
    iter += 1
    time.sleep(1)
