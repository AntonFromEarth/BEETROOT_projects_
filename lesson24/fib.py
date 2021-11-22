#Реалізувати рекурсивну функцію, яка виводитиме перші 20
# чисел з послідовності Фібоначчі

'''
fib1 = fib2 = 1
#n = int(input())
n=10
if n < 2:
    quit()
print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
 
print()
'''

'''
def fib_fu(index):
	
	if index == 0 or index == 1:
		return index
	#print(index)
	#return fib_fu(index-1) + fib_fu(index-2)
	else:
		fib_fu(index-1) + fib_fu(index-2)
'''

'''
def fib_fun(index):
	if index == 0 or index == 1:
		return index
	else:
		return fib_fun(index-1) + fib_fun(index-2)
		#fib_fun(index-1) + fib_fun(index-2)
'''
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12,  13,  14,  15,  16,  17,   18,   19,   20,   21,    22 

def fib_fu(n):
	pass


print(fib_fu(7))

#fib_fun(7)

