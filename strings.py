# Escape characters allow you to do things you normally wouldn’t be able to do following the normal Python syntax rules.
# For example, you want to print this line in your code with double quotes around the title of the movie, “Titanic”.
# To do this, you simply add a backslash(\) before the character you want to escape.

from operator import concat

# Take Input from user and store in variable
name = input("What is your name: ")
type(name)
greet = "Hello " + name
print(greet)

# Escape characters
print ("Cory's favorite movie is \"Titanic\" and \"Banshe\"")

a = "John"
b = "Paul"
c = "1,2,3,4,5"

# Changing Case
a = a.upper()
print(a)

# Spit String
c = c.split(",")
print(c)

# String Replace
d = a.replace(a,b).upper()
print (d)

# Concatenate strings
print(concat(a, " " + b))