n=10
data = '1 1 5 7 8 8 11 45 45 50'


def main():
    ''' устранение дубликатов через список'''
    import sys

    n = sys.stdin.readline().rstrip()
    n = int(n)
    data = sys.stdin.readline().rstrip()  
    # формируем список данных
    data_lst = str.split(data)
    result = []
    prev_num = ''
    for num in data_lst:
        # если текущее и предыдущее значение разные, добавляем в результирующий список
        if num!= prev_num:
            result.append(num) 
        prev_num = num
    # выводим на печать сконкатенированный список + размноженное подчеркивание с пробелом
    print(' '.join(result) + ' _' * (n - len(result)))

if __name__== '__main__':
    main()


def main():
    '''устранение дубликатов через множество'''
    import sys

    # n = int(input())
    # data = input()
    n = sys.stdin.readline().rstrip()
    n = int(n)
    data = sys.stdin.readline().rstrip()  
    # для выделения уникальных чисел переводим список значений во множество
    data_set = set(list(map(int, str.split(data))))
    # определяем мощность множества
    set_len = len(data_set)
    # data_list = list(data_set)
    # формируем список строк из множества
    data_lst = list(data_set)
    data_lst.sort()
    data_str = list(map(str,data_lst))
    # выводим на печать сконкатенированный список + размноженное подчеркивание с пробелом
    print(' '.join(data_str) + ' _' * (n - set_len))

if __name__== '__main__':
    main()