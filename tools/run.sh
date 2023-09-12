#!/bin/bash
sudo chown hiti /dev/ttyUSB0
USB_PORT="/dev/ttyUSB0" # Replace with your USB port
BAUD_RATE="115200"      # Set to your desired baud rate. 115200 is commonly used for ESP32.

ampy -p "$USB_PORT" -b "$BAUD_RATE" run src/main.py
