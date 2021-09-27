import urllib.request
import json

def check_updates(NAME, VERSION, URL):
    def parse_version(vstr):
        vstrs = vstr.lstrip('v').split('.')
        return [int(v) for v in vstrs]

    try:
        response = urllib.request.urlopen(
            URL + "/releases/latest")
        meta = json.loads(response.read())
        latest_version = parse_version(meta['tag_name'])
        current_version = parse_version(VERSION)

        for i in range(len(current_version)):
            if current_version[i] > latest_version[i]:
                break
            if current_version[i] < latest_version[i]:
                print("A new version of " + NAME + " is available", )
                print(URL + "/releases\n")
    except:
        pass