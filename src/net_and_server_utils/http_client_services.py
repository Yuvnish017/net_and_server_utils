import urllib
from urllib.request import urlopen


class HTTPClientServices:
    def __init__(self, url):
        self.url = url

    def read_url(self, num_bytes):
        with urlopen(self.url) as webdata:
            print(webdata.read(num_bytes).decode('utf-8'))
