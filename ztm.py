import sys

import requests


def ztm(stop_id):
    log("[***] Obtaining ZTM for %")
    site = 'http://87.98.237.99:88/delays?stopId=' + str(stop_id)
    log(site)
    r = requests.get(site)
    p = r.json()
    text = ""
    text += str("Numer: " + str(p['delay'][0]['tripId']) + "\n")
    text += str("Czas przybycia: " + str(p['delay'][0]['estimatedTime']) + "\n")
    text += str("Nazwa lini:" + str(p['delay'][0]['headsign']))

    return text


def stop_name_to_id(name):
    log("Trying to assign %s to ID" % name)
    switcher = {
        "Armii Krajowej"    :   "36410",
        "Wrzeszcz PKP"      :   "116",
        "Chelm Witosa"      :   "129"
    }
    return switcher.get(name, "116")

def log(message):
    print str(message)
    sys.stdout.flush()

