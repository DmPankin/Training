arr = [6, 5, 3, 1, 8, 7, 2, 4]

def bubble_sort(data):
    # пузырьковый алгоритм сортировки
    swapped = False
    last_ind = len(arr) - 1
    while last_ind > 0:
        for i in range(last_ind):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        if swapped == True:
            last_ind -= 1
        else:
            break
    return data

print(bubble_sort(arr))