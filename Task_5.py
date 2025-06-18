'''Напишите функцию is_correct_bracket_seq(), которая принимает на вход скобочную 
последовательность и возвращает True, если последовательность правильная, и False — 
в остальных случаях.
'''
line = '({[]})([])'  #     line = "{()}[]"

def check_brackets():
    open_br = ["(", "{", "["]   # input()  
    stack = []     
    line = input()
    for char in line:
        if char in open_br: # если символ - открывающая скобка, то вносим в стек
            list.append(stack, char)
        else:        # если закрывающая
            if stack == []:    # если стек пустой
                return False
            cur_ch = list.pop(stack)    # вынимаем символ
            if cur_ch == '(':
                if char != ')':
                    return False
            if cur_ch == '{':
                if char != '}':
                    return False
            if cur_ch == '[':
                if char != ']':
                    return False

    # проверяем пустой лист
    if stack != []:
        return False
    return True


if __name__ == "__main__":

    print(check_brackets())