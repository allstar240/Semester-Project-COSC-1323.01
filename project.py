users = {}
status = ""

def displayMenu():
    status = input("Do you have an existing username or password? [y/n] Enter q to quit: ")  
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    return status
def save_to_file(createLogin,createPassw):
    print ("Saving login information...")
    name = "login.txt"
    file = open(name, "a")
    file.write(createLogin)
    file.write(createPassw)
    file.close()
def load_file():
    print ("Loading login information...")
    name = "login.txt"    
    file = open(name, "w")
    file.close()
    
def newUser():
    createLogin = verifyUsername()
    createPassw = verifyPass()
    users[createLogin] = createPassw # add login and password
    save_to_file(createLogin,createPassw)
    print("\nUser created!\n")     
    
def verifyUsername():
    tempLogin = '' #store username in temp until valid e-mail is entered then transfer to createLogin
    createLogin = ''
    retryUsername = 'y'
    while createLogin == '':
        while retryUsername == 'y':
            try:
                tempLogin = input("Create login name.  It must be an .edu e-mail address contianing @ and .edu: ")
                if tempLogin in users: # check if login name exists
                    print ("\nLogin name already exist!\n")
                    retryUsername = retryEntry()
                elif '@' not in tempLogin:
                    print("Invalid entry.  Please enter a valid e-mail address.")
                    retryUsername = retryEntry()
                elif '.edu' not in tempLogin:
                    print("Invalid entry.  Please enter a valid .edu e-mail address.")
                    retryUsername = retryEntry()
                else:
                    createLogin = tempLogin
                    retryUsername = 'n'
            except:
                print("Unexpected error.")
    return createLogin

def retryEntry():
    retryE = ''
    while not (retryE == 'n' or retryE == 'y'):
        retryE = input("Would you like to correct your entry? [y/n] ")
        try:
            if not (retryE == 'n' or retryE == 'y'):
                print("That is not a valid option.")
        except:
            print("Unexpected error.")
    return retryE

def verifyPass():
    tempPass = '' #store pass in temp until valid combination is entered then transfer to createPassw
    createPassw = ''
    retryPassw = 'y'
    while createPassw == '':
        while retryPassw == 'y':
            try:
                tempPass = input("Create password with 6-10 characters, at least one of which is a number: ")
                print(len(tempPass))
                print(hasNumbers(tempPass))
                if len(tempPass) < 6 or len(tempPass) > 11: # check if login name exists
                    print ("The password must be between 6 and 10 characters long.")
                    retryPassw = retryEntry()
                elif 5 < len(tempPass) < 11 and not hasNumbers(tempPass):
                    print("Please include at least one number in your password.")
                    retryPassw = retryEntry()
                else:
                    createPassw = tempPass
                    retryPassw = 'n'
            except:
                print("Unexpected error.")
    return createPassw    

def hasNumbers(checkString):    
    return any(char.isdigit() for char in checkString)

def oldUser():
    load_file()
    login = input("Enter login name: ")
    passw = input("Enter password: ")    
    try:
        if users[login] == passw:
            print ("\nLogin successful!\n")
    except:
        print ("\nUser doesn't exist or wrong password!\n")

while status != "q":            
    status = displayMenu()

