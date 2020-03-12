import os
import json

data = ''


def application(env, start_response):
    global data

    method = env['REQUEST_METHOD']
    uri = env['REQUEST_URI']
    path = env['PATH_INFO']

    if method == 'POST' and path == '/update':
        body = env['wsgi.input'].read()
        print('POST /update: body =', repr(body)[0:100])
        data = body
        assert isinstance(data, bytes)

        resp = (str(len(body)) + " bytes\n").encode("ascii")
        headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(resp))),
        ]
        start_response('201 Created', headers)
        return [resp]

    elif method == 'GET' and path == '/data':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [data]

    else:
        start_response('404 Not Found', [('Content-Type','text/plain')])
        return [b'sorry\n']
