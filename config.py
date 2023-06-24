import dotenv
import json
import requests

class WebBase(object):
    def join(_path: str|bytes, *paths):
        paths = list(paths)
        if type(_path) is bytes:
            _path = _path.decode()
        sperator = '/'
        for i in range(len(paths)):
            if type(paths[i]) is bytes: paths[i] = paths[i].decode()
            elif type(paths[i]) is not str: paths[i] = str(paths[i])
        _path =  '/'.join([_path] + paths)
        return _path

# Load cookies
cookies = dotenv.dotenv_values()
cookies_text = '; '.join(f"{key}={cookies[key]}" for key in cookies)

# Load config
configurations = json.load(open('config.json', 'rb'))
url = configurations['url']
base1 = configurations['base1']
base2 = configurations['base2']
base2end = configurations['base2end']
base2start = configurations['base2start']
base1end = configurations['base1end']
base1start = configurations['base1start']
class1 = configurations['class1']
class2 = configurations['class2']
class3 = configurations['class3']
class4 = configurations['class4']
class5 = configurations['class5']
class6 = configurations['class6']
class7 = configurations['class7']

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Host': url.replace('https://', '').replace('http://', ''),
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    "Cookie" : cookies_text
}