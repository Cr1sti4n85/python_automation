
def greeting(name, dept):
    print("Hello " + name)
    print("Your department is " + dept)


greeting("Cristian", "Networking")

numbers = [4, 2, 18, 9]

#built.in functions
print(sorted(numbers))
print(min(numbers))
print(max(numbers))


#returning values
def area_triangle(base, height):
    return base*height/2

area = area_triangle(12, 20)
print(area)

def convert_seconds(sec: int):
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    remaining_seconds = sec - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(12000)


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Cris")
lucky_number("Cameron")