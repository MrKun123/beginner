import json
import time
import requests
from setup import *


class getter():
    def __init__(self):
        pass

    def getInfo(self,i):
        # 配置信息在setup

        param = {
            "f": "json",
            "objectIds": str(i),
            "outFields": "POINT_X,POINT_Y,交通位置,利用现状,地质工作程,矿产地名称,矿床成因类,矿种,规模,OBJECTID",
            "outSR": "102100",
            "returnM": "true",
            "returnZ": "true",
            "spatialRel": "esriSpatialRelIntersects",
            "where": "1=1",
        }
        res = requests.get(url, params=param, headers=getHeaders()).json()

        return res




if __name__ == '__main__':
    getter = getter()
    n = 73124
    for i in range(n,n+1):
        res = getter.getInfo(i)
        res = res["features"][0]["attributes"]
        print(res)
