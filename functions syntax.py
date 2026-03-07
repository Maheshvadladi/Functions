'''a=10
b=20
print("the sum is: ",a+b)
print("the diff is: ",a-b)
print("the product is: ",a*b)'''

'''a=100
b=200
print("the sum is: ",a+b)
print("the diff is: ",a-b)
print("the product is: ",a*b)'''

'''a=1000
b=2000
print("the sum is: ",a+b)
print("the diff is: ",a-b)
print("the product is: ",a*b)'''

#functions
'''def calculate(a,b):
    print("the sum is: ",a+b)
    print("the diff is: ",a-b)
    print("the product is: ",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculator(a,b):
    print("the power is: ",a**b)
    print("the div is: ",a//b)
    print("the mod is: ",a%b)
calculator(10,20)
calculator(2,6)
calculator(5,4)'''

'''def add(a,b):
    print(a+b)
add(6,8)'''

'''def add():
    a=int(input("a value: "))
    b=int(input("b value: "))
    print(a+b)
add()'''

'''def fullname():
    fname=input("first name: ")
    lname=input("last name: ")
    print(fname+" "+lname)
fullname()'''

#print v/s return
'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(3,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(3,4))'''

#Task 1
#1st method

'''def cal():
    a=int(input("a value: "))
    b=int(input("b value: "))
    print("options 1=Addition, 2=Subtraction, 3=Multiplication")
    option=int(input("Enter option: "))
    if option==1:
        print("the sum is: ",a+b)
    elif option==2:
        print("the diff is: ",a-b)
    elif option==3:
        print("the product is: ",a*b)
    else:
        print("invalid option")
cal()'''

#2nd method

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value: "))
    b=int(input("b value: "))
    print("options 1=Addition, 2=Subtraction, 3=Multiplication")
    option=int(input("Enter option: "))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()'''
    
