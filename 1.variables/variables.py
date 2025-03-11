# Day 2: 30 Days of python programming

import operator 

#Declare a first name variable and assign a value to it
first_name = 'saba'
last_name = 'Mirjankar'
full_name = 'Saba Mirjankar'
country = 'India'
city  = 'Hubli'
age = 29
year = 2025
is_true = 'true'

#Declare multiple variable on one line
name = [first_name, last_name, country] = ['Saba', 'Mirjankar', 'India']

print(first_name)
print(name)

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(city))
print(type(age))
print(type(name))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print(len(first_name)==len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = operator.add(num_one,num_two)
print("addition", total)

#Subtract num_two from num_one and assign the value to a variable diff
diff = (num_one - num_two)
print("substraction" , diff)

#Multiply num_two and num_one and assign the value to a variable product
product = (num_one * num_two)
print("multiplication", product)

#Divide num_one by num_two and assign the value to a variable division
division = (num_one/num_two)
print("division", division)

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = (num_one % num_two)
print("remainder", remainder)

# power of num_two and assign the value to a variable exp
exp = operator.pow(num_one,num_two)
print("exponential", exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = operator.floordiv(num_one, num_two)
print("floor div", floor_division)

#The radius of a circle is 30 meters.
r = 30
pi = 3.14
area_of_circle = pi * r * r
#Calculate the circumference of a circle
circum_of_circle = 2 * pi * r
print("ara of circle" , area_of_circle)
print("Circumference of circle", circum_of_circle)

#Take radius as user input and calculate the area.
r = float(input("enter radius of circle\n"))
pi = 3.14
area = pi * r * r
print("area" , area)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter Firstname\n")
last_name = input("enter last name\n")
country = input("Enter country\n")
age = int(input("enter age\n"))

print(first_name, last_name, country, age)
