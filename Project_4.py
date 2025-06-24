'''       номер посылки  139496394    '''
'''       ссылка на файл с отчетами https://docs.google.com/document/d/1JYjHDcvFxBt9Nh-kjAhBz3AciVzx32sEapWY-E1_YLE/edit?usp=sharing    '''
def serv_del(array: list, limit: int) -> int:
    ls: list = sorted(array, reverse=True)
    len_arr: int = len(ls)
    res: list = []
    while len_arr > 0:
        breaked: bool = False
        for k in range(len_arr):
            if breaked == True:
                break
            for l in range(k+1, len_arr):
                if ls[k] + ls[l] <= limit:
                    res.append((ls[k], ls[l]))
                    ls.pop(l)
                    ls.pop(k)
                    len_arr = len(ls)
                    breaked = True
                    break
            if breaked == False:
                res.append((ls[k]))
                ls.pop(k)
                len_arr = len(ls)
                breaked = True
                break
    return len(res)

if __name__ == '__main__':
    array = list(map(int, str.split(input())))       # '2 5 3 4 1 5 3 4 1 2 5')))  #input())))  # '1 0 2 3 4'
    limit = int(input())                    # int(input())
    print(serv_del(array, limit))