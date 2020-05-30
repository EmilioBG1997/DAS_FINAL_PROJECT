import requests 
import json


class DC_API(object):
    def __init__(self):
        self.ENDPOINT = "https://www.superheroapi.com/api.php/180962903366604"
        self.DC = []
    def get_data(self):
        for i in range(1, 10):
            uri = f"{self.ENDPOINT}/{i}"
            r = requests.get(uri)
            r = json.loads(r.text)
    
        if  r.get("biography", {}).get("publisher") == "DC Comics":
            self.DC.append(r)
        
        return self.DC

if __name__ == "__main__":
    api = DC_API()
    print(api.get_data())