import mysql.connector


if __name__ == '__main__':
	conn = mysql.connector.connect(
		host='localhost',
		database='train_schedule',
		user='root',
		password='bik3rm0n'
	)
	#
	cursor = conn.cursor(buffered=True)
	#
	# query = ("SELECT * FROM train_schedule")
	# join_query = ("SELECT train_name, arrival_gate, arrival_date_time, train_capacity, arrival_city, departure_city FROM train_schedule INNER JOIN trains USING (train_name) WHERE train_name = 'flying_bob'")
	#
	# cursor.execute(join_query)
	# for data in cursor:
	# 	print(data)


	insert_sql = ("INSERT INTO trains (train_name, train_capacity, train_descriptions, train_available_capacity, in_service) VALUES ('flashing_larry', '350', 'yellow', '0', 'no')")
	cursor.execute(insert_sql)
	conn.commit()




