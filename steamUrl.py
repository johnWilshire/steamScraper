#!/bin/usr/python

# a class to hold the keys and generate player url requests from ids
# https://developer.valvesoftware.com/wiki/Steam_Web_API
# returns urls to access data from the steam community api 
class SteamUrl:
    # constructor takes key as argument, if no key passed key is ""
    def __init__(self, key=""):
        self.key = key


    # gets a url to request the a players information from the steam api.
    def playerSummary (self, id):
        return "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + self.key + "&steamids=" + id

    def friendsList(self, id):
        return "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key="+ self.key +"&steamid=" + id +"&relationship=friend"

    # gets the url for the request that has owned games
    def getOwnedGames (self, id):
        return "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + self.key + "&steamid=" + id

    # returns the url for the app information page 
    def getAppInfo (self, id):
        return "http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key=" + self.key +"&appid=" + id

    # gets the url for a list of all apps availible on steam
    def allApps(self):
        return "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"