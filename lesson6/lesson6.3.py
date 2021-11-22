#import math # import all library of math
#math.pi # обращение к фцнкции, аргументу pi

#from math import pi # importing of exact part of library "pi" from library
from math import pi as p # import spetial part "pi" of librarry but with our name "p"

# circle area calculation

def circle(rad):
	return p*pow(rad, 2)

print(circle(2))


def cyrcles_from_list(rads_list, return_type='dict'):
	if type(rads_list) is not list:
		return
	if return_type.lower() == "dict":
		a = {r: circle(r) for r in rads_list}
		print(a)
#		return {r: circle(r) for r in rads_list}
		return a
		
	'''	
		circle_dict = {}
		for r in rads_list:
			circle_dict[r] = circle(r)
		return circle_dict
#		pass
	'''
	#else:
	return [circle(r) for r in rads_list]

'''
	result = []
	for rad in rads_list:
		result.append(circle(rad))
	return result
'''


rads1 = [1, 2, 3]
rads2 = [2, 4, 6, 8]

print(cyrcles_from_list(rads1, 'dict'))
print(cyrcles_from_list(rads2))
print(cyrcles_from_list(3))



