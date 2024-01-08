import mysql.connector
import denver_schedule


def main():
	schedule_data = {}
	query_schedule = ("SELECT * FROM train_schedule")

	cursor.execute(query_schedule)
	for data in cursor:
		schedule_data = {
			'train_name': data[1],
            'departure_date_time': data[2],
            'departure_city': data[3],
			'departure_gate': data[4],
			'arrival_date_time': data[5],
			'arrival_city': data[6],
			'arrival_gate': data[7],
			'on_time': data[8]
		}

		get_train_data = denver_schedule.RetrieveSchedule(
			schedule_data['train_name'], schedule_data['departure_date_time'],
			schedule_data['departure_city'], schedule_data['departure_gate'],
			schedule_data['arrival_date_time'], schedule_data['arrival_city'],
			schedule_data['arrival_gate'], schedule_data['on_time'], cursor
		)

		if arrival_city and departure_city:
			get_schedule_data = get_train_data.get_arrival_info(arrival_city, departure_city)
			display = (f'Train: {get_schedule_data[1]} | Departure Date: {get_schedule_data[2]} | '
			           f'Departure City: {get_schedule_data[3]} | Departure Gate: {get_schedule_data[4]} | '
			           f'Arrival Date: {get_schedule_data[5]} | Arrival City: {get_schedule_data[6]} | '
			           f'Arrival Gate: {get_schedule_data[7]} | On Time: {get_schedule_data[8]}')
			print(display)
		if train:
			train_data = get_train_data.get_train_info(train)
			print(train_data)
			# display = (f'Train: {train_data[0]} | Capacity: {train_data[1]} | Description: {train_data[2]} |'
			#            f' Current Capacity: {train_data[3]} | In Service: {train_data[4]}')
			# print(display)

		else:
			full_schedule = get_train_data.get_full_schedule()
			print(full_schedule)


if __name__ == '__main__':
	conn = mysql.connector.connect(
		host='localhost',
		database='train_schedule',
		username='root',
		password='bik3rm0n'
	)
	cursor = conn.cursor(buffered=True)
	# USER INPUTS
	arrival_city = 'bozeman'
	departure_city = 'denver'
	train = ''
	arrival_time = ''

	main()
