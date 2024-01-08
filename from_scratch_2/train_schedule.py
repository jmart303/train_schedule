import mysql.connector
import get_schedule
from datetime import datetime



def insert_schedule():
	train = 'jumping_jerry'
	departure_city = 'douglas'
	departure_date = '2024-01-01 1:00:00'
	departure_gate = '3E'
	arrival_city = 'suprise'
	arrival_date = '2024-01-01 15:30:00'
	arrival_gate = '5A'

	insert_sql = ("INSERT INTO train_schedule (train_name, departure_city, departure_date, departure_gate, arrival_city, arrival_date, arrival_gate) "
	              "VALUES (%s, %s, %s, %s, %s, %s, %s)")
	values = train, departure_city, departure_date, departure_gate, arrival_city, arrival_date, arrival_gate

	cursor.execute(insert_sql, values)
	conn.commit()



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

		for k, v in schedule_data.items():
			if k == 'train_name' and v == 'sliding_harry':
				print(f'Train Name {v}')

		# print(schedule_data.items())
		train_schedule = get_schedule.GetTrainSchedule(
			cursor, schedule_data['train_name'], schedule_data['departure_city'],
			schedule_data['departure_date'], schedule_data['departure_gate'],
			schedule_data['arrival_city'], schedule_data['arrival_date'],
			schedule_data['arrival_gate']
		                              )
		if departure_city and arrival_city:
			arrival_data = train_schedule.get_arrival_info(departure_city, arrival_city)
			display = arrival_data

		else:
			full_schedule = train_schedule.get_full_schedule()
			print(full_schedule)
		#
		# if search_date:
		# 	train_data = train_schedule.date_lookup(search_date)





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

