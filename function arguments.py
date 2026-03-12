#keyword and positional arguments
'''def details(id,name,mailid):
    id=2203031241005
    name='mohith'
    mailid='p@gmail.com'
    print(id,name,mailid)
details(id=id,name='name',mailid='mailid')'''

#method2
'''def details(id,name,mailid):
    print(id,name,mailid)
details(id=2203031241005,name='mohith',mailid='p@gmail.com')'''

#method3
#to setup headings
'''def details(id,name,mailid):
    print(id,name,mailid)
details(id='id',name='name',mailid='mailid')
details(id=2203031241005,name='mohith',mailid='p@gmail.com')'''

#method4
#order
'''def details(id,name,mailid):
    print(id,name,mailid)
details('2203031241005','mohith','m@.com')'''

#method5
#any order same result
'''details(name='mohith',mailid='m@.com',id=10)'''

#default arguments
#4methods
'''def grocery(item,price):
    print('item is %s' %item)
    print('price is %d' %price)
grocery('sugar',100)'''

'''def grocery(item='rice',price=1500):
    print('item is %s' %item)
    print('price is %d' %price)
grocery()'''

'''def grocery(item,price=200):
    print('item is %s' %item)
    print('price is %d' %price)
grocery('dhal')'''

'''def grocery(item='ghee',price):
    #erros accors because we cannot 
    #non-def arguments follows def arguments
    print('item is %s' %item)
    print('price is %d' %price)
grocery(800)'''

#task
'''def Cake(name, quantity, price):
    print("name is %s" %name)
    print("qunatity is %s" %quantity)
    print("price is %.2f" %price)
Cake("Choclate", "2kg", 320)'''

'''def Cake(name, quantity="1kg", price=190):
    print("name is %s" %name)
    print("qunatity is %s" %quantity)
    print("price is %.2f" %price)
Cake("Strawberry")'''

'''def Cake(name="Venela", quantity="1.5kg", price=210):
    print("name is %s" %name)
    print("qunatity is %s" %quantity)
    print("price is %.2f" %price)
Cake()'''

'''def Cake(name="Cold", quantity="1kg", price):
    print("name is %s" %name)
    print("qunatity is %s" %quantity)
    print("price is %.2f" %price)
Cake(230)'''

#* argments-> * is used to unpack the elements
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''b=(1,2,3,4,5,6,7,8,9)
print(b)
print(*b)'''

'''c={1,2,3,4,5,6,7,8}
print(c)
print(*c)'''

'''d={"year":2026, "month":3}
print(d)
print(*d)'''

'''a,b,c=1,2,3,4,5,6,7,8,9,10,11,12
print(a)
print(b)
print(c)'''#error

'''a,b,c=1,2,3
print(a)
print(b)
print(c)'''

'''a,*b,c=1,2,3,4,5,6,7,8,9,10,11,12
print(a)
print(*b)
print(c)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''

#variable arguments are automatic stored in tuple and we use * arguments
#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
d=[5,6,7,8,9,10]
check(d)
e={3,4,5,6,7}
check(*e)
f={"name":"pooja","city":"vja"}
check(*f)'''

'''def check1(*a):
    d=2#creating a variable
    print(a)
    for i in a:
        if type(i) in (int, float):
            d=d+i
            print(d)
        
check1()
check1(2,3,4,5,6)
check1(2,3,4,3.5,6.2,4.3)
check1(1,3,5,6.2,3.2,"pooja",4+9j,True,False)'''

#kwargs (**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30], "names":["somanath","aditya","mahesh"], "status":["P","A","P"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"idnos":[10,20,30], "names":["somanath","aditya","mahesh"], "status":["P","A","P"]}
details(**d)'''

#both * and ** usage
'''def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is: ",i)
        print("values is: ",j)
final()
data=(2,3,4,5,2.3,4.5)
final(*data)
details={"names":["sasidar","jaswanth","naveen"], "marks":[90,80,70]}
final(**details)
final(*data,**details)'''

#max, min, sum
'''a=4,6,8,9,10,12,14
print(max(4,6,8,9,10,12,14))
print(min(4,6,8,9,10,12,14))
print(sum(a))'''

#task
'''n=int(input("Enter no of students: "))
present=0
absent=0
for i in range(n):
    attendance=input("Enter the value: ")
    if attendance=="p":
        present+=1
    else:
        absent+=1
print("total no of studentsn)
print("no of students present: ",present)
print("no of students absent: ",absent)'''



