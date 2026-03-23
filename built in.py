#built-in functions

#from keys
'''a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a, "mahesh")
print(b)'''

#eval()
#evaluate means it will accept any data type in run time input

'''while True:
    a=int(input("a value: "))
    b=int(input("b value: "))
    print(a+b)'''

'''while True:
    a=float(input("a value: "))
    b=float(input("b value: "))
    print(a+b)'''

'''while True:
    a=input("a value: ")
    b=input("b value: ")
    print(a+b)'''

'''while True:
    a=eval(input("a value: "))
    b=eval(input("b value: "))
    print(a+b)
    print(type(a))'''

#zip-> we can combine multiple collections into one collection
'''a=[10,20,30,40,50,60]
names=["bhavani","taruni","joshnavi","chandana","harika"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''

#enumerate()-> we can give counter to the collection

'''names=["emanuel","mahesh","naveen","hitesh","mohith"]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names,1))
print(b)

b=list(enumerate(names,1))
print(b)'''

#ASCII
'''for i in range(65,91):
    print(chr(i),end=' ')'''

'''a="mahesh"
for i in a:
    print(ord(i))'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''

#annonymous functions (nameless functions)
#write a function to calculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f( ):
    x=int(input("Enter value: "))
    print(2*x+5)
f( )'''

#syntax
#a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("Enter number: "))
b=lambda x:2*x+5
print(b(a))'''

'''a=int(input("a value: "))
b=int(input("b value: "))
c=lambda a,b:a*b
print(c(a,b))'''

'''a=lambda a:a.upper()
print(a("python"))'''

'''a=input("Enter data: ")
b=lambda a:a.upper()
print(b(a))'''

'''a=input("Enter first name: ")
b=input("Enter last name: ")
c=lambda a,b:(a+"  "+b).title()
print(c(a,b))'''

'''a,b=[str(x) for x in input("enter the names: ").split(",")]
c=lambda a,b:(a+"  "+b).title()
print(c(a,b))'''

#filter()
'''a=[2,5,7,8,9,11,20]'''
'''for i in a:
    if i%2==0:
        print(i,end=" ")'''

'''b=list(filter(lambda x:x%2==0, a))
print(b)'''

'''a=[[ ], ( ), set( ), { }, None, 3,4.5,"python",6+9j,True,False]
b=list(filter(None,a))
print(b)'''

#map()-> each object from a collection and forms a new collection
'''a=[10,5,7,8,15,20,40,100]
b=[4,6,12,25,40,80,35,1,98]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''

'''a=input("data1: ")
b=input("data2: ")
print(a+b)'''

'''a,b=input("Enter data: ").split(",")
print(a+b)'''

'''a,b=[x for x in input("Enter data: ").split(",")]
print(a+b)'''

'''a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print(a+b)'''

'''a,b=int(input("enter values: ").split(","))
print(a+b)''' #we get error

'''a,b=[int(x) for x in input("Enter values: ").split(",")]
print(a+b)'''

'''a,b=map(int, input("Enter values: ").split(","))
print(a+b)'''

'''a=list(map(int, input("Enter vaues: ").split(",")))
print(a)'''

'''a=tuple(map(int, input("Enter vaues: ").split(",")))
print(a)'''

'''a=set(map(int, input("Enter vaues: ").split(",")))
print(a)'''

#dictionary run time
'''a=input("Enter the key and value pair: ")
b=dict(i.split(":") for i in a.split(","))
print(b)'''
