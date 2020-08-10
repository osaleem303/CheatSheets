#######################################
#
#   Python CHEAT SHEET
#
#######################################


#**************************************
#   Table of Contents
#**************************************

# 1. Basic Commands
# 2. Basic DataTypes
# 3. File Reading Commands
# 4. Data Frames
# 5. Plotting


#**************************************
#   Basic Commands & Examples
#**************************************

#**************************************
#   Python Variables
#**************************************

# 	->Creating Variable
# 		Variables are containers for storing data values.
# 		Unlike other programming languages, Python has no 
# 		command for declaring a variable.
# 		A variable is created the moment you first assign
# 		a value to it.
	
    # ->Example

x = 5 #x is of int 
y = "John" #y is string
print(x)
print(y)

	# ->Output	
	# 	5
	# 	John

# Variables do not need to be declared with any particular 
# type and can even change type after they have been set.
	
	# ->Example

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

	# ->Output
	# 	sally
	
# String variables can be declared either by using single 
# or double quotes:
	
	# ->Example
x = "John"
# is the same as
x = 'John'
	
	# ->Output
	# 	John
		
	# Variable Names
	# 	-> A variable can have a short name (like x and y) or a more 
	# 	   descriptive name (age, carname, total_volume). Rules for Python variables:
	# 	-> A variable name must start with a letter or the underscore character
	# 	-> A variable name cannot start with a number
	# 	-> A variable name can only contain alpha-numeric characters 
	# 	   and underscores (A-z, 0-9, and _ )
	# 	-> Variable names are case-sensitive (age, Age and AGE are 
	# 	   three different variables)

	# ->Example
		#Legal variable names:
			# myvar = "John"
			# my_var = "John"
			# _my_var = "John"
			# myVar = "John"
			# MYVAR = "John"
			# myvar2 = "John"

		#Illegal variable names:
			# 2myvar = "John"
			# my-var = "John"
			# my var = "John"
			
# Assign Value to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

	# ->Example

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
		
	# 	->Output
	# 		Orange
	# 		Banana
	# 		Cherry
			
	# And you can assign the same value to multiple variables in one line:

	# ->Example
x = y = z = "Orange"
print(x)
print(y)
print(z)	
	
	# ->Output
	# 	Orange
	
	# You can also use the + character to add a variable to another variable:

	# ->Example

x = "Python is "
y = "awesome"
z =  x + y
print(z)
	
	# ->Output
	# 	Python is awesome
		
	# If you try to combine a string and a number, Python will give you an error:

	# ->Example
x = 5
y = "John"
print(x + y)	
	
	# ->Output
	# 	error
		
	# Global Variables
	
	# Variables that are created outside of a function are known as global variables.
	# Global variables can be used by everyone, both inside of functions and outside.	
	
	# Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
	
	# ->Output
	# 	Python is awesome
		
	# If you create a variable with the same name inside a function, this variable will 
	# be local, and can only be used inside the function. The global variable with the 
	# same name will remain as it was, global and with the original value.
		
	# ->Example
	# 	Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
    x = "fantastic"
print("Python is " + x)

myfunc()

print("Python is " + x)
		
	# 	->Output
	# 		Python is fantastic
	# 		Python is awesome
	
	# The global Keyword
	
	# Normally, when you create a variable inside a function, that variable is local,
	# and can only be used inside that function.
	# To create a global variable inside a function, you can use the global keyword.

	# ->Example
	# 	If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
x = "fantastic"

myfunc()

print("Python is " + x)	
	
	# 	->Output
	# 		Python is fantastic
		
	# Also, use the global keyword if you want to change a global variable inside a
	# function.
	
	# ->Example
	# 	To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
    global x
x = "fantastic"

myfunc()

print("Python is " + x)
		
		# ->Output
			# Python is fantastic


#**************************************
#   Python Data Types
#**************************************            

# Built-in Data Types
	
	# 	In programming, data type is an important concept.
	# 	Variables can store data of different types, and different types 		can do different things.
	# 	Python has the following data types built-in by default, in these 			
	# 	categories:

	# 	-> Text Type:	str
	# 	-> Numeric Types:	int, float, complex
	# 	-> Sequence Types:	list, tuple, range
	# 	-> Mapping Type:	dict
	# 	-> Set Types:	set, frozenset
	# 	-> Boolean Type:	bool
	# 	-> Binary Types:	bytes, bytearray, memoryview


	# Getting the Data Type

	# 	You can get the data type of any object by using the type() 		function:

	# 	->Example
	# 		Print the data type of the variable x:

x = 5
print(type(x))
		
	# 	# ->Output
	# 	# 	<class 'int'>


	# Setting the Data Type

	# 	In Python, the data type is set when you assign a value to a 		variable:

	# 	->Example	Data Type	


x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

	# Setting the Specific Data Type

	# If you want to specify the data type, you can use the following 	constructor functions:

	# ->Example	Data Type	
		
		
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set("apple", "banana", "cherry")	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview


#**************************************
#   Python Numbers:
#**************************************   

# There are three numeric types in Python:

	# -> int
	# -> float
	# -> complex

	# Variables of numeric types are created when you assign a value to them:

	# -> Example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

	# To verify the type of any object in Python, use the type() function:

	# -> Example

print(type(x))
print(type(y))
print(type(z))

	# -> Output
	# 	<class 'int'>
	# 	<class 'float'>
 	# 	<class 'complex'>


	# Integers:

	# Int, or integer, is a whole number, positive or negative, without 		decimals, of unlimited length.

	# -> Example


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

	# -> Output
	# 	<class 'int'>	 
	# 	<class 'int'>
	# 	<class 'int'>

	# Floats:
	
	# Float, or "floating point number" is a number, positive or negative, 		containing one or more decimals.

	# -> Example

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

	# -> Output
	# 	<class 'float'>
	# 	<class 'float'>
	# 	<class 'float'>

	# Float can also be scientific numbers with an "e" to indicate the power of 		10.

	# -> Example

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

	# -> Output
	# 	<class 'float'>
	# 	<class 'float'>
	# 	<class 'float'>


	# Complex:

	# Complex numbers are written with a "j" as the imaginary part:

	# -> Example

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

	# -> Output
	# 	<class 'complex'>
	# 	<class 'complex'>
	# 	<class 'complex'>



#**************************************
# #   Python Casting:
# #**************************************    
	
# 	Specify a Variable Type
	
# 	There may be times when you want to specify a type on to a variable. This 	can be done with casting. Python is an object-orientated language, and as 	such it uses classes to define data types, including its primitive types.

# 	Casting in python is therefore done using constructor functions:

# 	-> int() - constructs an integer number from an integer literal, a float 		literal (by rounding down to the previous whole number), or a string 		literal (providing the string represents a whole number)
# 	-> float() - constructs a float number from an integer literal, a float 	literal or a string literal (providing the string represents a float or an 	integer)
# 	-> str() - constructs a string from a wide variety of data types, 	including 	strings, integer literals and float literals

# 	-> Example
# 		Integers:

x = int(1)  
y = int(2.8)
z = int("3") 

	# -> Output
	# 	1
	# 	2
	# 	3


	# -> Example
	# 	Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


	# -> Example
	# 	Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'