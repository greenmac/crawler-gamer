import requests

url = 'https://www.youtube.com/channel/UCL_qhgtOy0dy1Agp8vkySQg'
resp = requests.get(url)
resp_results = resp