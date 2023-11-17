import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='deadline5_final',
                                         user='root',
                                         password='iloveiiitd')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server")
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        t1 = 0
        t2 = 0
        cursor.execute("SHOW TRIGGERS;")
        ans = cursor.fetchall()
        for i in ans:
            if i[0] == "trigger1":
                t1 = 1
            if i[0] == "trigger2":
                t2 = 1

        while True:
            print("""Menu:
 1. Query-1 : Average Fare.
 2. Query-2 : Drivers who have not done any trips.
 3. Query-3 : Drivers with highest ratings.
 4. Query-4 : Number of rides by all drivers.
 5. Query-5 : All Details of Distinct Drivers with whom rider with rider_id = 1 has taken a trip with.
 6. Query-6 : Drivers with low ratings (between 1 to 5).
 7. Query-7 : Details of vehicles whose brand name starts with letter 'm'
 8. OLAP-1 : Average Amount groupped by payment method.
 9. OLAP-2 : Trips where the fare is greater than or equal to the overall average fare for all trips groupped by rider_id
 10. OLAP-3 : CUBE OLAP query on trip table
 11. OLAP-4 : Roll Up OLAP query on vehicle table
 12. Create Trigger-1 : Trigger to check if the input rating of driver is above or below 10; if it's above 10, then make it 10.
 13. Drop Trigger-1 : Delete the trigger 1 if it exists.
 14. Create Trigger-2 : Trigger to Captialize each letter of the Vehicle's Brand, Type and Model.
 15. Drop Trigger-2 : Delete the trigger 2 if it exists.
 16. Show Triggers.
 17. Check Trigger 1.
 18. Check Trigger 2.
 Press 0 to EXIT""")
            
            a = int(input("Select your query: "))
            p = 0
            if a == 0:
                break
            elif a == 1:
                cursor.execute("""SELECT AVG(fare)
 AS average_fare FROM trip;""")
                p = 1
                
            elif a == 2:
                cursor.execute("""SELECT driver.* FROM driver 
WHERE driver.driver_id NOT IN (
    SELECT driver.driver_id 
    FROM driver 
    INNER JOIN trip ON driver.driver_id = trip.driver_id 
    WHERE trip.fare > 0
) ;""")
                p = 1

            elif a == 3:
                cursor.execute("""SELECT * FROM driver
WHERE rating = (
  SELECT MAX(rating)
  FROM driver
);""")
                p = 1

            elif a == 4:
                cursor.execute("""SELECT d.*, COUNT(*) AS total_rides FROM trip t
JOIN driver d ON t.driver_id = d.driver_id
GROUP BY t.driver_id;""")
                p = 1

            elif a == 5:
                cursor.execute("""SELECT DISTINCT driver.*
FROM driver
JOIN trip ON driver.driver_id = trip.driver_id
WHERE trip.rider_id = 1;""")
                p = 1

            elif a == 6:
                cursor.execute("""SELECT * FROM driver
WHERE driver.rating BETWEEN 1 and 5;""")
                p = 1

            elif a == 7:
                cursor.execute("""SELECT * FROM vehicle
WHERE brand LIKE 'm%';""")
                p = 1

            elif a == 8:
                cursor.execute("""SELECT method, AVG(amount), COUNT(*) as total                        
FROM payment
GROUP BY method""")
                p = 1

            elif a == 9:
                cursor.execute("""SELECT rider_id, AVG(fare)
FROM trip
WHERE trip.fare >= (SELECT AVG(fare) FROM trip)
GROUP BY rider_id""")
                p = 1

            elif a == 10:
                cursor.execute("""SELECT
pickup, droploc, COUNT(*) as total_rides, AVG(fare) as average_fare
FROM trip
GROUP BY pickup,droploc
union all
SELECT
pickup, NULL,COUNT(*) as total_rides, AVG(fare) as average_fare
FROM trip
GROUP BY pickup
union all
SELECT
NULL ,droploc ,COUNT(*) as total_rides, AVG(fare) as average_fare
FROM trip
GROUP BY droploc
union all
SELECT
NULL, NULL, COUNT(*) as total_rides, AVG(fare) as average_fare
FROM trip;""")
                p = 1

            elif a == 11:
                cursor.execute("""SELECT
vehicletype, model, AVG(seatingcap) as sc, COUNT(*) as c
FROM vehicle
GROUP BY vehicletype ,model
union all
SELECT
vehicletype, NULL, AVG(seatingcap) as sc, COUNT(*) as c
FROM vehicle
GROUP BY vehicletype
union all
SELECT
NULL, NULL, AVG(seatingcap) as c, COUNT(*) as c
FROM vehicle;""")
                p = 1
                               

            elif a == 12:
                if t1 == 0:
                    cursor.execute("""CREATE TRIGGER trigger1
BEFORE INSERT ON driver
FOR EACH ROW
BEGIN
    IF NEW.rating > 10 THEN
        SET NEW.rating = 10;
    END IF;
END;""")
                    t1 = 1
                    print("Trigger 1 created.")
                else:
                    print("Trigger 1 already exists.")

            elif a == 13:
                if t1 == 1:
                    cursor.execute("""DROP TRIGGER IF EXISTS trigger1;""")
                    print("Trigger 1 dropped.")
                    t1 = 0
                else:
                    print("Trigger 1 doesn't exist")

            elif a == 14:
                if t2 == 0:
                    cursor.execute("""CREATE TRIGGER trigger2
BEFORE INSERT ON vehicle
FOR EACH ROW
BEGIN
	SET NEW.brand = UPPER(NEW.brand);
    SET NEW.vehicletype = UPPER(NEW.vehicletype);
    SET NEW.model = UPPER(NEW.model);
END;""")
                    
                    t2 = 1
                    print("Trigger 2 created.")
                else:
                    print("Trigger 2 already exists.")

            elif a == 15:
                if t2 == 1:
                    cursor.execute("""DROP TRIGGER IF EXISTS trigger2;""")
                    print("Trigger 2 dropped.")
                    t2 = 0
                else:
                    print("Trigger 2 doesn't exist.")

            elif a == 16:
                cursor.execute("SHOW TRIGGERS;")
                p = 1

            elif a == 17:
                print("inserting into driver table: {driver_id = 200, rating = 17}   :  insert into driver (driver_id, first_name, middle_name, last_name, contact, license, rating) values (200, 'Ravi', 'Kumar', 'Sharma', '4438104621', 'FCJMRzfEesbq', 17);")
                cursor.execute("insert into driver (driver_id, first_name, middle_name, last_name, contact, license, rating) values (200, 'Ravi', 'Kumar', 'Sharma', '4438104621', 'FCJMRzfEesbq', 17);")
                print()
                cursor.execute("select * from driver where driver_id = 200;")
                ans = cursor.fetchall()
                for i in ans:
                    print(i)
                    print()
                print()
                cursor.execute("DELETE FROM driver where driver_id = 200;")

            elif a == 18:
                print("inserting into vehicle table:  {brand : 'Chevrolet', type : 'sedan', model : 'Malibu44'}  :  insert into vehicle (vehicle_id, brand, vehicletype, model, seatingcap, plateno, rider_id) values (200, 'Chevrolet', 'sedan', 'Malibu44', 5, 'AL98WD4800', 9);")
                cursor.execute("insert into vehicle (vehicle_id, brand, vehicletype, model, seatingcap, plateno, rider_id) values (200, 'Chevrolet', 'sedan', 'Malibu44', 5, 'AL98WD4800', 9);")
                print()
                cursor.execute("select * from vehicle where vehicle_id = 200;")
                ans = cursor.fetchall()
                for i in ans:
                    print(i)
                    print()
                print()
                cursor.execute("DELETE FROM vehicle where vehicle_id = 200;")

            else:
                print("Make a Valid Choice.")

            if p == 1:
                ans = cursor.fetchall()
                for i in ans:
                    print(i)
                    print()

                print()
                print()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")