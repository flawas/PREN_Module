import requests
from requests.structures import CaseInsensitiveDict

def checkAvailability(url, headers):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        return True
    except requests.exceptions.Timeout:
        return False


def checkData(url, headers, token, time, config):
    headers = CaseInsensitiveDict()

    headers["Content-Type"] = "application/json"
    headers["Auth"] = token
    data = {"time": time,
            "config": config}
    resp = requests.post(url, headers=headers, json=data)
    print("Dataverify request " + str(resp.status_code))