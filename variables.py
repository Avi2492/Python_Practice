# Baisc syntax
x = 5
y = "Avinash"
print(x)
print(y)

# Lets assign same value
x = 5
x = 'Avinash'
# String will be more preferable
print(x) 

# typecasting
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
print(type(x))

# Case senstive - variables name are case senstive
a = 4
A = 'Sally'
print(a)
# Here A will not overite a

# Assign multiple values
d, e, f = 'Bmw', 'Audi', 'Fortuner'
print(d)
print(e)
print(f)

# One to multiple
g = h = i = 'Apple'
print(h)

# unpacking/ disctionary
cars = ['Audi', 'ferrari', 'Bmw']
d, e, f = cars
print(d)
print(e)
print(f)

# Output variables
x = "JAVA"
y = "is"
z = "Good"
# Concatination but type should be same
print(x, y, z)

# different type throw an error

# Global variables - outside of function used by anyone inside or outside
x = "Awsome"

def myfunc():
    print("python is " + x)

myfunc()   

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
y = "awsome"

def myfuns():
    y = "fantastic"
    print("python is " + y)

myfuns()

print("python is " + y)

# Global keyword - use if you want to change a global variable inside a function.
x = "awsome"

def myfun():
    global x
    x = "fantastic"

myfun()

print("python is " + x)
