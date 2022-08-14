import urllib.request
import sys

import sqlite3

class DB_object:
    #creates the database object
    #params: url, the username, and the password
    #return: true if successful, flase otherwise
    def __init__(self, url, username, password):
        self._url = url
        self._username = username
        self._password = password

    #getUrl
    #params: none
    #returns: url stringx
    def getUrl(self):
        return self._url

    #getUsername
    #params: none
    #returns: username string
    def getUsername(self,):
        return self._username

    #getPassword
    #params: none
    #returns: password string
    def getPassword(self):
        return self._password


    #TODO setters for the members
    #setUrl
    #params: none
    #returns: url stringx
    def setUrl(self, url):
        self._url = url

    #setUsername
    #params: none
    #returns: username string
    def setUsername(self, username):
        self._username = username

    #setPassword
    #params: none
    #returns: password string
    def setPassword(self, password):
        self._password = password
