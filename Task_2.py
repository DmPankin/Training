data = '5 5 5 5'
val = '5'

def main():
    data = input()
    val = int(input())
    # формируем список данных
    data_lst = list(map(int, str.split(data)))
    # если искомое значение больше последнего значения списка, то индекс = последний+1
    if val > data_lst[len(data_lst)-1]:
        print(len(data_lst))
    if val < data_lst[0]:
        print(0)
    for num in range(len(data_lst)):
        # если текущее и искомое значение равны, выводим индекс текущего
        if data_lst[num] == data_lst[num-1] and num > 0:
            continue
        if data_lst[num] == val or data_lst[num] > val and data_lst[num-1] < val:
            print(num)


if __name__== '__main__':
    main()