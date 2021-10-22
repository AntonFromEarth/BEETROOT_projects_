import unittest
#import les22
from les22 import linear_shift, circular_shift, nested_parentheses

class TestLess22(unittest.TestCase):
	def test_linear_shift(self):
		array = [1, 2, 3, 4]; shift_1 = 1; shift_2 = 2
		test_list=linear_shift(array, shift_1)
		self.assertEqual(test_list, [0,1,2,3])
		test_list=linear_shift(array, shift_2)
		self.assertEqual(test_list, [0,0,1,2])


	def test_circular_shift(self):
		array = [1, 2, 3, 4]; shift_1 = 1; shift_2 = 2
		test_list=circular_shift(array, shift_1)
		self.assertEqual(test_list, [4,1,2,3])
		test_list=circular_shift(array, shift_2)
		self.assertEqual(test_list, [3,4,1,2])

	def test_nested_parentheses(self):
		incoming_t_1 = "((())(())())"
		incoming_t_2 = ""
		incoming_t_3 = "(((())))"
		incoming_f_1 = "())"
		incoming_f_2 = "("
		incoming_f_3 = incoming = ")()("
		self.assertTrue(nested_parentheses(incoming_t_1))
		self.assertTrue(nested_parentheses(incoming_t_2))
		self.assertTrue(nested_parentheses(incoming_t_3))
		self.assertFalse(nested_parentheses(incoming_f_1))
		self.assertFalse(nested_parentheses(incoming_f_2))
		self.assertFalse(nested_parentheses(incoming_f_3))



if __name__ == '__main__':
    unittest.main()