def max_uniq():
    '''
    Напишите программу, которая принимает на вход строку и находит в ней наибольшую 
    длину подстроки, в которой нет повторяющихся символов. Программа должна вернуть 
    натуральное число — длину этой подстроки.
Используйте метод скользящего окна для решения задачи. Если в строке встретится дубликат, 
запомните длину получившейся подстроки и начинайте строить окно заново.
    '''
    data = input()
    max_len = 0


    cur_str = ''
    for val in data:
        if val not in cur_str:
            cur_str += val
            max_len = max(len(cur_str), max_len)
        else:
            pos = cur_str.find(val)
            cur_str = cur_str[cur_str.find(val) + 1:] + val

    return max_len

if __name__ == '__main__':
    print(max_uniq())    


