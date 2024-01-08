
CREATE TABLE train_schedule (
    id INT NOT NULL AUTO_INCREMENT,
    train_name varchar(25),
    departure_city varchar(25),
    departure_date DATETIME(6),
    departure_gate varchar(25),
    arrival_city varchar(25),
    arrival_date DATETIME(6),
    arrival_gate varchar(25),
    PRIMARY KEY (id)
);

CREATE TABLE trains (
    id INT NOT NULL AUTO_INCREMENT,
    train_name varchar(25),
    capacity varchar(3),
    description varchar(255),
    available_capacity varchar(3),
    PRIMARY KEY (id)
);

INSERT INTO train_schedule (train_name, departure_city, departure_date, departure_gate, arrival_city, arrival_date, arrival_gate)
VALUES (
        'running_bill', 'denver', '2023-11-05 4:30:00', '2D', 'bozeman', '2023-11-05 7:45:00', '1A'
       );

INSERT INTO train_schedule (train_name, departure_city, departure_date, departure_gate, arrival_city, arrival_date, arrival_gate)
VALUES (
           'sliding_harry', 'new york', '2023-11-06 13:10:00', '1E', 'florida', '2023-11-07 4:45:00', '6B'
       );

INSERT INTO train_schedule (train_name, departure_city, departure_date, departure_gate, arrival_city, arrival_date, arrival_gate)
VALUES (
           'crazy_kim', 'arizona', '2023-12-15 12:30:00', '5D', 'casper', '2023-12-16 18:15:00', '3C'
       );

INSERT INTO train_schedule (train_name, departure_city, departure_date, departure_gate, arrival_city, arrival_date, arrival_gate)
VALUES (
           'rolling_phil', 'seattle', '2023-11-07 10:40:00', '1C', 'san diego', '2023-11-07 23:30:00', '2G'
       );


INSERT INTO trains (train_name, capacity, description, available_capacity)
VALUES (
           'running_bill', '300', 'red', '25'
       );

INSERT INTO trains (train_name, capacity, description, available_capacity)
VALUES (
           'sliding_harry', '250', 'blue', '75'
       );

INSERT INTO trains (train_name, capacity, description, available_capacity)
VALUES (
           'crazy_kim', '50', 'yellow', '100'
       );

INSERT INTO trains (train_name, capacity, description, available_capacity)
VALUES (
           'rolling_phil', '450', 'green', '220'
       );