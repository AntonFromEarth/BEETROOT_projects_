# 
"""
linked list. каждый узел node связан
 с последующим
"""

class Node:

	def __init__(self, data, next_node = None):
		self.data = data
		self.next_node = next_node


class LinkedList:

	def __init__(self, root=None):
		self.root = root
		self.size = 0

	def add(self, data):
		new_node = Node(data, self.root)
		self.root = new_node
		self.size += 1

	def __repr__(self):
		next_n = self.root
		res = ""

		while next_n:
			res += str(next_n.data) + " -> "
			next_n = next_n.next_node
		return res

my_list = LinkedList()
my_list.add(5)
print(my_list)

my_list.add(9)
print(my_list)

my_list.add(7)
print(my_list)
