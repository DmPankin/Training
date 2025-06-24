''' СОРТИРОВКА ПО ШАБЛОНУ'''
''' Ваша задача — написать программу, которая:
будет принимать на вход массив для сортировки и массив-шаблон, в соответствии с которым должна быть выполнена сортировка;
вернёт массив, отсортированный в соответствии с шаблоном  '''

#n = 11
#data = list(map(int, str.split('2 3 1 3 2 4 6 7 9 2 19')))
#m = 6
#pat = list(map(int, str.split('2 1 4 3 9 6')))

def insertion_sort(n, data, m, pat):
    dct_not = {}
    dct_in = {}
    for val in data:
        if val in pat:
            dct_in[val] = data.count(val)
        else:
            dct_not[val] = data.count(val)

    # dc_in = dict(sorted(dct_in.items(), key=lambda item: item[0]))
    dc_in = {}
    for k in pat:
        dc_in[k] = dct_in[k]
    dc_not = dict(sorted(dct_not.items(), key=lambda item: item[0]))
    dc_in.update(dc_not)
    str_out = ''
    for k, v in dc_in.items():
        str_out += (' ' + str(k)) * v
    return str_out.strip()

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, str.split(input())))
    m = int(input())
    pat = list(map(int, str.split(input())))
    print(insertion_sort(n, data, m, pat))



''' 
        # Создаём массив для подсчёта вхождений каждого значения.
    max_in = max(pat)
    cnt_in = [0] * (max_in + 1)
    cnt_not = [0] * (m + 1)
    # Перебираем массив по элементам.
    for item in data:
        if item in pat:
        # Для каждого значения массива array увеличиваем счётчик 
        # в соответствующей ячейке массива count.
        # Например, увидели в array значение 2 - добавляем единицу к значению count[2].
            cnt_in[item] += 1
        else:
            cnt_not[item] += 1

    # Объявляем результирующий список:
    sorted_array = []
    # Перебираем все уникальные элементы в списке count.
    for item in range(maximum + 1):
        # Добавляем в sorted_array уникальный элемент столько раз, 
        # сколько он встретился в исходном массиве.
        sorted_array += [item] * count[item]
    return sorted_array


arr = [8, 1, 4, 10, 4, 1, 4, 7, 6, 8, 6, 4, 5, 10, 1, 0, 5, 4, 9, 7]
result = counting_sort(arr, 10)

    # Проходим по всем элементам массива, начиная со второго.
    for i in range(1, n):
        # Сохраняем текущий элемент в переменную current.
        if data[i] in pat:
            current = data[i]
            # Сохраняем индекс предыдущего элемента в переменную prev (от previous - предыдущий).
            prev = i - 1
            # Сравниваем current с предыдущим элементом и двигаем предыдущий элемент на одну позицию вправо, 
            # пока он больше current и не достигнуто начало массива.
            while prev >= 0 and data[prev] > current:
                data[prev + 1] = data[prev]
                prev -= 1
            # Вставляем current в отсортированную часть массива на нужное место.
            data[prev + 1] = current 
            print(f'Шаг {i}, отсортировано элементов: {i + 1}, {data}')
        else:
            t = data.pop(i)
            data.append(t)
    print(data)    

'''


