# Cold < 30
# Warm < 40
# Hot > 40

def request():
    temperature = int(input("enter temperature:"))
    if (int(temperature) < 30):
        print("Cold")
    elif (int(temperature) < 40):
        print("Warm")
    elif (int(temperature) > 40):
        print("Hot")


request()
