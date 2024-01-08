from dataclasses import dataclass


@dataclass
class GetTrainSchedule:
	train_name: str
	departure_city: str
	departure_date: str
	departure_gate: str
	arrival_city: str
	arrival_date: str
	arrival_gate: str





data = GetTrainSchedule('railway', 'denver', '2023-11-10 3:00:00', '2D', 'bozeman', '2023-11-10 14:10:00', '1A')



print(data.train_name)
