import sys
import time
import http.client as httplib

class MyHTTPConnection(httplib.HTTPConnection):
    def close(self):
        print('closing', repr(self))
        super().close()


#conn = httplib.HTTPConnection("localhost", 7020)
conn = MyHTTPConnection("localhost", 7020)
conn.set_debuglevel(1)
body = 'hello\n'
print('send req 1')
conn.request(
    'POST',
    f'/update',
    headers={'content-type': 'text/plain'},
    body=body)
print('get resp 1')
resp = conn.getresponse()
print('resp 1:', resp.status, resp.reason)
print('body 1:', resp.read())

#time.sleep(1)
#conn = httplib.HTTPConnection("localhost", 7020)
print('send req 2')
conn.request(
    'GET',
    f'/data')
resp = conn.getresponse()
print('resp 2:', resp.status, resp.reason)
print('body 2:', resp.read())
