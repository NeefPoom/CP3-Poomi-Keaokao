distance = float(input("Distance (km) : "))
while distance < 1:
    print("You have to fill number more than 1 ")
    distance = float(input("Distance (km) : "))
time = float(input("Time (Hour) : "))
while time < 1:
    print("You have to fill number more than 1 ")
    time = float(input("time (Hour) : "))
print(distance/time, "km/h")