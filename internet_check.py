import urllib.request

a=(str("Checking internet connection..."))

print(a)

def connect(host='http://duckduckgo.com'):
      try:
          urllib.request.urlopen(host)
          return True
      except:
          return False
# test
print("connected to the internet" if connect() else "You are not connected to the internet")

"""import requests

def url_checker(url):
	try:
		#Get Url
		get = requests.get(url)
		# if the request succeeds 
		if get.status_code == 200:
			return(f"{url}: is reachable")
		else:
			return(f"{url}: is Not reachable, status_code: {get.status_code}")

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")"""



"""import speedtest

# Speed test
#st = speedtest.Speedtest()

# Download Speed
#ds = st.download()

#print(ds)


import whois

domain = 'pytutorial.com'

get_info = whois.whois(domain)

print(get_info)

"""

"""import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( "connected" if connect() else "no internet!" )
"""
