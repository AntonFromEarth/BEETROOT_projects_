students = ['Alice', 'Bob', 'Joe']
test_points = [[100, 75, 81], [94, 75, 63],[71, 84, 83]]

student_results = dict(zip(students, test_points))
print(student_results)
print('')
# у каких сткдкнтов средняя оценка выше 80?
for name, points in student_results.items():
	if sum(points)/len(points) > 80:
		print(name)