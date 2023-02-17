#!usr/bin/env python3

#this is a single line comment.
# python program to illustrate strings operations in python.
# name :mark.
# email :miraurimarkson@gmai.com.
# date :17th feb 2023.
#file :strings.py

poem = '''this is a poem about nothing
             its funny people laugh about nothing
'''

print(poem)

print(len(poem))

f_name = "mark"
s_name = "mirauri"
full_name = f_name + " " + s_name
age = 25 #years
print("my name is " + full_name + " and i am " +str(age)+ " years old")
print("my name is {} and i am {} years old".format(full_name.upper(),str(age)))
print("Hello from Mark. \n how are you? \n i am fine.")
print("Hello from Mark. \thow are you? \t i am fine.")