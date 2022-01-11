
def linear_search(list, find_value):

    for i in range(len(list)):
        if (list[i] == find_value):
            return i
    return -1


list = [12, 23, 45, 56, 67, 78] 

print(linear_search(list,67))


