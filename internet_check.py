import requests
import sys

#function to check internet

def check_internet(host = "https://duckduckgo.com/", timeout = 100):
    try:
        requests.head(host, timeout = timeout)
        print("You are connected to internet.")
    except requests.ConnectionError:
        print("Please check your internet connection.")


check_internet()
