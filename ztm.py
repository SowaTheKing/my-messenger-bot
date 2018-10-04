import requests


def ztm(stop_id):

    site = 'http://87.98.237.99:88/delays?stopId=' + str(stop_id)
    r = requests.get(site)
    p = r.json()
    text = ""
    text += str("Numer: " + str(p['delay'][0]['tripId']) + "\n")
    text += str("Czas przybycia: " + str(p['delay'][0]['estimatedTime']) + "\n")
    text += str("Nazwa lini:" + str(p['delay'][0]['headsign']))

    return text


def stop_name_to_id(name):
    switcher = {
        "Armii Krajowej"    :   36410,
        "Wrzeszcz PKP"      :   116,
        "Chelm Witosa"      :   129
    }
    return switcher.get(name, "Invalid Id")