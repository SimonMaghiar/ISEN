import http.client

def HTTP_Pong(host, SSL = False):
    conn = http.client.HTTPConnection(host) if not SSL else http.client.HTTPSConnection(host)
    conn.request("GET", "/")
    res = conn.getresponse()
    print(res.status, res.reason)