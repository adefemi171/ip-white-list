import requests
import base64
import json

https://github.com/firehol/blocklist-ipsets/blob/master/blocklist_de.ipset

https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/blocklist_de.ipset

def constructURL(user = "firehol",repo_name= "blocklist-ipsets",path_to_file= "blob/master/blocklist_de.ipset",url= "404"):
  url = url.replace("{user}",user)
  url = url.replace("{repo_name}",repo_name)
  url = url.replace("{path_to_file}",path_to_file)
  return url

user = 'firehol'
repo_name = 'blocklist-ipsets'
path_to_file = 'blob/master/blocklist_de.ipset'
json_url ='https://api.github.com/repos/{user}/{repo_name}/contents/{path_to_file}'

json_url = constructURL(user,repo_name,path_to_file,json_url) #forms the correct URL
response = requests.get(json_url) #get data from json file located at specified URL 

if response.status_code == requests.codes.ok:
    jsonResponse = response.json()  # the response is a JSON
    #the JSON is encoded in base 64, hence decode it
    content = base64.b64decode(jsonResponse['content'])
    #convert the byte stream to string
    jsonString = content.decode('utf-8')
    finalJson = json.loads(jsonString)
    print (content)
else:
    print('Content was not found.')

# for key, value in finalJson.items():
#     print("The key and value are ({}) = ({})".format(key, value))