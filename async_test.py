import config
from base64 import b64encode
import grequests


class Test:
    def __init__(self, username, password, urls):
        self.username = username
        self.password = password
        self.urls = urls
        credentials = b64encode(bytes(username + ':' + password, 'utf-8')).decode('ascii')
        self.headers = {'Authorization': 'Basic %s' % credentials}

    @staticmethod
    def exception(self, request, exception):
        print("Problem: {}: {}".format(request.url, exception))

    def async_run(self):
        rs = (grequests.get(u, headers=self.headers) for u in self.urls)
        response = grequests.map(rs, exception_handler=self.exception, size=10)
        return response


if __name__ == '__main__':
    test = Test(config.username, config.password, config.paths)
    result = test.async_run()
