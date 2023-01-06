import requests
import parameters

def get_web(web_url):
  resp = requests.get(web_url)
#   print (resp.text)
  print ('resp.status_code>>>', resp.status_code)
  return resp.status_code



if __name__=="__main__":
    web_url = parameters.web_url
    get_web(web_url)
    