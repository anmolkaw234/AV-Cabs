CREATE TABLE admin(
	first_name VARCHAR(50),
	middle_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	password VARCHAR(50)
);

CREATE TABLE rider(
	rider_id BIGINT NOT NULL PRIMARY KEY,
	first_name VARCHAR(50),
	middle_name VARCHAR(50),
	last_name VARCHAR(50),
	contact BIGINT NOT NULL,
	email VARCHAR(50),
	UNIQUE KEY (contact),
	UNIQUE KEY (email)
);

CREATE TABLE driver(
	driver_id BIGINT NOT NULL PRIMARY KEY,
	first_name VARCHAR(50),
	middle_name VARCHAR(50),
	last_name VARCHAR(50),
	contact BIGINT NOT NULL,
	license VARCHAR(50) NOT NULL,
	UNIQUE KEY (contact),
	UNIQUE KEY (license)
);

CREATE TABLE vehicle(
	vehicle_id BIGINT NOT NULL PRIMARY KEY,
	brand VARCHAR(50),
	vehicletype VARCHAR(50),
	model VARCHAR(50),
	seatingcap INT,
	plateno VARCHAR(50) NOT NULL,
	UNIQUE KEY (plateno),
    rider_id BIGINT,
	FOREIGN KEY (rider_id) REFERENCES rider(rider_id)
);


CREATE TABLE trip(
	trip_id BIGINT NOT NULL PRIMARY KEY,
	pickup VARCHAR(50),
	droploc VARCHAR(50),
	fare INT,
    driver_id BIGINT,
    rider_id BIGINT,
	FOREIGN KEY (driver_id) REFERENCES driver(driver_id),
	FOREIGN KEY (rider_id) REFERENCES rider(rider_id)
);

CREATE TABLE payment(
	payment_id BIGINT NOT NULL PRIMARY KEY,
	method VARCHAR(50),
	amount INT,
    rider_id BIGINT,
    trip_id BIGINT,
	FOREIGN KEY (rider_id) REFERENCES rider(rider_id),
	FOREIGN KEY (trip_id) REFERENCES trip(trip_id)
);