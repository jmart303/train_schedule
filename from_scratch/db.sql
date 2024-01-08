

CREATE TABLE train_schedule (
    id INT NOT NULL AUTO_INCREMENT,
    train_name varchar(25),
    departure_date_time DATETIME(6),
    departure_city varchar(50),
    departure_gate varchar(5),
    arrival_date_time DATETIME(6),
    arrival_city varchar(50),
    arrival_gate varchar(5),
    on_time varchar(5),
    PRIMARY KEY (id)
    );



CREATE TABLE trains (
    id INT NOT NULL AUTO_INCREMENT,
    train_name varchar(25),
    train_capacity varchar(5),
    train_descriptions varchar(255),
    train_available_capacity varchar(5),
    in_service varchar(3),
    PRIMARY KEY (id)
    );

INSERT INTO trains (train_name, train_capacity, train_descriptions, train_available_capacity, in_service)
VALUES (
           'flying_bob', '200', 'red', '0', 'yes'
       );

INSERT INTO trains (train_name, train_capacity, train_descriptions, train_available_capacity, in_service)
VALUES (
           'rolling_sue', '500', 'green', '0', 'yes'
       );

INSERT INTO trains (train_name, train_capacity, train_descriptions, train_available_capacity, in_service)
VALUES (
           'sliding_sally', '50', 'blue', '0', 'yes'
       );

INSERT INTO trains (train_name, train_capacity, train_descriptions, train_available_capacity, in_service)
VALUES (
           'flashing_larry', '350', 'yellow', '0', 'no'
       );



INSERT INTO train_schedule (train_name, departure_date_time, departure_city, departure_gate, arrival_date_time, arrival_city, arrival_gate, on_time)
VALUES (
        'flying_bob', '2023-11-01 3:00:00', 'denver', '4D', '2023-11-01 10:00:00', 'bozeman', '1A', 'yes'
        );

INSERT INTO train_schedule (train_name, departure_date_time, departure_city, departure_gate, arrival_date_time, arrival_city, arrival_gate, on_time)
VALUES (
        'rolling_sue', '2023-10-31 6:00:00', 'dallas', '6A', '2023-11-02 14:30:00', 'arizona', '3C', 'yes'
        );

INSERT INTO train_schedule (train_name, departure_date_time, departure_city, departure_gate, arrival_date_time, arrival_city, arrival_gate, on_time)
VALUES (
        'sliding_sally', '2023-11-05 12:15:00', 'seattle', '2E', '2023-11-05 22:35:00', 'san diego', '3A', 'yes');

INSERT INTO train_schedule (train_name, departure_date_time, departure_city, departure_gate, arrival_date_time, arrival_city, arrival_gate, on_time)
VALUES (
           'flying_bob', '2023-11-23 17:00:00', 'las vegas', '1E', '2023-11-23 22:00:00', 'bozeman', '1A', 'yes'
       );

INSERT INTO train_schedule (train_name, departure_date_time, departure_city, departure_gate, arrival_date_time, arrival_city, arrival_gate, on_time)
VALUES (
           'flashing_larry', '2023-11-23 17:00:00', 'sacramento', '1E', '2023-11-23 22:00:00', 'orange county', '1A', 'yes'
       );

