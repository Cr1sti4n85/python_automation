file = open("spider.txt")
# print(file.readline())
# print(file.readline())
print(file.read())
file.close()

with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().lower()) #strip method removes newline characters

file = open("spider.txt")
lines = file.readlines() #creates a list of lines in the file
file.close()
lines.sort()
print(lines)