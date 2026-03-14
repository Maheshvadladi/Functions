#global and local variables
#Def: a variable inside and outside of function is called global and local variables
#1). A variable is define above the funciton and is accessible to the entire global space is called a global variable
#2). A variable is inside the funciton is called local varialbe

#first case of global variable
'''a=3
def check():
    print("inside value is: ",a)
check()
print("outside value is: ",a)'''

#second case of global variable
'''a=2
def check1():
    a=5
    a=a**2
    print("inside value is: ",a)
check1()
print("outside value is: ",a)'''

#third case of global variable and local variable
'''a=4
b=3
def check2():
    a=7
    print("inside value is: ",a)
    a=10
    print("updated value is: ",a+5)
    b=12#local variable
    b=b+a
    print("value of b is: ",b)
check2()
print("a value is: ",a)
print("b value is: ",b)'''

#Usage of global keyword
#When user wants to access the global variable inside the function directly and carry forward the updated value even outside the function then we need to
#use global keyword.

#fourth case usage of global keyword
'''a=5
def final():
    global a,b
    print("inside value is: ",a)
    a=10
    print("updated value is: ",a)
    b=15
    b=b+a
    print("value of b is: ",b)
final()
print("a value is: ",a)
print("b value is: ",b)'''


