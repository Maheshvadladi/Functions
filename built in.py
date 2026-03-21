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
