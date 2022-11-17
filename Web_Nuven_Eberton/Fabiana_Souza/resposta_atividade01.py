import requests

import json

SUBSCRIPTION_KEY = "d6e99366e8b84c77a54c8ac9b429adf8"

vision_service_address = "https://pythonimageanalize1fabiana.cognitiveservices.azure.com/vision/v2.0/ocr?"

address = vision_service_address + "analyze"

parameters  = {'details':'Celebrities',
               'language':'pt',
               'detectOrientation':'true'}

image_path = "a-pessoa-criativa.jpg"
image_data = open(image_path, "rb").read()


headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

response = requests.post(address, headers=headers, params=parameters, data=image_data)

response.raise_for_status()

results = response.json()
print(json.dumps(results))