#!/bin/bash
sudo chown hiti /dev/ttyUSB0

USB_PORT="/dev/ttyUSB0"  # Replace with your USB port
BAUD_RATE="115200"       # Set to your desired baud rate. 115200 is commonly used for ESP32.

# Loop through each .py file in the src directory
for file in src/*.py; do
    # Extract the filename without the path
    filename=$(basename "$file")
    # Upload the file
    echo "Uploading $filename"
    ampy -p "$USB_PORT" -b "$BAUD_RATE" put "$file" "$filename"
done

echo "Done uploading files"