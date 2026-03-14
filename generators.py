#Generators
#No tuple comprehension in above cases if we remove those cases and keep parenthesis then the outcome is generated
#List comprehension syntax->a=[expr for var in collection/range]
'''a=[i for i in range(21)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(*a)
print(type(a))'''

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
#print(set(a))'''

#Main definition
#A generator is also a funciton which can be used as an iterator (loop) by producing group of values, variable used yield keyword
#yield v/s return
#return will terminate the function whereas yield can pass the function and go on with every successive iteration

'''a,b=[int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values: ").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

#yeild v/s return
'''def mygen():
   #return "python"
    #return "java"
    #return "dsa"
    return "python", "java", "dsa"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "dsa"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''
