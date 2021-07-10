# Write a python program to check whether a character is uppercase or lowercase alphabet

#initalizing value
a="suraj"

#comparision of value
if a==a.upper():
    print(f"{a} is a upper case alpahbet")
elif a==a.lower():
    print(f"{a} is a lower case alphabet")
elif a==a.title():
    print(f"{a} is a title case alphabet")
else:
    print(f"{a} is a mixed case alphabet")