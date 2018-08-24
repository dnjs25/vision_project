import requests
import time
import sys

api_url = "https://eastasia.api.cognitive.microsoft.com/vision/v1.0/describe"
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '7fe8083f86814c12ba7d15500d7a95df',
}
params = {'maxCandidates': '1'}
with open('static/temp/upload_180613_054312.jpg', 'rb') as f:
    data = f.read()

try:
    start_time = time.time()
    resp = requests.post(api_url, params=params, headers=headers, data=data)
    e = time.time() - start_time
    print(e)
    # print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60), file=sys.stderr)
    resp.raise_for_status()
    print(resp.text)
except Exception as e:
    print(str(e))
    sys.exit(0)
