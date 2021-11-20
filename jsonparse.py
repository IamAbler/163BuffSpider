import getinfo
import json


def jsonparse(getinfo):
    info = json.loads(getinfo)
    return info
