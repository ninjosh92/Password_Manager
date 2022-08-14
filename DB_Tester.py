import DB_interface
import DB_object


def main():
    print("Hey")
    my_DB_interface = DB_interface.DB_interface("Keys")
    #print(my_DB_interface.toString())
    print(my_DB_interface.isDB_Created)

    myUrl1 = "www.bitchen.com"
    myUsername1 = "AssMan69"
    myPassword1 = "Password1234"
    myRecord1 = DB_object.DB_object(myUrl1, myUsername1, myPassword1)

    myUrl2 = "www.itchen.com"
    myUsername2 = "AssMan70"
    myPassword2 = "Password12345"
    myRecord2 = DB_object.DB_object(myUrl2, myUsername2, myPassword2)

    myUrl3 = "www.bitchen.com"
    myUsername3 = "AssMan71"
    myPassword3 = "Password123456"
    myRecord3 = DB_object.DB_object(myUrl3, myUsername3, myPassword3)    

    #myRecord1 = ["www.bitchen.com", "AssMan69", "Password1234"]
    #myRecord2 = ["www.itchen.com", "AssMan70", "Password12345"]
    #myRecord3 = ["www.bitchen.com", "AssMan71", "Password123456"]

    print ("This worked 1:", my_DB_interface.addRecord(myRecord1))
    print ("This worked 2:", my_DB_interface.addRecord(myRecord2))
    print ("This worked 3:", my_DB_interface.addRecord(myRecord3))
    recordString = my_DB_interface.toString()
    getStringTest1 = my_DB_interface.getRecord("www.bitchen.com")
    getStringTest2 = my_DB_interface.getRecord("www.itchen.com")
    print(recordString)
    print("This is the getString test1: ", getStringTest1)
    print("This is the getString test2: ", getStringTest2)
    pk = ["www.bitchen.com", "AssMan69"]
    success = my_DB_interface.editRecord(pk, "assword")
    print("We edited a record: ", success)
    print(recordString)

    pk = ["www.itchen.com", "AssMan70"]
    success = my_DB_interface.deleteRecord(pk)
    print("We deleted a record: ", success)
    print(my_DB_interface.toString())

    pk = ["www.itchen.com", "AssMn70"]
    success = my_DB_interface.deleteRecord(pk)
    print("We deleted a record: ", success)
    print(my_DB_interface.toString())
    #testing git

main()
