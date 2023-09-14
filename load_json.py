
# # import urllib library
# from urllib.request import urlopen
# from pprint import pprint
import io
import json
# import json
# # store the URL in url as 
# # parameter for urlopen
# url = "https://www.toolify.ai/self-api/v1/tools?order_by=recommended_at&page=61&per_page=100&fbclid=IwAR0mshO-6LN8lVaIL1mI07V6mJczXufFAWjzp_PFXD9pJnTCxCCSaGahLXg"
  
# # store the response of URL
# response = urlopen(url)
  
# # storing the JSON response 
# # from url in data
# data_json = json.loads(response.read())
  
# # print the json response
# pprint(data_json)
from urllib import request
from urllib.request import Request, urlopen
rslt = []
for page_no in range(1, 62):
    url = "https://www.toolify.ai/self-api/v1/tools?order_by=recommended_at&page="+str(page_no)+"&per_page=100&fbclid=IwAR0mshO-6LN8lVaIL1mI07V6mJczXufFAWjzp_PFXD9pJnTCxCCSaGahLXg"
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    webpage = urlopen(request_site).read()
    my_json = webpage.decode('utf8')
    data = json.loads(my_json)
    rslt += data["data"]["data"]
s = json.dumps(rslt, indent=4, sort_keys=True)
with open('services.json', 'w') as f:
    f.write(s)
# Load the JSON to a Python list & dump it back out as formatted JSON



