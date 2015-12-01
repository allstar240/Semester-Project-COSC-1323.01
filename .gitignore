users = {}
status = ""

def displayMenu():
    status = input("Do you have an existing username or passowrd? [y/n] Enter q to quit: ")  
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    return status

def newUser():
    createLogin = input("Create login name: ")

    if createLogin in users: # check if login name exists
        print ("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw # add login and password
        print("\nUser created!\n")     

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if users[login] == passw: 
        print ("\nLogin successful!\n")
    else:
        print ("\nUser doesn't exist or wrong password!\n")

while status != "q":            
    status = displayMenu()
