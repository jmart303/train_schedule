
mysql -u root -p
show databases;

CREATE DATABASE train_schedule;
USE train_schedule;

CREATE TABLE schedule (
    id INT NOT NULL AUTO_INCREMENT,
    trainName varchar(50),
    ArrivalTime DATETIME(6),
    DestinationCity varchar(50),
    DepartureTime DATETIME(6),
    DepartureCity varchar(50),
    Gate varchar(5),
    PRIMARY KEY (Id)
);


SELECT * FROM schedule;

INSERT INTO schedule (trainName, Gate, DepartureTime, DepartureCity, ArrivalTime, DestinationCity)
VALUES (
           'Larry_tracks', '1A', '2023-10-30 3:00:00', 'Denver', '2023-10-30 19:15:00', 'New York'
        );

INSERT INTO schedule (trainName, Gate, DepartureTime, DepartureCity, ArrivalTime, DestinationCity)
VALUES (
            'rolling_vickie', '3A', '2023-10-30 2:00:00', 'Seattle','2023-10-30 22:30:00', 'L.A.'
    );

INSERT INTO schedule (trainName, Gate, DepartureTime, DepartureCity, ArrivalTime, DestinationCity)
VALUES (
       'mikey_movers', '2A', '2023-10-30 3:00:00', 'Boston', '2023-11-30 5:00:00', 'Denver'
    );

INSERT INTO schedule (trainName, Gate, DepartureTime, DepartureCity, ArrivalTime, DestinationCity)
VALUES (
           'sliding_sue', '6A', '2023-10-30 4:00:00', 'L.A.', '2023-11-30 3:35:00', 'Chicago'
    );

INSERT INTO schedule (trainName, Gate, DepartureTime, DepartureCity, ArrivalTime, DestinationCity)
VALUES (
           'mikey_movers',  '7A', '2023-10-30 5:00:00', 'Tempe', '2023-12-30 10:45:00', 'Dallas'
        );
INSERT INTO schedule (trainName, Gate, DepartureTime, DepartureCity, ArrivalTime, DestinationCity)
VALUES (
       'Larry_tracks', '9A', '2023-10-30 6:00:00', 'Bozeman','2023-10-30 11:30:00', 'Utah'
    );


CREATE TABLE trains (
    id int AUTO_INCREMENT,
    trainName varchar(50),
    trainColor varchar(25),
    current_capacity int(3) NOT NULL,
    capacity int(3) NOT NULL,
    FOREIGN KEY (Id) REFERENCES schedule(Id)
);


INSERT INTO trains(trainName, trainColor, current_capacity, capacity)
VALUES (
    'Larry_tracks', 'red', '150', '200'
       );

INSERT INTO trains(trainName, trainColor, current_capacity, capacity)
VALUES (
   'rolling_vickie', 'blue', '225', '250'
    );
INSERT INTO trains(trainName, trainColor, current_capacity, capacity)
VALUES (
    'mikey_movers', 'green', '400', '400'
    );

INSERT INTO trains(trainName, trainColor, current_capacity, capacity)
VALUES (
    'sliding_sue', 'black', '25', '50'
    );

