import requests, json
# "https://shelly-21-eu.shelly.cloud/device/status"
def checkCloudStatus(url, devid, authkey):
    j = json.loads(getData(url, devid, authkey))
    if (j["data"]["online"] == True):
        return True
    else:
        return False


def getData(url, devid, authkey):
    if(checkCloudStatus(url, url, devid)):
        data = {'id': devid, 'auth_key': authkey}
        reply = requests.post(url, data=data)
        return reply.content
    else:
        return "Not connected"


def getEnergyTotal(url, devid, authkey):
    if (checkCloudStatus(url, url, devid)):
        j = json.loads(getData(url, devid, authkey))
        return j["data"]["device_status"]["switch:0"]["aenergy"]["total"]
    else:
        return "Not connected"
