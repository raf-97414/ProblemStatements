import logging
import sys

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def app_status(url, urlstrip):
    try:
        #avoids verifying ssl cert
      session = requests.Session()
      r = session.get(url, verify=False,timeout=(20,10))
                                                #time to establish connection #time to wait on a response once your client has established a connection
      if r.status_code == 200:
          print("Status code is " + str(r.status_code) +" of "+ urlstrip + " so domain is up")
          logging.basicConfig(filename="activeStatus.log", filemode='w')
          logging.warning("Status code is " + str(r.status_code) +" of "+ urlstrip + " so domain is up")
      else:
          print("Status code is " + str(r.status_code) +" of "+urlstrip+" so domain is down")
          logging.basicConfig(filename="activeStatus.log", filemode='w')
          logging.warning("Status code is " + str(r.status_code) + " of " + urlstrip + " so domain is down")


    except TimeoutError:
        print("Connection timed out")





#entry point for program execution
if __name__ == '__main__':
    try:
        #print('Hello add your domain to be checked as follow python3 %s <url>' % sys.argv[0])
        url = sys.argv[1].strip()

        if (url[:8] == "https://"):
            urlstrip = url.replace("https://","")
        else:
            urlstrip = url.replace("http://", "")
        app_status(url, urlstrip)
    except IndexError:
        print('[-] Usage python3 applicationHealthChecker.py <fullpathurl>')
        print('[-] Example python3 applicationHealthChecker.py https://example.com')
        print('[-] Example python3 applicationHealthChecker.py http://example.com')






