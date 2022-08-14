import urllib.request
import sys
import DB_object

import sqlite3

#URl + USERNAME make up the primary key
class DB_interface:
    #creates the database connection and table
    #params: name for the database file
    #return: true if successful, flase otherwise
    def createDB(self, conn):
        try:
            #DB_file_name_input = DB_file_name + ".db"
            #conn = sqlite3.connect(DB_file_name_input)
            conn.execute('''CREATE TABLE if not exists MYKEYS
             (URL           TEXT      NOT NULL,
             USERNAME       TEXT    NOT NULL,
             PASSWORD       TEXT    NOT NULL,
             PRIMARY KEY (URL, USERNAME)
             );''')
            return True
        except:
            return False

    def __init__(self, DB_file_name):
        self.DBname = DB_file_name
        self.conn = sqlite3.connect(DB_file_name + ".db") #sqlite3.Connection object
        self.isDB_Created = self.createDB(self.conn)
        
    
    def addRecord(self, record):
        url = record.getUrl()
        username = record.getUsername()
        password = record.getPassword()
        rowToEnter = [url, username, password]
        try:
            self.conn.execute("insert into MYKEYS (URL,USERNAME,PASSWORD) values (?, ?, ?)",(url, username, password))
            self.conn.commit()
            return True
        except:
            return False

    def getRecord(self, recordPrimaryKey):
        #some logic to return via url

        url = recordPrimaryKey[0]
        username = recordPrimaryKey[1]
        try:
            allRecords = []
            cursor = self.conn.execute("SELECT PASSWORD FROM MYKEYS WHERE URL = ? AND USERNAME = ?", (url, username))
            for row in cursor:
                newRow = []
                newRow.append(row[0])
                
                allRecords.append(newRow)
            return allRecords
        except:
            return "No Records matching that key"
        pass

    def getAllKeys(self):
        #some logic to return via url
        try:
            allRecords = []
            cursor = self.conn.execute("SELECT URL, USERNAME FROM MYKEYS")
            for row in cursor:
                newRow = []
                newRow.append(row[0])
                newRow.append(row[1])
                
                allRecords.append(newRow)
            return allRecords
        except:
            return "No Records matching that key"
        pass

    def getAllRecords(self):
        #some logic to return via url
        try:
            allRecords = []
            cursor = self.conn.execute("SELECT * FROM MYKEYS")
            for row in cursor:
                newRow = []
                newRow.append(row[0])
                newRow.append(row[1])
                newRow.append(row[2])
                allRecords.append(newRow)
            return allRecords
        except:
            return "No Records matching that key"
        pass    

    #edits a specific records
    #param primary key (url and username)
    #returns true if succesful, false otherwise
    def editRecord(self, recordPrimaryKey, change):
        print("inside edit record")
        url = recordPrimaryKey[0]
        username = recordPrimaryKey[1]
        rowToEnter = [url, username, change]
        try:
            sql_update_query = """Update MYKEYS set PASSWORD = ? where URL = ? and USERNAME = ?"""
            print(change + " " + url + " " + username )
            self.conn.execute(sql_update_query,(change, url, username))
            self.conn.commit()
            return True
        except:
            return False
        

    #deletes a specific record
    #param primary key (url and username)
    #returns true if succesful, false otherwise
    #TODO rework logic. First check if the record exisits. If not, return False or throw an error
    #If it does exist, do the delete logic
    def deleteRecord(self, recordPrimaryKey):
        url = recordPrimaryKey[0]
        username = recordPrimaryKey[1]
        rowToEnter = [url, username]
        try:
            isPresent = self.isPresent(rowToEnter)
            if isPresent:
                sql_update_query = """DELETE from MYKEYS where URL = ? and USERNAME = ?"""
            
                self.conn.execute(sql_update_query,(url, username))
                self.conn.commit()
                wasDeleted = not self.isPresent(rowToEnter)
                if wasDeleted:
                    print("wasDeleted: ", wasDeleted)
                    
                else:
                    print("wasDeleted: ", wasDeleted)
                    raise Exception("Record was not present")
                return True
            else:
                raise Exception("Record was not present")
            
    
        except Exception as e:
            print(e)
            return False

    #Tells you if a record is present in the table or not
    #params recordPrimaryKey: a list that contains the url, username, in that order and is used to look up the record
    #returns True if the record is found, else it returns False
    def isPresent(self, recordPrimaryKey):
        url = recordPrimaryKey[0]
        username = recordPrimaryKey[1]
        rowToEnter = [url, username]
       
        #SELECT COUNT(*) from a_table'
        sql_update_query = """Select COUNT(*) from MYKEYS where URL = ? and USERNAME = ?"""

        cursor=self.conn.cursor()

        
         
        cursor.execute(sql_update_query,(url, username))
        result = cursor.fetchall()

        print("This was the result", result[0][0])

        if result[0][0] == 0:
            print("was not present")
            return False
        else:
            print("was present")
            return True    

    def toString(self):
        allRecords = []
        cursor = self.conn.execute("SELECT URL, USERNAME, PASSWORD from MYKEYS")
        for row in cursor:
            newRow = []
            newRow.append(row[0])
            newRow.append(row[1])
            newRow.append(row[2])
            allRecords.append(newRow)
        return (allRecords)

    
