import requests
import json

class characterSearch:
    def __init__(self):
        self.url = "https://dokkan.fyi/characters/"

    #Search desired character
    def buscarPersonaje(self, id : int) -> list:
        #Create url
        try:
            url = self.url+str(id)
        except TypeError:
            print("Id debe ser tipo int")

        querystring = {"":""}

        headers = {
            "x-inertia": "true",
            "x-inertia-version": "aa6e2214730f2161a1f77c9fa9074052"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        #If character doesnt exist throw error
        if(response.status_code!=200):
            raise ValueError("Character doesnt exist or wrong code")

        #Add character name to list
        nombre = response.json()["props"]["card"]["name"]
        dict = [nombre]

        #Add all character links skills to list
        x = True
        i = 1
        a = "link_skill"
        b = "_id"
        links = []
        while x :
            try:
                c = a+str(i)+b
                links.append(response.json()["props"]["card"][c])
                i+=1
            except KeyError:
                x = False
        dict.append(links)
        #Return list [Name, [Links skills]]
        return dict