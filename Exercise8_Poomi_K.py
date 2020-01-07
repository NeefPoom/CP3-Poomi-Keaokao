wirelessCharger = 500
adaptor = 300
iPhone = 34000

usernameInput = input("Username : ")
while usernameInput != "admin":
    print("This username is do not exist")
    usernameInput = input("Username : ")
passwordInput = input("Password : ")
while passwordInput != "1234":
    print("Wrong password. Please try again")
    passwordInput = input("Password : ")
if usernameInput == 'admin' and passwordInput == '1234':
    print("welcome !",usernameInput)
    print("------iShop--------")
    print("1. Wireless Charger",wirelessCharger,"THB")
    print("2. Adaptor",adaptor,"THB")
    print("3. iPhone",iPhone,"THB")
    userSelected = int(input(">> "))

    if userSelected == 1 or userSelected == "Wireless Charger":
        amountItem1 = int(input("How many items? : "))
        print("------------------------------")
        print("Total : ", wirelessCharger * amountItem1, "THB")
        print("----------Thank  You----------")

    elif userSelected == 2 or userSelected == "Adaptor":
        amountItem2 = int(input("How many items? : "))
        print("------------------------------")
        print("Total : ", adaptor * amountItem2, "THB")
        print("----------Thank  You----------")

    elif userSelected == 3 or userSelected == "iPhone":
        amountItem3 = int(input("How many items? : "))
        print("------------------------------")
        print("Total : ", iPhone * amountItem3, "THB")
        print("----------Thank  You----------")