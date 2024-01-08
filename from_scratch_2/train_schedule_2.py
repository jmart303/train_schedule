import mysql.connector
import get_schedule_2
from datetime import datetime







def main():
	main_query = ("SELECT * FROM train_schedule")

	cursor.execute(main_query)

	for data in cursor:
		schedule_data = {
			'train_name': data[1],
			'departure_city': data[2],
			'departure_date': data[3],
			'departure_gate': data[4],
			'arrival_city': data[5],
			'arrival_date': data[6],
			'arrival_gate': data[7]
		}

		train_schedule = get_schedule_2.GetTrainSchedule(
			schedule_data['train_name'], schedule_data['departure_city'],
			schedule_data['departure_date'], schedule_data['departure_gate'],
			schedule_data['arrival_city'], schedule_data['arrival_date'],
			schedule_data['arrival_gate'])

		arrival_data = train_schedule.get_arrival_info(cursor, departure_city, arrival_city)
		display = (f'Train: {arrival_data[0]} | Departure Date: {arrival_data[1]} | '
		           f'Departure City: {arrival_data[2]} | Departure Gate: {arrival_data[3]} | '
		           f'Arrival Date: {arrival_data[4]} | Arrival City: {arrival_data[5]} | '
		           f'Arrival Gate: {arrival_data[6]} | On Time: {arrival_data[7]}')
		print(display)





if __name__ == '__main__':
	conn = mysql.connector.connect(
		host='localhost',
		database='train_schedule',
		user='root',
		password='bik3rm0n'
	)

	cursor = conn.cursor(buffered=True)
	# cursor.execute(query)

	# USER INPUT
	departure_city = 'denver'
	arrival_city = 'bozeman'
	gate = ''
	# search_date = '2023-11-05 4:30:00'
	date = datetime.now()

	main()
# insert_schedule()

