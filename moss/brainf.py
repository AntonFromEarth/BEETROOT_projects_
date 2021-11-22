#########################################################################
"""Более сложный интерпретатор"""


"""
Translator of BRAINFUCK
Hello World!
14.09.2021
"""
# version 1


brainf_string = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++\
 .>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.\
 ------.--------.>+.>.'
 
'''
 
brainf_string = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
''' 
 
def do_loop( fu_brainf_string, fu_symbol_list, fu_index_in_brainf_string, fu_inddex_in_symbol_list ):
    left_square_bracket_index = fu_index_in_brainf_string
    loop_symbol_list_index = fu_inddex_in_symbol_list
    
    while fu_symbol_list[loop_symbol_list_index]:
        fu_index_in_brainf_string += 1
        
        print("in fu 1")
        
        if fu_brainf_string[fu_index_in_brainf_string] == "+":
            fu_symbol_list[fu_inddex_in_symbol_list] += 1
        
        elif fu_brainf_string[fu_index_in_brainf_string] == "-":
            fu_symbol_list[fu_inddex_in_symbol_list] -= 1
            
        elif fu_brainf_string[fu_index_in_brainf_string] == ">":
            fu_inddex_in_symbol_list += 1
        
        elif fu_brainf_string[fu_index_in_brainf_string] == "<":
            fu_inddex_in_symbol_list -= 1
            
        elif fu_brainf_string[fu_index_in_brainf_string] == ".":
            print(fu_symbol_list[fu_inddex_in_symbol_list])
            
        elif fu_brainf_string[fu_index_in_brainf_string] == "[":
            print("in fu-2")
            fu_brainf_string, fu_symbol_list, fu_index_in_brainf_string, fu_inddex_in_symbol_list = do_loop( fu_brainf_string, fu_symbol_list, fu_index_in_brainf_string, fu_inddex_in_symbol_list ) 
        
        elif fu_brainf_string[fu_index_in_brainf_string] == "]": # возвращает в начало ветвления, то есть сразу в ячейку после знак "["
            right_square_bracket_index = fu_index_in_brainf_string
            fu_index_in_brainf_string = left_square_bracket_index
#            fu_index_in_brainf_string = left_square_bracket_index + 1
        
#        fu_index_in_brainf_string += 1
        
        
        
    return fu_brainf_string, fu_symbol_list, fu_index_in_brainf_string, fu_inddex_in_symbol_list     
 
 
my_num = 0
my_list = []
my_str = ''

symbol_list = [0 for i in range(brainf_string.count('>'))] # список члены которого будут ячейками с записанным в них значением выглядит так: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
index_in_brainf_string = 0 # счет и обозначение на каком из элементов строки с символами мы находимся
inddex_in_symbol_list = 0

print("symbol_list at start:",symbol_list)
print("len(brainf_string):",len(brainf_string))
print("brainf_string.count('>')", brainf_string.count('>'))
print("brainf_string.count('<')", brainf_string.count('<'))
#print("type(brainf_string[17])", type(brainf_string[17]))

while True:
    if brainf_string[index_in_brainf_string] == "+":
        symbol_list[inddex_in_symbol_list] += 1
        
    elif brainf_string[index_in_brainf_string] == "-":
        symbol_list[inddex_in_symbol_list] -= 1
        
    elif brainf_string[index_in_brainf_string] == ">":
        inddex_in_symbol_list += 1
    
    elif brainf_string[index_in_brainf_string] == "<":
        inddex_in_symbol_list -= 1
        
    elif brainf_string[index_in_brainf_string] == ".":
        my_str += chr(symbol_list[inddex_in_symbol_list])
        print(chr(symbol_list[inddex_in_symbol_list]))
        
    elif brainf_string[index_in_brainf_string] == "[":
        brainf_string, symbol_list, index_in_brainf_string, inddex_in_symbol_list = do_loop( brainf_string, symbol_list, index_in_brainf_string, inddex_in_symbol_list )
        
        
    index_in_brainf_string += 1 # после всех сравнений пройти к следующему значению в списке "brainf_string"
    
    if index_in_brainf_string == len(brainf_string): # выйти из ветвления если дошли до конца списка "brainf_string"
        break

print("The strin is: ", my_str)
print("symbol_list at end:",symbol_list)


