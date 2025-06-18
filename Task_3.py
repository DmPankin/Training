data = '0 1 2 3 4'
data = '4 3 2 1'
'''
Напишите функцию valid_mountain_array, которая будет принимать на вход массив 
с высотами и возвращать True или False в зависимости от того, «правильная» это гора 
или нет.
Если в массиве менее трёх элементов, такой массив не может описывать «правильную» гору.
'''

def valid_mountain_array():
    from sys import maxsize

    data = list(map(int,str.split(input())))
    change_dir = False
    up = data[1] > data[0]
    if up:
        pt_prev = -1
    else:
        pt_prev = maxsize
    
    if len(data) < 3:
        return False
    
    for pt in data:
        if (pt > pt_prev and up) or (pt < pt_prev and not up):
            pt_prev = pt
            continue
        if pt < pt_prev and up and not change_dir:
            pt_prev = pt
            up = False
            change_dir = True
            continue
        if (pt > pt_prev and not up) or (pt < pt_prev and up) or pt == pt_prev:
            return False
        
    return change_dir
            
if __name__ == '__main__':
    print(valid_mountain_array())