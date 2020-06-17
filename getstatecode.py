def getstatecode(state):
    states = {'Andhra Pradesh': 'AP', 'Arunachal Pradesh': 'AR', 'Assam': 'AS',     'Bihar': 'BR', 'Chhattisgarh': 'CT',     'Goa': 'GA', 'Gujarat': 'GJ',     'Haryana': 'HR',     'Himachal Pradesh': 'HP',     'Jharkhand': 'JH', 'Karnataka': 'KA',    'Kerala': 'KL',     'Madhya Pradesh': 'MP',     'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ML',     'Mizoram': 'MZ', 'Nagaland': 'NL',    'Odisha': 'OR', 'Punjab': 'PB',   'Rajasthan': 'RJ',    'Sikkim': 'SK',     'Tamil Nadu': 'TN',     'Telangana': 'TG',     'Tripura': 'TR', 'Uttarakhand': 'UK',     'Uttar Pradesh': 'UP',     'West Bengal': 'WB', 'Andaman and Nicobar Islands': 'AN',     'Chandigarh': 'CH',     'Dadra and Nagar Haveli and Daman and Diu': 'DN',     'Delhi': 'DL', 'Jammu and Kashmir': 'JK',     'Ladakh': 'LA', 'Lakshadweep': 'LD',     'Puducherry': 'PY',}
    code  = states.get (state)
    return(code,code.lower())
"""this program returns the statecode both in full caps and full lower case as a list"""    
    
