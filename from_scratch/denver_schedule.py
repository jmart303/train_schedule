class RetrieveSchedule:
	def __init__(self, train_name, departure_date_time, departure_city, departure_gate, arrival_date_time, arrival_city,
	             arrival_gate, on_time, cursor):
		self.train_name = train_name
		self.departure_date_time = departure_date_time
		self.departure_city = departure_city
		self.departure_gate = departure_gate
		self.arrival_date_time = arrival_date_time
		self.arrival_city = arrival_city
		self.arrival_gate = arrival_gate
		self.on_time = on_time
		self.cursor = cursor

	def get_arrival_info(self, *args):
		arrival_city = args[0]
		departure_city = args[1]

		arrival_query = (
			f"SELECT * FROM train_schedule WHERE departure_city = '{departure_city}' AND arrival_city = '{arrival_city}'")
		self.cursor.execute(arrival_query)

		for data in self.cursor:
			return data

	def get_departure_info(self):
		pass

	def get_gate_info(self):
		pass

	def get_train_info(self, *args):
		train = args[0]
		train_query = (f"select * from trains WHERE train_name = '{train}'");
		self.cursor.execute(train_query)
		for data in self.cursor:
			return data

	def get_full_schedule(self):
		full_schedule_data = (f'{self.train_name} | {self.departure_gate} | {self.departure_city} | '
		                      f'{self.departure_date_time} | {self.arrival_city} | {self.arrival_date_time} | '
		                      f'{self.arrival_gate} | {self.on_time}')

		return full_schedule_data
