from wl_request import get_rt_data
from wifi import connect_to_wifi

connect_to_wifi()

data = get_rt_data()

print(data)