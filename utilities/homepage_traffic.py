from pprint import pprint

import requests
from browsermobproxy import Server


class BMPClient:
    server = Server("D:\\UI_Automation_Rapyuta\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")


    def start_server(self):
        self.server.start()
        client = self.server.create_proxy(params={'trustAllServers':'true'})
        client.new_har("noogle")
        print(client.proxy)
        return client

    def stop_server(self, client):
        pprint(client.har)
        self.server.stop()

