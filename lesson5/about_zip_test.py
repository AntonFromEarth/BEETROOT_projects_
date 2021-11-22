'''
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

print(list(zip(list1, list2)))
print(zip(list1, list2))
'''
# средний балл на экзамене
alice = [89, 78, 90]
bob = [94, 93, 77]
joe = [76, 90, 72]

tests = list(zip(alice, bob, joe))
for test in tests:
	print(sum(test)/len(test))

