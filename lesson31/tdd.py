import datetime

class Book:
	items = []

	def __init__(self, title, published, author):
		self.title = title
		self.published = published
		self.author = author
		Book.items.append(self)

	def __str__(self):
		return f'{self.author}\'s {self.title}'

	def __repr__()

	@classmethod
	def find_by_title(cls, title):
		find_books = []
		for item in cls.items:
			if title.lower() == item.title.lower():
				find_books.append(item)
		return find_books

	@classmethod
	def find_by_author(cls, author):
		find_books = []
		for item in cls.items:
			if author.lower() == item.author.lower():
				find_books.append(item)
		return find_books




