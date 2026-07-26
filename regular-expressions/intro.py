import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result1 = re.search(regex, log)
if result1: #result might be None if no match is found
    print(result1[1])


result2 = re.search(r"aza", "plaza")
print(result2)

print(re.search(r"aza", "maze"))

print(re.search(r"^x", "xenon")) 

print(re.search(r"p.ng", "Penguin", re.IGNORECASE))


print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

#any character that is not a letter
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) 
#any character that is not a letter or a space
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))