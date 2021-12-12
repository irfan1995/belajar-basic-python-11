#dictionary

mydict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1987
}

print(mydict)


print(mydict["model"])

#change value
mydict["year"] = 1995

print(mydict)

#Quiz
mydict = {'Name':'Irfan', 'Age':25, 'Class':"First"}
mydict['Age']=8
mydict['School']='Dict School'

print("Dict['Age']: ",mydict['Age'])
print("Dict['School']: ",mydict['School'])

#Function tanpa parameter
def myFunction():
    print("Halo nama saya Irfan")

myFunction()    

#Function dengan parameter
def myFunction(nama):
    print("Halo nama saya : " + nama)

myFunction("Irfan")  

#Function default parameter
def myFunction(name="Anonym"):
    print("Hello " + name)

myFunction()

#function with return value
def myFunction(x):
    y = x**2 + 2*x + 3
    return y

print(myFunction(3))    

#Quiz
def myFunction():
    x = 10
    print("Value inside section: ", x)

x = 20
myFunction()
print("Value outside section: ", x)