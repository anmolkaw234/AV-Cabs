   
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


            if p == 1:
                ans = cursor.fetchall()
                for i in ans:
                    print(i)
                    print()

                print()
                print()