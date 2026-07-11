name = "Jaylen"
print(name[1])

print(name[0:2])

fruit= "pineapple"
print(fruit[:4])
print(fruit[4:])

print(fruit.index("n"))

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

pets="Cats & Dogs"
print("Dragons" in pets)
print("Cats" in pets)

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

print(replace_domain("cperezlecaros@gmail.com", "gmail.com", "yahoo.com"))

#string methods
print("Mountains".upper())
print("Mountains".lower())
print(" yes ".strip())
print("The number of times e occurs in this string is 4".count("e"))
print("Forest".endswith("rest"))
print("Forest".startswith("For"))
print("Forest".isnumeric())
print("12345".isnumeric())
print(int("12345") + int("54321"))
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))
string_to_list = "This is another example".split()
print(string_to_list)

#Formatting strings
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

print("Your lucky number is {number}, {name}.".format(name=name, number=number))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

fruit = "peaches"
weight = 3.0
per_pound = 2.99
output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
print(output)

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
  
subtotal = 100
tax_amt = subtotal * 0.19
total = subtotal + tax_amt

print("Subtotal:     ${:10,.2f}".format(subtotal))
print("Sales Tax:    ${:10,.2f}".format(tax_amt))
print("Total:        ${:10,.2f}".format(total))

#F strings
name = "Micah"

print(f'Hello {name}')

item = "Purple Cup"

amount = 5

price = amount * 3.25

print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')