#String

#String are another data structure of python. They denote str in the pyObject.
#Example:

var_name_1 = "Hello"
var_name_2 = "Lama"
var_name_3 = 97

#This is how we initialize string.
#We can do multiple thing with string. We can add multiply not like integer but add two strings and multiple its value.

#We can concinnate.
value = var_name_1 + var_name_2
print(value)
#output will be HelloLama

#To multiply the string we can do 
multiple_value = var_name_1 * 2
print(multiple_value)
#output will be HelloHello

#It also has some methods. For all methods visit this link: https://realpython.com/python-strings/
print(chr(var_name_3))  #converts integer to ASCII character #output 97
print(ord("a")) #converts character to integer #output 97
print(len(var_name_1)) #says len of string
print(str(var_name_1)) #converts to string

#They can also be accessed with index
print(var_name_1[0]) #output H

#We can do slicing to the string
# [start:end:step] #default step 1

print(var_name_1[1:3]) #output will be el



