def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("wrong password")
        return login()
def showMenu():
    print("------- ishop ----------")
    print("1.Vat Calculator")
    print("2. Price Calculator")
    return  menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    #ถ้าตัวแปรที่ประกาศอยู่ด้านใน ไม่สามารถเอาไปใช้ร่วมกับห้องใหญ่ได้
    if userSelected == 1:
        return  vatCalculate(float(input("What price? : ")))
    elif userSelected == 2:
        return  priceCalculate()
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
    # return result to where it call below
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return(vatCalculate(price1 + price2))
    #Returnค่า Function ไปที่ print ด้านล่าง

print(login())
