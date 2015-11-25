
# class that accesses the gender db

import urllib2
import json

class Gender:
    def __init__(self, connection, apikey):
        self.connection = connection
        self.apikey = apikey

    def getGender(self, name):
        response = self.lookUp(name)
        if response != None:
            return [response[1],response[2]]
        else:
            response = self.callApi( name)
            return [response[1], response[2]]

    def lookUp (self, name):
        c = self.connection.cursor()
        c.execute("""SELECT * FROM Gender WHERE name=?;""", (name,))
        return c.fetchone()

    def callApi(self, name):
        print "\tcalling gender API for ", name
        url = "https://api.genderize.io/?name=%s&apikey=%s" % (name, self.apikey )
        response = urllib2.urlopen(url)
        jsons = json.loads(response.read())
        return self.insertName(jsons, name)

    def insertName(self, nameJsons, name):
        c = self.connection.cursor()
        if nameJsons["gender"] == None:
            gender = "None"
            probability = 1.00
            count = 0
        else:
            gender = str(nameJsons["gender"])
            probability = str(nameJsons["probability"])
            count = str(nameJsons["count"])
        t = (name,gender,probability,count,)
        c.execute("""INSERT INTO Gender (name, gender, prob, count) VALUES (?, ?, ?,?);""", t)
        self.connection.commit()
        return t