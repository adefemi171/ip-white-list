import requests
import re

# https://github.com/firehol/blocklist-ipsets/blob/master/blocklist_de.ipset

def getBaseIP(url: str) -> list:
  """Get IP address from IPset
  """
  
  response = requests.get(url) #get data 

  ip_sets = response.text
  ip_list = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})', ip_sets)
  
  return ip_list
    