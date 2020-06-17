def getDiffConreco(state1):    
    import requests
    import json
    from matplotlib import pyplot as plt
    a=requests.get('https://api.covid19india.org/states_daily.json')
    b=a.text
    s=json.loads(b)
    lcon=[]
    lreco=[]
    ldef=[]
    l1def=[]
    l=[]
    x=[]
    y=[]
    state=state1
    data=s["states_daily"]
    for i in range(0,96):
        int(i)
        l.append(i)
    for i in range(0,len(data)):
        x=data[i]
        if x["status"]=="Confirmed":
            y=int(x[state])
            lcon.append(y)
        if x["status"]=="Recovered":
            w=int(x[state])
            lreco.append(w)  
    for i in range(0,len(lcon)):
        dif=lcon[i]-lreco[i]
        ldef.append(dif)
    for i in range(0,len(ldef)-1):
        x=ldef[i]-ldef[i+1]
        l1def.append(x)
    """for i in range(0,len(l1def)-1):"""

    x=l
    y=ldef
    plt.title("confirmed-recovered") 
    plt.xlabel("Dates") 
    plt.ylabel("confirmed cases-recovered cases") 
    plt.bar(x,y) 
    plt.show()    
