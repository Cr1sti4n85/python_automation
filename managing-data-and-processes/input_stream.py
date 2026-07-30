import os

name = input("Please enter your name: ")
print("Hello, " + name)

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("Welcome to this time converter")
cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input("Do you want to do another conversion? [y to continue] ")
    
print("Goodbye!")

#Environment variables
print("HOME: " + os.environ.get("HOME", "Not found"))
print("SHELL: " + os.environ.get("SHELL", "Not found"))
print("PATH: " + os.environ.get("PATH", "Not found"))