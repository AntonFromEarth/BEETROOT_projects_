import json
import csv

TEST = []
test_list = [
"question", 
"answers", 
"correct_answer",
"grade"]


def load_from_json(file_path='data\\exam_1.json'):
    with open(file_path, 'r') as read_file:
        TEST.extend(json.load(read_file))

load_from_json()
#print("TEST", TEST)
print(test_list)
print("Len of TEST", len(TEST))
print("put ")
total_grade = 0
for test_field in range(len(TEST)):
    print()

    '''
    for sym in range(len(TEST[test_field][test_list[0]])):
        print("_", end="")
    print()
    '''

    print(TEST[test_field][test_list[0]])
    for question in TEST[test_field][test_list[1]]:
        print('  ',question)
    answer = input("Put number of your answer: ")
    if answer == TEST[test_field][test_list[2]]:
        total_grade += int(TEST[test_field][test_list[3]])

print("Your total grade is:", total_grade)


