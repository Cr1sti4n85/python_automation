file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

print(file_counts["txt"])

print("jpg" in file_counts)
print("html" in file_counts)

file_counts["cfg"] = 8
print(file_counts)

del file_counts["cfg"]
print(file_counts)

for extension in file_counts:
  print(extension)

for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
  print(value)

pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}  


print(pet_dictionary.get("dogs", 0))

#return a dictionary with the users as keys and a list of their groups as values. 
def groups_per_user(group_dictionary):
	user_groups = {}
	for group, users in group_dictionary.items():
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			if group not in user_groups[user]:
				user_groups[user].append(group)

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

def count_numbers(text):
  dictionary = {} 
  for char in text:
    if char.isnumeric():
      if char not in dictionary:
          dictionary[char] = 0
      dictionary[char] += 1
  return dictionary

print(count_numbers("1001000111101"))

print(count_numbers("Math is fun! 2+2=4"))

print(count_numbers("This is a sentence."))

print(count_numbers("55 North Center Drive"))