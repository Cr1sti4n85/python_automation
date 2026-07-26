import re
result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", "Lovelace, Ada")

if result: 
    print(result)
    print(result.groups()) #returns a tuple of the matched groups
    print(result[0])
    print(result[1])
    print(result[2])
    print("{} {}".format(result[2], result[1]))

def rearrange_name1(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
print(rearrange_name1("Kenndy, John F."))
