import DB_object


def main():
    print("Hey")
    myUrl = "www.cheeseboys.com"
    myUsername = "spookyShoes"
    myPassword = "password1234"
    my_DB_Object = DB_object.DB_object(myUrl, myUsername, myPassword)
    print("constructor and getter test")
    print("url", my_DB_Object.getUrl())
    print("username", my_DB_Object.getUsername())
    print("password", my_DB_Object.getPassword())

    my_DB_Object.setUrl("www.cheeseboys.com")
    my_DB_Object.setUsername("comfortablehatboy")
    my_DB_Object.setPassword("notMyPassword")
    print("setter test")
    print("url", my_DB_Object.getUrl())
    print("username", my_DB_Object.getUsername())
    print("password", my_DB_Object.getPassword())

    print("dot operatore test", my_DB_Object._username)    

    #testing git

main()
