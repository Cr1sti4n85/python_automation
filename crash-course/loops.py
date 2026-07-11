x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

def get_username():
    return input("Enter username: ")

def valid_username(username):
    return len(username) >= 3 and len(username) <= 10

username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()


def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))

for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

greeting = 'Hello'
for char in greeting:
	print(char)
   
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1

index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1

#List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

#Slicing strings
string1 = "Greetings, Earthlings"

print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
print(string1[-10:]) # Prints “Earthlings”

#Stride argument. This allows you to skip over the corresponding number of characters in your index, or if you’re using a negative stride, the string prints backwards.
# Prints “Getns atlns”
print(string1[0::2])

# Prints “sgnilhtraE ,sgniteerG”
print(string1[::-1])

greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"