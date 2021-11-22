matrix = [[1,2,3],[4,5,6],[7,8,9]]
# transposed matrix
def transpose(initial):
	transposed = []

	for row in range(3):
		transposed.append([])
		for column in range(3):
			transposed[row].append(None)
	for row in range(3):
		for column in range(3):
			transposed[column][row] = initial[row][column]
	return transposed

transposed_matrix = transpose(matrix)
print(transposed_matrix)


"""
#finding of determinants
main = 1
secondary = 1
for row in range(3):
	for column in range(3):
		if row == column:
			element = matrix[row][column]
			main *= element
			#нам не нежно дальше перебирать по этому можно 
			# цикл закончит и выйти из второго for

			#break 
# у диагонали справа вверху вниз слева 3, 5, 7 
		if row + column == 2:
			element = matrix[row][column]
			secondary *= element




print(main)
print(secondary)
print("det=")
det = main-secondary
print(det)
"""


