import http.client as client

con = client.HTTPConnection('127.0.0.1' , 8000)

con.request("GET", "/test")
