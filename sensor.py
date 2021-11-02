import requests, json

def get_sensor_readings(thermostat_ip: str) -> list:
    req = requests.get('http://{}/query/sensors'.format(thermostat_ip))
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return []
    return req.json()['sensors']

get_thermostat_info(thermostat_ip: str) -> dict:
    req = requests.get)'http://{}/query/info'.format(thermostat_ip))
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return {}
    return req.json()

