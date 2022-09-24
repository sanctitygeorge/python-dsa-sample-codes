#This program takes a number as a value as an input and prints the odd and even numbers from the number
max = int(input("Enter max number: "))

#Declare an Empty array for the odd numbers
odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)


#Declare an Empty array for the even numbers
even_numbers = []

for k in range(1, max):
    if k % 2 == 0:
        even_numbers.append(k)
print("Even numbers:", even_numbers)