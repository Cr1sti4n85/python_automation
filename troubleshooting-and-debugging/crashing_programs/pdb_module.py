import pdb


def add_numbers(a, b):
    result = a + b
    pdb.set_trace()  # This will set a breakpoint in the code
    return result


print(add_numbers(3, 4))