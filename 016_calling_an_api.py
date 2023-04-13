from symbol import parameters
from urllib import response
import requests
import json

SUBSCRIPTION_KEY = 'd568291b79c1432d86356afcedf3bda5'

vision_service_address = 'https://rarc-python-image-analyzer.cognitiveservices.azure.com/vision/v3.1/'

address = vision_service_address + 'analyze'

params = {'visualFeatures': 'Description,Color', 'language': 'en'}

image_path = 'assets/images/tower-of-fantasy.jpg'
image_data = open(image_path, 'rb').read()

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

response = requests.post(address, headers=headers,
                         params=params, data=image_data)

response.raise_for_status()

results = response.json()
print(results)
# print(json.dumps(results))
