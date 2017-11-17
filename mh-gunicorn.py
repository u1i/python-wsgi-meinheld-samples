from meinheld import server

def application(environ, start_response):
    status = b'200 OK'
    res = b"Hello world!"
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(res)))]
    start_response(status, response_headers)
    return [res]
