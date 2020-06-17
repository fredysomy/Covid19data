def getstateresource(state):    
    import requests
    import json
    a=requests.get('https://api.covid19india.org/resources/resources.json')
    b=a.text
    s=json.loads(b)
    data=s["resources"]
    for i in range(0,len(data)):
        x=data[i]
        if x["state"]==state and x["phonenumber"]!=" ":
            print(x["category"])
            print("City "+x["city"])
            print("Contact number="+x["phonenumber"])
            print("At "+x["nameoftheorganisation"])
            print("------------------------------------------")
        else:
            continue
