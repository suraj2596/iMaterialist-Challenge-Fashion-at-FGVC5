#Just a test script. Actual download script is in the Python notebook
import json
data = json.load(open('validation.json'))

#for i in range(len(data['images'])):
img_url = data['images'][0]['url']
img_name = data['images'][0]['imageId'] 
print img_url
print img_name
