# Implement Bubble Sort

import time

numbers: list = []

for x in range(1, 1000 + 1):
    numbers.append(x)

def swap(x: int, y: int):
    return y, x

def bubble_sort(a: list):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if(a[j] > a[j + 1]):
                a[j], a[j + 1] = swap(a[j], a[j +1])
    return None
# start1: int = time.time()
# bubble_sort(numbers)
# print(numbers)
# print(f"{time.time() - start1} -- PRIMA VERSIONE")


# Improved one

def improved_bubble_sort(a: list):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if(a[j] > a[j + 1]):
                a[j], a[j + 1] = swap(a[j], a[j +1])
    return None

# start2: int = time.time()
# improved_bubble_sort(numbers)
# print(numbers)
# print(f"{time.time() - start2} -- SECONDA VERSIONE")

# Flag bubble sort

def flag_bubble_sort(a: list):
    for i in range(len(a)):
        swap_flag = False
        for j in range(len(a) - i - 1):
            if(a[j] > a[j + 1]):
                swap_flag = True
                a[j], a[j + 1] = swap(a[j], a[j +1])
        if swap_flag is False:
            return None
    return None

# start3: int = time.time()
# flag_bubble_sort(numbers)
# print(numbers)
# print(f"{time.time() - start3} -- TERZA VERSIONE")