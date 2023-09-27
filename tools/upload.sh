#!/bin/bash
sudo chown "$USER" /dev/ttyUSB0

USB_PORT="/dev/ttyUSB0"  # Replace with your USB port
BAUD_RATE="115200"       # Set to your desired baud rate. 115200 is commonly used for ESP32.

# Check if an argument is passed, and set the source directory accordingly
SRC_DIR="src"
if [ "$#" -eq 1 ]; then
    SRC_DIR="$1"
fi

# Loop through each .py file in the source directory
for file in "$SRC_DIR"/*.py; do
    # Extract the filename without the path
    filename=$(basename "$file")
    # Upload the file
    echo "Uploading $filename"
    ampy -p "$USB_PORT" -b "$BAUD_RATE" put "$file" "$filename"
done

echo "Done uploading files"
