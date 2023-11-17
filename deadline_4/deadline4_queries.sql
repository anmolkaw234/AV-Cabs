-- -- Query 1:- Average Fare
--  SELECT AVG(fare)
--  AS average_fare FROM trip


-- -- Query 2:- Drivers who have not done any trip
-- SELECT driver.* FROM driver 
-- WHERE driver.driver_id NOT IN (
--     SELECT driver.driver_id 
--     FROM driver 
--     INNER JOIN trip ON driver.driver_id = trip.driver_id 
--     WHERE trip.fare > 0
-- ) 


-- -- Query 3: Display Details of Drivers with highest ratings
-- SELECT * FROM driver
-- WHERE rating = (
--   SELECT MAX(rating)
--   FROM driver
-- )


-- -- Query 4: Display the number of rides done by all the drivers
-- SELECT d.*, COUNT(*) AS total_rides FROM trip t
-- JOIN driver d ON t.driver_id = d.driver_id
-- GROUP BY t.driver_id;



-- -- Query 5: Display all rides details along with customer name, driver name and driver rating
-- SELECT t.*, r.*, d.*
-- FROM trip t
-- JOIN rider r ON t.rider_id = r.rider_id 
-- JOIN driver d ON t.driver_id = d.driver_id
-- GROUP BY t.trip_id;



-- -- Query 6: All details of distinct drivers rider with rider_id = 1 has driver with
-- SELECT DISTINCT driver.*
-- FROM driver
-- JOIN trip ON driver.driver_id = trip.driver_id
-- WHERE trip.rider_id = 1;



-- -- Query 7 : using UPDATE Command
-- -- -- Original Entry: -- insert into rider (rider_id, first_name, middle_name, last_name, contact, email) values (200, 'Bruce', 'Lemar', 'Somner', '6226609845', 'bsomner5j@nasa.gov');
-- -- -- updating the customer email to : BruceLemar@iiitd.com

-- -- original entry
-- select * from rider where rider_id = 200;

-- UPDATE rider
-- SET email = 'BruceLemar@iiitd.com'
-- WHERE rider_id = 200;

-- -- updated entry:
-- select * from rider where rider_id = 200;


-- -- Query 8: Display Details of Drivers with low ratings (<5)
-- SELECT * FROM driver
-- WHERE driver.rating BETWEEN 1 and 5;


-- -- Query 9: foreign key constraint
-- -- The table trips has an entry where the foreign key rider_id = 70. So if we delete entry from rider table where id = 70, it'll fail as it is being used as foreign key in another table.
-- -- -- insert into trip (trip_id, pickup, droploc, fare, driver_id, rider_id) values (298, '3845 Everett Road', '763 Huxley Park', 1187, 142, 70);

-- DELETE FROM rider
-- WHERE rider_id = 70;



-- -- Query 10:

-- -- SHOW CREATE TABLE trip;

-- -- Originial Entry
-- -- -- insert into rider (rider_id, first_name, middle_name, last_name, contact, email) values (201, 'Gay', 'Merlin', 'Tucsell', '1129165277', 'gtucsell5k@cmu.edu');

-- -- Duplicate entry with same rider_id but different everything:
-- insert into rider (rider_id, first_name, middle_name, last_name, contact, email) values (201, 'hi', 'hello', 'hey', '9999999999', 'haha@iiitd.edu');

-- -- Duplicate entry with same email but different everything:
-- insert into rider (rider_id, first_name, middle_name, last_name, contact, email) values (202, 'hihihi', 'hihi', 'hi', '1111111111', 'gtucsell5k@cmu.edu');


-- -- Query 11 : Using WILDCARD : display details of vehicles whose brand name stars with letter 'a'
-- SELECT * FROM vehicle
-- WHERE brand LIKE 'm%';


-- -- Query 12 : details of trips where ride fare is greater than 1400 and less than 1500
-- SELECT t.*
-- FROM trip t
-- INNER JOIN rider r ON r.rider_id = t.rider_id
-- WHERE t.fare > 1400 and t.fare < 1500
-- GROUP BY t.trip_id;