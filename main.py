from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
import json
import os

import json

app = FastAPI()




@app.get("/ip1")
def do_ping_sweep(ip,num):
    #ip="192.168.1.1"
    num=int(num)
    resu=""
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    for i in range(num):
        num_of_host=i
        scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
        response = os.popen('ping -c 1 '+scanned_ip)
        res = response.readlines()
        resu+=str(res)
        resu+=f"[#] Result of scanning: {scanned_ip} [#]\n{res[2].encode('cp1251').decode('cp866')}"+"\n\n"
    return resu

@app.get("/ht")
def sent_http_request(target, method="GET", headers=None, payload=None):
    headers_dict = dict()
    method=method.upper()

    if headers:
        for header in headers:
            header_name = header.split(':')[0]
            header_value = header.split(':')[1:]
            headers_dict[header_name] = ':'.join(header_value)
    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    return "[#] Response status code: "+str(response.status_code)+"\n"+"[#] Response headers:"+str(json.dumps(dict(response.headers)))+"[#] Response content:\n"+str(response.text)


