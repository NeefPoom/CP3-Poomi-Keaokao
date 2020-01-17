def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return float(result)

print(vatCalculate(float(input("Total Price : "))))
