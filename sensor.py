import requests, json
from definitions import FanState

def get_sensor_readings(thermostat_ip: str) -> list:
    req = requests.get('http://{}/query/sensors'.format(thermostat_ip))
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return []
    return req.json()['sensors']

def get_thermostat_info(thermostat_ip: str) -> dict:
    req = requests.get('http://{}/query/info'.format(thermostat_ip))
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return {}
    return req.json()

def get_fan_state(ip: str) -> str:
    info = get_thermostat_info(ip)
    return FanState(info['fanstate']).name
