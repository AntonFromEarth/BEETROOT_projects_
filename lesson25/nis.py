'''
Euler problem No.5
3. 2520 найменше число, що ділиться на будь-яке число від 1 до 10 без залишку. 
Яке найменше позитивне число ділиться без залишку на всі числа від 1 до 20?
Answer: 232792560
'''
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

high = 10
number = 1
flag = False
while True:
	for div in range(1, high+1):
		if number%div == 0:
			#number += 1
			print(number)
			if div == high:
				flag = True
				break
			continue
	number += 1
	if flag:
		break

print(number)
print("@@@@@@@@@@@@@@@@@@@@")
i=2520
c=False
r=(3,4,6,7,8,9,11,12,13,14,15,16,17,18,19)
while c is False:
    str(i)
    for j in r:
        if i%j==0:
            c=True
            continue
        else:
            c=False
            break
    i+=10

print(i-10)
