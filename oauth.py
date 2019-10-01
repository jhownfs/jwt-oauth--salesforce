import jwt
import time
import requests
import json

def oAuthConnectionRS(url, consumerkey, keyfile, user):
  
  urlDomain = url
  issuer = consumerkey
  keyfileStore = keyfile
  user = user

  with open(keyfileStore) as fd:
    private_key = fd.read()

    payload = {
      'iss': issuer,
      'exp': int(time.time()) + 300,
      'aud': urlDomain,
      'sub': user
    }
    
  encoded = jwt.encode(payload, private_key, algorithm='RS256')

  r = requests.post(urlDomain + '/services/oauth2/token', data = {
    'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    'assertion': encoded,
  })

  print('Status:', r.status_code)
  return r.json()