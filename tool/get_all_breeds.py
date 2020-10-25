#!/usr/bin/env python3
"""
Get all dog bleeds from Dog API
"""
import json
import requests

URL = 'https://dog.ceo/api/breeds/list/all'

if __name__ == '__main__':
  res = requests.get(URL)
  res_json = json.loads(res.text)
  breeds = res_json['message']

  for breed in breeds:
    if breeds[breed]:
      for breed_children in breeds[breed]:
        print('<option value="' + breed + '/' + breed_children + '">' + breed_children + ' ' + breed + '</option>')
    else:
      print('<option value="' + breed + '">' + breed + '</option>')

