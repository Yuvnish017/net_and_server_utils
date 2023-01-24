import urllib
from urllib.request import urlopen
import urllib.request
import urllib.parse
from urllib.error import HTTPError


class HTTPClientServices:
    def __init__(self, url):
        self.url = url

    def read_url(self, num_bytes):
        with urlopen(self.url) as webdata:
            print(webdata.read(num_bytes).decode('utf-8'))

    def get_request_to_url(self, data):
        params = urllib.parse.urlencode(data)
        query_url = self.url + '?%s'%params
        with urlopen(query_url) as webdata:
            print(webdata.read().decode('utf-8'))

    def post_request_to_url(self, data):
        data = urllib.parse.urlencode(data)
        data = data.encode('ascii')
        with urlopen(self.url, data) as webdata:
            print(webdata.read().decode('utf-8'))

