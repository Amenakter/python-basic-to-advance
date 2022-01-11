x = 20  #x is a variable and 20 is a value of variable x
y = "Bangladesh" #this type of string

print(x)
print(y)


first_name = "Amena "
last_name = "Akter"
print(first_name + last_name)

# check data type of variable

X = 12 #int type
y = "123" #string
z = 12.34 # float 
c = "Mohon" #string
x = True #boolen

print(type(X))
print(type(y))
print(type(z))
print(type(c))
print(type(x))



# double quotes or single Quotes dosen't matter in python programming

a = "Mollika" 
# both are same
b = 'Mollika'

print(a)
print(b)

# python variable case-sensitive

a = 23
A = 40
# A is not overwrite a
print(a)
print(A)

'''
2a = 23 # 2a is not  variable
first name = "Amena" # is not variable
first - name = "Amena" # is not variable
@,$,%,& this symbol don't use to declear a variable name

'''

#different type of variable, chamel case, pascal case, snake case

myFirstName = "Amena" #chamel case
MyLastName = "Akter" #pascal case
my_full_name =  "Amena Akter"#snake case


print("My first name:",myFirstName)
print( "My last name:",MyLastName)
print("My full name:",my_full_name)



#we can assign multiple variable in one line 

a, b, c = 23, 34, 45
print(a) # 23
print(b) # 34
print(c) #45

#we can assign  one value to multiple variable in one line

x=y=z = "Bangladesh"

print(x)
print(y)
print(z)

#unpack collection. python allow extract the values into variable
num = [12, 32, 45, 56, 35]
a, b, c, d, e = num
print(a)

contry = ["Bangladesh" , "india", "srilangka"]
x , y , z = contry

print(x)
print(y)
print(z)


# variable concatanation

name = "Amena Akter"
print("My name is ", name)

x = 23
y =23
print(x+y)


a = 23
b = 34
c = a + b
print(c)


a = "fantastic"
print("Python is " + a)


first_name = "Amena "
last_name = "Akter"
print("fullname: ", first_name + last_name)

first_name = "Amena "
last_name = "Akter"
fullName = first_name + last_name
print("fullname: ",fullName)


''' global variable ===>
 global variable are created outside of the function
 global variable can used everyone,both inside or outside of the function.'''

x = "Amena" #global variable
def bio():
    print("My name is " + x) # use inside
bio() 
print("this is " + x) #use outside

'''local variable ===>
 local variable are created inside of function.
 local vareiable are use only inside of the function.'''

def myName():
    x = "Karim" #local variable
    print("My name is " + x)

myName()
# print("My name is " + x) # error => "x" is not define


"""globle keyword
globle keyword use to convert local variable to globle variable.
then we can use it everywhere, both inside or outside of the function"""

def country():
    global a #local variable to globle variable
    a = "Bangladesh"
    print("my country name is " + a) #inside
country()   

print("Dhaka is the capital of " + a) #outside










 
