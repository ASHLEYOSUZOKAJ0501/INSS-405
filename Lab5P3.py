def request():
    num1 = input('Enter num1:')
    num2 = input('Enter num2:')
    num3 = input('Enter num3:')
    print ('sum=', addition(num1, num2, num3))
    print ('average=', average(num1, num2, num3))
    print ('maximum=', maximum(num1, num2, num3))
    print ('minimum=', minimum(num1, num2, num3))
    print ('product=', product(num1, num2, num3))

def addition(num1, num2, num3):
    sum = int(num1) + int(num2) + int(num3)
    return sum

def average(num1, num2, num3):
    sum = int(num1) + int(num2) + int(num3)
    average = sum / 3
    return average

def maximum(num1, num2, num3):
    maximum = (num1, num2, num3)
    maxi = max(maximum)
    return maxi

def minimum(num1, num2, num3):
    minimum = (num1, num2, num3)
    mini = min(minimum)
    return mini

def product(num1, num2, num3):
    multiplication = int(num1) * int(num2) * int(num3)
    return multiplication


request()