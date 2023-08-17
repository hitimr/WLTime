from wl_request import get_rt_data

import network
import time

def connect_to_wifi(ssid, password):
    # Initialize the station interface
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        
        # Wait for the connection to complete
        while not sta_if.isconnected():
            time.sleep(1)
    
    print('network config:', sta_if.ifconfig())

def check_connection():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        print("Connected to WiFi!")
        return True
    else:
        print("Not connected to WiFi.")
        return False

# Replace 'your_ssid' and 'your_password' with your WiFi credentials
ssid = 'WLAN11831488'
password = 'h5Zbeexvkyhz'

connect_to_wifi(ssid, password)
check_connection()

data = get_rt_data()

print(data_datalist)