def count_num():
    '''
    Для каждого элемента требуется определить, сколько в массиве есть значений меньше, 
    чем текущее. Результат нужно записать во второй массив
        '''
    data = str.split(input())
    res = ''
    for i in range(len(data)):
        cnt = 0
        for j in range(len(data)):
            if int(data[j]) < int(data[i]) and i != j:
                cnt += 1
        res += ' ' + str(cnt)
    return res


if __name__ == '__main__':
    print(str.strip(count_num()))