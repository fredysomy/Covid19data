def getdistrictzone(state):
    import requests
    import json
    a=requests.get('https://api.covid19india.org/zones.json')
    b=a.text
    s=json.loads(b)
    z=s["zones"]
    for i in range(0,734):
        y=z[i]
        if y["statecode"]==state:
            w=y["district"]
            c=y["zone"]
            print(w+" zone="+c)
