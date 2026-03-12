#write()
'''a=open("mahesh.txt", "w")
a.write("codegnan it solutions")
a.close()'''

'''a=open("mahesh.txt", "w")
a.write("python")
a.close()'''

#append
'''a=open("mahesh.txt", "a")
a.write(" mahesh")
a.close()'''

#run-time input()
'''a=open("mahesh.txt", "w")
a.write(input("Data: "))
a.close()'''

'''a=open("mahesh.txt", "w")
b=input("data: ")
a.write(b)
a.close()'''

'''a=open("mahesh.txt", "w")
b=input("data: ")
a.write(b)
a.close()'''

#readlines()
'''a=open("mahesh.txt")
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#it will display with \n
#print(a.read(8))#it will display no of characters'''

#writelines()#it makes every object side by side
'''a=open("data.txt", "w")
b=["python", "dsa", "java", "html", "css"]
a.writelines(b)
a.close()'''

'''a=open("data.txt", "w")#it makes every object in new line
b=["python", "dsa", "java", "html", "css"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("functions syntax.py")
print(a.read())'''

'''a=open("C:\\Users\\mahes\\Downloads\\codegnan 029\\function arguments.py")
print(a.read())'''

#error handling
#syntax error
#Compile error
'''for i in range(10)
print(i)'''

#run_time error
#Excution time it will happen
'''a=int(input("a value: "))
b=int(input("b value: "))
print(a//b)'''

#logical error
#Error in logic (it can't be visible)
'''a=10
b=20
print(a-b)'''

'''a=2
b=5
if a>b:
    print("true")'''

#Exception handling
#try->Instructions from which we are expecting the exceptions
#except->Exception is raised in try block. It will be handle by this block
#else->Optional(no-exception)
#finally->Always it will display

'''while True:
    a=int(input("a value: "))
    b=int(input("b value: "))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exception")
    finally:
        print("program end...")'''
