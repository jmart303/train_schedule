from dataclasses import dataclass


class GetTrainSchedule:
	def __init__(self, cursor, train_name, departure_city, departure_date, departure_gate, arrival_city, arrival_date,
	             arrival_gate):
		self.train_name = train_name
		self.departure_city = departure_city
		self.departure_date = departure_date
		self.departure_gate = departure_gate
		self.arrival_city = arrival_city
		self.arrival_date = arrival_date
		self.arrival_gate = arrival_gate
		self.cursor = cursor

	def get_arrival_info(self, *args):
		departure_city = args[0]
		arrival_city = args[1]
		arrival_query = (
			f"SELECT * FROM train_schedule WHERE departure_city = '{departure_city}' AND arrival_city = '{arrival_city}'")
		self.cursor.execute(arrival_query)
		for arrival_data in self.cursor:
			print(arrival_data)

	def get_train_info(self, *args):

		self.cursor.execute()

	def get_schedule(self):

		self.cursor.execute()

	def date_lookup(self, *args):
		search_date = args[0]
		search_query = (f"SELECT * FROM train_schedule WHERE departure_date = '{search_date}'")

		self.cursor.execute(search_query)
		for i in self.cursor:
			print(i)

	def get_full_schedule(self):
		full_schedule_data = (f'{self.train_name} | {self.departure_gate} | {self.departure_city} | '
		                      f'{self.departure_date} | {self.arrival_city} | {self.arrival_date} | '
		                      f'{self.arrival_gate} ')
		return full_schedule_data
