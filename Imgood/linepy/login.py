import json, requests
from .server import Server


class Login(object):
    def __init__(self):
        self.set = json.loads(open('Data/settings.json','r').read())
        self.server = Server()

    def logqr(self,cert=None):
        host = "https://api.imjustgood.com/lineqr"
        headers = {
          "apikey": "{}".format(self.set["apikey"]),
          "appName": "{}".format(self.server.APP_NAME),
          "sysName": "{}".format(self.server.SYSTEM_NAME),
          "cert": cert,
          "User-Agent": "Justgood/5.0"
        }
        main = json.loads(requests.get(host,headers=headers).text)
        if main["status"] == 200:
           qrlink = main["result"]["qr"]
           print("Open this link on your LINE for smartphone in 2 minutes\n" + qrlink)
           data = json.loads(requests.get(main["result"]["callback"]["pin"],headers=headers).text)
           if data["status"] == 200:
              print("Input Your PIN: " + data["result"]["pin"])
           data = json.loads(requests.get(main["result"]["callback"]["token"],headers=headers).text)
           if data["status"] == 200:
              print("Token: " + data["result"]["token"])
              print("Cert : " + data["result"]["cert"])
              return data["result"]["token"]
           else:
             print(main["message"])
        else:
           print(main["message"])
