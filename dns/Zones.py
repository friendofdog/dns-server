import glob
import json


def get_zones():
    jsonzone = {}
    zones = glob.glob('zones/*.zone')

    for zone in zones:
        with open(zone) as zonedata:
            data = json.load(zonedata)
            zonename = data['$origin']
            jsonzone[zonename] = data

    return jsonzone


class Zones:

    def __init__(self):
        self.zones = get_zones()
