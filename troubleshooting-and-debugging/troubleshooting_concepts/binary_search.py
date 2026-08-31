def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    counter = 0
    right = len(list) - 1
    while left <= right:
        counter += 1
        print(f"Iteración {counter}")
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

numList = list(range(1, 101))
print(numList)
key = 40
result = binary_search(numList, key)
print(f"El número {key} se encuentra en la posición: {result}")

# tenemos una lista del 1 al 100 y se elige como key el número 40

# primera iteración: 
# left = 0; right = 99; middle = 49
#list[middle] = 50 es > que 40. Por tanto, right = 49 - 1 = 48

#Segunda iteración:
#left = 0; right = 48; middle = 24
#list[middle] = 25 es < que 40. Por tanto, left = 24 + 1 = 25

#Tercera iteración:
#left = 25; right = 48; middle = 36
#list[middle] = 37 es < que 40. Por tanto, left = 36 + 1 = 37

#Cuarta iteración:
#left = 37; right = 48; middle = 42
#list[middle] = 43 es > que 40. Por tanto, right = 42 - 1 = 41

#Quinta iteración:
#left = 37; right = 41; middle = 39
#list[middle] = 40 es == que 40. Por tanto, retorna middle = 39
