# This script will create a SqlInjection Scanner

# this script will require:
# - pipenv (pip install pipenv)

# SQL Injection:
# A SQL injection attack consists of insertion or “injection” of a SQL query via the input data 
# from the client to the application. A successful SQL injection exploit can read sensitive data 
# from the database, modify database data (Insert/Update/Delete), execute administration operations on the database 
# (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue 
# commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected 
# into data-plane input in order to affect the execution of predefined SQL commands.

import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"

# function to get all forms
def get_forms(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")

# functipn that returns the details of each form
def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get")
    inputs = []
    
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        
    detailsOfForm['action'] = action
    detailsOfForm['method'] = method
    detailsOfForm['inputs'] = inputs
    return detailsOfForm

def vulnerable(response):
    errors = {"quoted string not properly terminated", "unclosed quotation mark after character string", "SQL syntax error"}
    
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False # else return false
    
def sql_injection_scan(url):
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    
    for form in forms:
        details = form_details(form)
    
    # \ " ' are malicious characters
    for i in "\"'":
        data = {}
        for input_tag in details["inputs"]:
            if input_tag["type"] == "hidden" or input_tag["value"]:
                data[input_tag['name']] = input_tag["value"] + i
            elif input_tag["type"] != "submit":
                data[input_tag['name']] = f"test{i}"
                
        print(url)
        form_details(form)
        
        if details["method"] == "post":
            res = s.post(url, data=data)
        elif details["method"] == "get":
            res = s.get(url, params=data)
        
        if vulnerable(res):
            print(f"SQL injection attack vulnerability in link: {url}")
        else:
            print("No SQL injection attack vulnerability detected")
            break

if __name__ == __main__:
    urlToBeChecked = "https://somewebsitethatihavepermissiontodothison.com"
    sql_injection_scan()
    