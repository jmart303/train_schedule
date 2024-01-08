# use item() for dictionaries
# use generator
# use starmap and map
# write TEST !
# caching
# set
#
# import json
#
# with open('prod_collectors_p1_2021-05-12.json', 'r') as file:
# 	data = json.load(file)
# 	collectors = data['collectors']
# 	for collector in collectors:  # grabs the dictionary
# 		for k, v in collector.items():
# 			if k == 'name':
# 				print(v)


# with open('prod_collectors_p1_2021-05-12.json', 'r') as file:
# 	data = json.load(file)
# 	collectors = data['collectors']
# 	for collector in collectors:
# 		if collector['name']:
# 			print(collector['name'])

# Generators


# def get_name():
# 	with open('prod_collectors_p1_2021-05-12.json', 'r') as file:
# 		data = json.load(file)
# 		collectors = data['collectors']
#
# 		for collector in collectors:  # grabs the dictionary
# 			for k, v in collector.items():
# 				if k == 'name':
# 					yield v
#
#
# lines = get_name()
#
# for line in lines:
# 	print(line)
# 	# print(line)

# map

def addition(n):
	return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


# starmap

import multiprocessing
import json


def get_id_list():
	import random
	id_list = []
	for i in range(15):
		test_id = random.randint(1, 100000)
		id_list.append(test_id)
	id_list.append('181406250')
	return id_list


def get_my_collector():
	collector_data_list = []

	with open('prod_collectors_p1_2021-05-12.json', 'r') as file:
		data = json.load(file)
		for lines in data['collectors']:
			collector_data_list.append(lines)
	return collector_data_list


def results(collector_id, collector_data_list):
	for line in collector_data_list:
		if collector_id in line:
			print('HY')



def map_test():
	random_id_list = get_id_list()
	# print(random_id_list)
	collector_data_list = get_my_collector()

	job_arguments = [
		[my_id, collector_data_list]
		for my_id in random_id_list
	]

	with multiprocessing.Pool(processes=10) as p:
		my_collector = p.starmap(results, job_arguments)
	# 	# print(my_collector)


map_test()
