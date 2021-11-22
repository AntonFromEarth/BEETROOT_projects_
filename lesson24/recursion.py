
def up_and_down(num):
	print("Level {}, located at: {}". format(num, id(num)))
	if (num<4):
		up_and_down(num+1)
	print("LEVEL {}, located at: {}". format(num, id(num)))

up_and_down(1)

import sys

for d in sys.path:
    print(d)