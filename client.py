import http.client as client
from time import sleep

con = client.HTTPConnection('127.0.0.1' , 8000)

try:
    while True:
        con.request("GET", "/test")
        res = con.getresponse()
        print(res.getheaders())
        sleep(2.5)
except KeyboardInterrupt:
    con.close()
    print("Closing...")

