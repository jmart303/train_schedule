from dataclasses import dataclass
from datetime import datetime


@dataclass
class GetTrainSchedule:
	train_name: str
	departure_city: str
	departure_date: datetime
	departure_gate: str
	arrival_city: str
	arrival_date: datetime
	arrival_gate: str

	def get_arrival_info(self, *args):
		cursor = args[0]
		departure_city = args[1]
		arrival_city = args[2]
		arrival_query = (
			f"SELECT * FROM train_schedule WHERE departure_city = '{departure_city}' AND arrival_city = '{arrival_city}'")
		cursor.execute(arrival_query)
		for arrival_data in cursor:
			return arrival_data
	#
	# def get_train_info(self, *args):
	#
	# 	self.cursor.execute()
	#
	# def get_schedule(self):
	#
	# 	self.cursor.execute()
	#
	# def date_lookup(self, *args):
	# 	search_date = args[0]
	# 	search_query = (f"SELECT * FROM train_schedule WHERE departure_date = '{search_date}'")
	#
	# 	self.cursor.execute(search_query)
	# 	for i in self.cursor:
	# 		print(i)
	#
	# def get_full_schedule(self):
	# 	full_schedule_data = (f'{self.train_name} | {self.departure_gate} | {self.departure_city} | '
	# 	                      f'{self.departure_date} | {self.arrival_city} | {self.arrival_date} | '
	# 	                      f'{self.arrival_gate} ')
	# 	return full_schedule_data
