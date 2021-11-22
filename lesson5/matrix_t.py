"""
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

transponed = [
[1, 4, 7],
[2, 5, 8],
[3, 6, 9]
]
"""


matrix = [[1,2,3],[4,5,6],[7,8,9]]
#finding of determinants
main = 1
secondary = 1
transponed = []
for column in range(3):
	temp_row = []
	for row in matrix:
		temp_row.append(row[column])

	transponed.append(temp_row)


print("matrix=", matrix)
print("transponed = ", transponed)

for row in transponed:
	for element in row:
		print(element, end = ' ')
	print('')




