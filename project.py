users = {}
status = ""

def displayMenu():
    status = input("Do you have an existing username or password? [y/n] Enter q to quit: ")  
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    return status

def newUser():
    tempLogin = '' #store username in temp until valid e-mail is entered then transfer to createLogin
    createLogin = ''
    while createLogin == '':
        try:
            tempLogin = input("Create login name.  It must be an .edu e-mail address: ")
            if tempLogin in users: # check if login name exists
                print ("\nLogin name already exist!\n")
            elif '@' not in tempLogin:
                print("Invalid entry.  Please enter a valid e-mail address.")
            elif '.edu' not in tempLogin:
                print("Invalid entry.  Please enter a valid .edu e-mail address.")
            else:
                createLogin = tempLogin
        except:
            print("Unexpected error.")
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