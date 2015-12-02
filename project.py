import json
users = {}
status = ""
f = open("login.txt", 'w')
f.close()

def displayMenu():
    status = input("Do you have an existing username and password? [y/n] Enter q to quit: ")  
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    return status
def save_to_file(users):
    print ("\nSaving login information...")
    name = "login.txt"
    json.dump(users, open(name, "w"))
def load_file():
    print ("\nLoading login information...\n")
    name = "login.txt"    
    try:
        tempUsers = json.load(open(name, "r"))
        return tempUsers
    except:
        print("There was an error reading the file.")
    
def newUser():
    createLogin = verifyUsername()
    createPassw = verifyPass()
    users[createLogin] = createPassw # add login and password
    save_to_file(users)
    print("\nUser created!\n")     
    
def verifyUsername():
    tempLogin = '' #store username in temp until valid e-mail is entered then transfer to createLogin
    createLogin = ''
    retryUsername = 'y'
    while createLogin == '':
        while retryUsername == 'y':
            try:
                tempLogin = input("Create login name.  It must be an .edu e-mail address containing @ and .edu: ")
                if tempLogin in users: # check if login name exists
                    print ("\nLogin name already exist!\n")
                    retryUsername = retryEntry()
                elif '@' not in tempLogin:
                    print("Invalid entry.  Please enter a valid e-mail address.")
                    retryUsername = retryEntry()
                elif '.edu' not in tempLogin:
                    print("Invalid entry.  Please enter a valid .edu e-mail address.")
                    retryUsername = retryEntry()
                    retryUsername = retryEntry()
                elif len(tempLogin) <5: #length of @ and .edu is 5
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
    users = load_file()
    login = input("Enter login name: ")
    passw = input("Enter password: ")    
    try:
        if users[login] == passw:
            print ("\nLogin successful!\n")
    except:
        print ("\nUser doesn't exist or wrong password!\n")

def main():
    status = "y"
    while status != "q":            
        status = displayMenu()

main()
