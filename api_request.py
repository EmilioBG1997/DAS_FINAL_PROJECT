import requests, json

ENDPOINT = "https://www.superheroapi.com/api.php/180962903366604"
DC = []
for i in range(1, 733):
    url = f"{ENDPOINT}/{i}"
    r = requests.get(url)
    r = json.loads(r.text)
    
    if  r.get("biography", {}).get("publisher") == "DC Comics":
        DC.append(r)
print (DC)



