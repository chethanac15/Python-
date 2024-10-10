def large(array, n):

    large = array[0]

    for i in range(1, n):

        if large < array[i]:

            large = array[i]

    return large

array = []

n = int(input("Enter the number of elements in the array"))

for i in range(0, n):

    element = int(input())

    array.append(element)

print(array)

answer = large(array, n)

print("Largest number in the array is", answer)
