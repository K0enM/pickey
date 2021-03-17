import http.client as client
from time import sleep

con = client.HTTPConnection('mod7-pickey.herokuapp.com' , 80)

try:
    while True:
        con.request("GET", "/")
        res = con.getresponse()
        print(res.getheaders())
        sleep(2.5)
except KeyboardInterrupt:
    con.close()
    print("Closing...")

