''' Задание: написать программу, которая получает на вход массив и возвращает максимальное число 
блоков, на которое можно разбить этот массив так, чтобы сортировка отработала корректно. 
Блоки не меняют расположение между собой '''

def merge_sort(len_array, array):
    left = 0
    right = 0
    cnt = 0
    off = False
    while left < len_array:
        min_val = min(array[left:len_array])
        if array.index(min_val) == left:
            cnt += 1
            left += 1
            continue
        min_val_ind = max(array.index(min_val), right)
        max_val = max(array[left:min_val_ind + 1])
        right = max(min_val_ind, array.index(max_val))
        for val in range(min_val, max_val + 1):
            if val not in array[left:right + 1]:
                right = array.index(val)
                off = True
                break
        if off:
            off = False
            continue
        cnt += 1
        left = right + 1
    return cnt


if __name__ == '__main__':
    len_array = int(input())
    array = list(map(int, str.split(input())))  # '1 0 2 3 4'  input()
    print(merge_sort(len_array, array))