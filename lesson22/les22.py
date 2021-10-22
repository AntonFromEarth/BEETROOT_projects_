
def linear_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [0, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [0, 0, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [0, 0, 0, 1]
    '''
    
    temp = array[:-shift]
    temp1 = [0 for i in range(shift)]
    temp1.extend(temp)
    return temp1 


def circular_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [4, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [3, 4, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [2, 3, 4, 1]
    '''
    
    temp = []

    for i in range(len(array)):
        temp.append(array[i-shift])
    return temp


def nested_parentheses(incoming: str) -> bool:
    '''
    Функція отримує рядок, який складається тільки зі знаків "(" або ")"
    Рядок вважається таким, що містить коректно вкладені скобки, якщо для
    кожної скобки "(" існує відповідна ")". 
    Функція повертає булевську змінну, яка показує, чи містить вхідний рядок
    тільки правильно вкладені скобки - True, чи ні - False
    incoming = "((())(())())" => True
    incoming = "" => True
    incoming = "(((())))" => True
    incoming = "())" => False
    incoming = "(()()(())" => False
    '''
    if incoming == "":
        return True
    elif incoming[0] == "(" and incoming[len(incoming)-1] == ")":
        if incoming.count("(") == incoming.count(")"):
            return True
    else:
        return False

if __name__ == '__main__':
    array = [1, 2, 3, 4]; shift = 2


    print(linear_shift(array, shift))

    print(circular_shift(array, shift))


    #incoming = "((())(())())"

    incoming = ""
    #incoming = "(((())))"
    #incoming = "())"
    #incoming = "(()()(())"
    #incoming = ")()("

    print(nested_parentheses(incoming))
