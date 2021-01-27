accounts = []
def signup(username,password,accounts):
    #check if taken
    for accountVar in accounts:
        if accountVar == [username,password]:
            return False
        else:
            accounts.append(username,password)
            return True
    accounts.append([username,password])
    return True
def login(accounts):
    username = (input('Enter a your login (username): '))
    password = (input('Enter a your login (password): '))
    for account in accounts:
        if account == [username,password]:
            return True
        else:
            return False
Opt = False
while True:
    while Opt == False:
        try:
            opt = int(input('Would you like to sign up or login [1/2]: '))
            Opt = True
        except:
            print('please enter 1 to proceed to the sign up or 2 to login')

    if opt == 1:
        username = (input('Please enter a username: '))
        password = (input('Please enter a password: '))
        signUpInfo = signup(username,password,accounts)
        if signUpInfo == True:
            print('Sign up... successfull!')
            print('Please check if you can log in')
            loginInfo = login(accounts)
            if loginInfo == True:
                print('logged in successfully')
            else:
                print('failed to log in')
        if signUpInfo == False:
            print('This account has been taken, try another one')
    elif opt == 2:
        loginInfo = login(accounts)
        if loginInfo == True:
            print('logged in successfully')
        else:
            print('failed to log in')
    else:
        print('please enter 1 to proceed to the sign up or 2 to login')



