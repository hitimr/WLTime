try:
    import requests
except ImportError:
    import urequests as requests

def generate_url():
    # website for stations: https://till.mabe.at/rbl/?line=508&station=62517

    # Base URL
    url = "http://www.wienerlinien.at/ogd_realtime/monitor?"

    url += "stopId=1718&" # WLB, 62 Aßmayergasse -> Baden Josephplatz 
    url += "stopId=1748&" # WLB, 62 Aßmayergasse -> Wien Oper
    url += "stopId=1692&" # 59A Aßmayergasse -> Bhf Meidling S U
    url += "stopId=1693&" # 59A Aßmayergasse -> Oper, Karlsplatz
    url += "stopId=1708&"

    # Options
    url += "activateTrafficInfo=stoerungkurz&"
    url += "activateTrafficInfo=stoerunglang&"

    # Sender
    url += "sender=hiti"

    return url

def request_data():
    r = requests.get(generate_url())
    return r.json()["data"]["monitors"]


def get_direction(line):
    b_direction = False

    # H-Directions go outward
    if line["direction"] == "H":
        b_direction = True

    # except for WLB. there its the other way around
    if line["name"] == "WLB":
        b_direction = not b_direction

    # return string
    if b_direction is True:
        return "outwards"
    else:
        return "center"

def to_series(line):
    ret = {
        "name": line["name"],
        "countdown": line["departures"]["departure"][0]["departureTime"]["countdown"],
        "outwards": get_direction(line)
    }
    return ret

def get_rt_data():
    data_list = []
    data = request_data()
    for monitor in data:
        data = to_series(monitor["lines"][0])
        data_list.append(data)

    return data_list
