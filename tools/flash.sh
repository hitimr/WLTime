sudo chown hiti /dev/ttyUSB0
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 bin/esp32-20230426-v1.20.0.bin