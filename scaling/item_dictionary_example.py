import csv

# print dictionary values with items()
my_dict = {
		'car_model': 'honda',
		'transmission': '4-wheel',
		'color': 'black'
	}

my_dict.items()
print(my_dict)


#  print key and value through for loop
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

