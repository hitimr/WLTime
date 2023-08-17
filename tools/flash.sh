esptool --chip esp32 --port ${USB_PORT} --baud 460800 write_flash -z 0x1000 ${ESP_DIR}/os/esp32-20220117-v1.18.bin
