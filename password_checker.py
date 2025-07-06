#password_checker.py

#Ask user to enter Password
password = input("Enter Password :")
#Loop until correct password is entered
while password != "open123" :
    password = input("Wrong Password, re-enter Password :")
#Once correct, welcome the user
else:
    print("Welcome back 😁")
