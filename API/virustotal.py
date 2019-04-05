import requests

def vt_url_scan(res_url):
  url = 'https://www.virustotal.com/vtapi/v2/url/scan'
  apikey = <apikey>
  params = {'apikey': apikey, 'url':res_url}
  response = requests.post(url, data=params)
  return response.json()
  
def vt_url_report(res_url):
  url = 'https://www.virustotal.com/vtapi/v2/url/report'
  params = {'apikey': '<apikey>', 'resource':res_url}
  response = requests.get(url, params=params)
  return response.json()
