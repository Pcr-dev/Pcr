# importing python in-built library called random for randomize the password sequence
import random

# printing to the user screen a welcome message
print("Welcome to the password generator")

# creating a var that holds the possible alfanumerical characters that will help to generate the password
password_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_?<>.'

# opting the user how much password they want to generate
number_of_password = int(input("enter the number of passwords You want ie. 1 or 2 or many ! "))
print(number_of_password)

# Asking the user to enter length of the password
password_length = int(input("enter how many characters You need to create a password "))
print(password_length)

# say to user this is all Your passwords
print("\nThis is the passwords based on Your needs")

#invoking for loop to print the password
for pwd in range(number_of_password):
    password = ''
    for i in range(password_length):
        password += random.choice(password_character)
print(password)
