import requests, json
import sensor as s
from definitions import FanMode

def set_cool_temp(ip: str, cooltemp: int) -> bool:
    current_thermostat = s.get_thermostat_info(ip)
    response_data = { 'heattemp': current_thermostat['heattemp'], 'cooltemp': cooltemp }
    req = requests.post('http://{}/control'.format(ip), data=response_data)
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return False
    return True

def set_fan_mode(ip: str, fan_mode: FanMode) -> bool:
    current_thermostat = s.get_thermostat_info(ip)
    response_data = { 'heattemp': current_thermostat['heattemp'], 'cooltemp': current_thermostat['cooltemp'], 'fan': fan_mode.value }
    req = requests.post('http://{}/control'.format(ip), data=response_data)
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return False
    return True
