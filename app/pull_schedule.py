import mysql.connector
import get_schedule
import sys


def insert_data(new_train):
	train_query = (f"SELECT * from trains")
	cursor.execute(train_query)
	for trainName in cursor:
		if new_train['trainName'] in trainName[2]:
			print(f'{trainName[2]} already exists')
			sys.exit(1)

	name = new_train['trainName']
	color = new_train['trainColor']
	current_capacity = new_train['current_capacity']
	capacity = new_train['capacity']
	print(name, color, current_capacity,capacity)

	insert_sql = "INSERT INTO trains (trainName, trainColor, current_capacity, capacity) VALUES(%s, %s, %s, %s)"
	values = name, color, current_capacity, capacity

	cursor.execute(insert_sql, values)
	conn.commit()
	print(f'inserted {cursor.rowcount} rows')


def main():
	data_query = ("SELECT * FROM schedule INNER JOIN trains USING (trainName)")
	cursor.execute(data_query)
	try:
		for data in cursor:
			schedule_data = {
				'train': data[0],
				'arrival_time': data[2],
				'arrival_time': data[2],
				'destination_city': data[3],
				'departure_time': data[4],
				'departure_city': data[5],
				'gate': data[6]
			}

			scheduled_data = get_schedule.QueryTrains(cursor, schedule_data['train'], schedule_data['gate'],
			                                          schedule_data['arrival_time'],
			                                          schedule_data['departure_city'], schedule_data['departure_time'],
			                                          schedule_data['destination_city'])

			if dest_city and depart_city:
				arrivals = scheduled_data.get_arrival_data(dest_city, depart_city)
				if arrivals is not None:
					arrival_time = arrivals[0]
					print(f'train from {depart_city} to {dest_city} will arrive at {arrival_time}')
					sys.exit(0)
				else:
					print('No Results from search')
					sys.exit(1)
			if train and dest_city:
				train_info = scheduled_data.get_train(train, dest_city)
				if train_info is not None:
					display = f"Train: {train_info[0]} {train}| Gate: {train_info[6]} | Departure City: {train_info[3]} | Departure Time: {train_info[4]} | Destination City:{train_info[5]} | Arrival Time: {train_info[2]}"
					print(display)
					sys.exit(0)
				else:
					print('No Results for train and destination')
					sys.exit(1)
			if train:
				train_capacity = scheduled_data.get_train_capacity(train)
				for train_data in train_capacity:
					# print(train_data)
					display = f" Train Name: {train_data[0]}  | Gate: {train_data[1]} | Destination: {train_data[2]} | train capacity: {train_data[3]}"
					print(display)

			else:
				full_schedule = scheduled_data.get_all_schedule()
				print(full_schedule)
	except Exception as error:
		print(f'Error {error}')


if __name__ == '__main__':
	conn = mysql.connector.connect(
		host='localhost',
		database='train_schedule',
		user='root',
		password='bik3rm0n'
	)
	cursor = conn.cursor(buffered=True)

	# user input from front-end
	dest_city = ''
	depart_city = ''
	train = 'mikey_movers'
	main()

	# new_train = {
	# 	'trainName': 'flying_bob',
	# 	'trainColor': 'purple',
	# 	'current_capacity': 0,
	# 	'capacity': 600
	# }
	#
	# insert_data(new_train)
