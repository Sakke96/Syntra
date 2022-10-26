
def exercise1(array2D):
    sum = 0
    for i in array2D:
        for j in i:
            sum += j
    return sum
    

def exercise2():
    square_array = []
    for i in range(1, 21):
        square_array.append(i**2)
    print(square_array)

def exercise3(x, y, z):
    if x == y or y == z or z == x:
        return 0
    else:
        return x+y+z

def exercise4(array1, array2):
    sum_array = []
    for i in range(len(array1)):
        sum_array.append(array1[i]+array2[i])
    return sum_array
        

def exercise5(array):
    tuple_list = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] % 3 == 0:
                tuple_list.append((i,j))
    return tuple_list
                

    
array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]

print(exercise1(array))
exercise2()
print(exercise3(0,1,2))
print(exercise4([1,2,3,4],[2,3,4,5]))
print(exercise5(array))

