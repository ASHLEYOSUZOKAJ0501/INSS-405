def request():
    num1=input('Enter varaiable num1')
    print (even(num1))



def even(num1):
    if int(num1)%2==0:
        return 'Even'
    else:
        return 'odd'

request()



