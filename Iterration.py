class FlatIterator:
	def __init__(self, rest_list):
		tmp = []
		for id in rest_list:
			for id2 in id:
				tmp.append(id2)
		self.rest_list = tmp

	def __iter__(self):
		self.coursor = -1
		return self

	def __next__(self):
		self.coursor += 1
		if self.coursor == len(self.rest_list):
			raise StopIteration
		return self.rest_list[self.coursor]

def flat_generator(rest_list):
	for id in rest_list:
		for id2 in id:
			yield id2

# def flat_generator_sort(rest_list):
# 	global new_list
# 	for id in rest_list:
# 		if type(id) == list:
# 			flat_generator_sort(id)
# 		else:
# 			new_list.append(id)
# 	return
#
# def flat_generator3(rest_list):
# 	# flat_generator_sort(nested_list_2)
#
# 	for id in rest_list:
# 		yield id

def flat_generator_sort(rest_list):
	global new_list
	for id in rest_list:
		if type(id) == list:
			flat_generator_sort(id)
		else:
			new_list.append(id)
	return

def flat_generator3(rest_list):
	global new_list
	new_list = []
	flat_generator_sort(rest_list)
	for id in new_list:
		yield id

if __name__ == '__main__':
	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None]
	]

	nested_list_2 = [
		['a', 'b', 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None, [10, ['new', 'old'], 11]],
	]


	print('Задача 1.\n')
	for item in FlatIterator(nested_list):
		print(item)

	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)

	print('\nЗадача 2.\n')

	for item in flat_generator(nested_list):
		print(item)

	print('\nЗадача 4.\n')

	for item in flat_generator3(nested_list_2):
		print(item)