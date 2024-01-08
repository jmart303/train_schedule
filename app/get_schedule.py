import mysql.connector


class QueryTrains:
	def __init__(self, conn, train, gate, arrival_time, dest_city, depart_time, depart_city):
		self.conn = conn
		self.train = train
		self.gate = gate
		self.arrival_time = arrival_time
		self.dest_city = dest_city
		self.depart_time = depart_time
		self.depart_city = depart_city

	def get_arrival_data(self, *args):
		cursor = self.conn
		dest_city = args[0]
		depart_city = args[1]

		arrival_query = (
			f"SELECT `ArrivalTime` FROM schedule WHERE `DestinationCity` = '{dest_city}' AND `DepartureCity` = '{depart_city}'"
			)
		cursor.execute(arrival_query)
		for results in cursor:
			return results

	def get_train(self, *args):
		cursor = self.conn
		train = args[0]
		dest_city = args[1]

		gate_query = (f"SELECT `gate` FROM schedule WHERE `trainName` = '{train}' and `DestinationCity` = '{dest_city}'"
		                 )
		cursor.execute(gate_query)
		try:
			for results in cursor:
				if results:
					gate = results[0]
					train_data_query = (f"SELECT * FROM schedule WHERE `gate` = '{gate}' and `trainName` = '{train}' ")
					cursor.execute(train_data_query)
					for train_info in cursor:
						return train_info
		except Exception as e:
			print(f'error getting train info {e}')

	def get_train_capacity(self, *args):
		train_list = []
		cursor = self.conn
		train = args[0]
		capacity_query = (f"select trainName, gate, destinationcity, capacity  FROM schedule INNER JOIN trains USING (trainName) WHERE schedule.trainName = '{train}'");
		cursor.execute(capacity_query)
		try:
			for results in cursor:
				train_list.append(results)
			return train_list
		except Exception as e:
			print(f'error getting capacity {e}')

	def get_all_schedule(self):
		full_schedule = f"Train: {self.train} | Gate: {self.gate} | Departure City: {self.dest_city} | Departure Time: {self.depart_time} | Destination City: {self.dest_city} | Arrival Time: {self.arrival_time}"
		return full_schedule
