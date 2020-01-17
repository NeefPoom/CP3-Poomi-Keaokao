number = int(input("How many stars? : "))
for i in range(number):
    text = "" 
    for j in range(2*i+1):
        text += "*"
    print(" "*(number-i-1)+text)