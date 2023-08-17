from wifi_credentials import SSID, PASSWORD
import network
import time

CONNECTION_TIMEOUT = 5 # seconds

def connect_to_wifi():
    # Initialize the station interface
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        
        # Wait for the connection to complete
        start_time = time.monotonic()
        while not sta_if.isconnected():
            time.sleep(0.1)
            if time.monotonic() - start_time > CONNECTION_TIMEOUT:
                raise TimeoutError("Connection to WiFi timed out.")
    
    print('network config:', sta_if.ifconfig())
