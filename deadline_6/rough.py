import getpass
import mysql.connector
from mysql.connector import Error
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from geopy.exc import GeocoderTimedOut

def get_coordinates(location_string):
    geolocator = Nominatim(user_agent="geo_distance_calculator")
    try:
        location = geolocator.geocode(location_string)
        if location is not None:
            return location.latitude, location.longitude
        else:
            print(f"Could not find coordinates for {location_string}.")
            return None
    except GeocoderTimedOut:
        print("Geocoder service timed out. Please try again later.")
        return None

def calculate_distance(location1, location2):
    coordinates1 = get_coordinates(location1)
    coordinates2 = get_coordinates(location2)
    
    if coordinates1 is not None and coordinates2 is not None:
        return great_circle(coordinates1, coordinates2).kilometers
    else:
        return None


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

        cursor.execute("select * from rider")
        x = cursor.fetchall()
        riderid = x[-1][0] + 1
        cursor.execute("select * from trip")
        x = cursor.fetchall()
        tripid = x[-1][0] + 1
        cursor.execute("select * from payment")
        x = cursor.fetchall()
        paymentid = x[-1][0] + 1
        y = 0
        t1 = 0
        basefare = 9

        cursor.execute("SHOW TRIGGERS;")
        ans = cursor.fetchall()
        for i in ans:
            if i[0] == "trigger1":
                t1 = 1

        while True:

            print("""\nAV Cabs\n
1. Sign Up
2. Login
3. Exit""")
            a = int(input("Enter your choice: "))
            p = 0
            if a == 3:
                break

            elif a == 1:
                firstname = input("First Name: ")
                mid_name = input("Middle Name: ")
                lastname = input("Last Name: ")
                ridercontact = int(input("Contact: "))
                ridermail = input("Email: ")
                cursor.execute("""SELECT * FROM rider""")
                ans = cursor.fetchall()
                for i in ans:
                    if i[5] == ridermail:
                        print("Email already exists. Either use a different mail or login.")
                        y = 1
                        break
                    if i[4] == ridercontact:
                        print("Phone number already exists. Either use a different number or login.")
                        y = 1
                        break
                if(y == 1):
                    continue
                
                query = "insert into rider (rider_id, first_name, middle_name, last_name, contact, email) values (%s,%s,%s,%s,%s,%s);"
                vals = (riderid, firstname, mid_name, lastname, ridercontact, ridermail)
                cursor.execute(query,vals)
                connection.commit()
                riderid += 1

                # cursor.execute("select * from rider where rider_id = 202")
                # print(cursor.fetchall())
                # cursor.execute("delete from rider where rider_id = 202")
                # connection.commit()

            
            elif a == 2:
                mailyes = 0
                contactyes = 0
                y = 0
                ridermail = input("Email: ")
                ridercontact = int(input("Contact: "))
                cursor.execute("""SELECT * FROM rider""")
                ans = cursor.fetchall()
                for i in ans:
                    if i[5] == ridermail and i[4] == ridercontact:
                        mailyes = 1
                        contactyes = 1
                        y = 1
                        break
                
                if(y == 0):
                    print("user not found. either try again or signup")
                    continue
                else:
                    print(f"Welcome, ",i[1],i[2],i[3],"\n")

                bookcab = -1

                print("""1. Book a Cab""")
                bookcabchoice = int(input("choice: "))
                
                if(bookcabchoice == 1):
                    location1 = input()
                    location2 = input()
                                    
                distance = calculate_distance(location1, location2)
                if distance is not None:
                    # print(f"Distance between {location1} and {location2}: {distance:.2f} km")
                    fare = distance * basefare
                    print(fare)
                else:
                    print("Could not calculate distance due to missing coordinates.")
                # cursor.execute("select * from rider where rider_id = 202")
                # print(cursor.fetchall())
                # cursor.execute("delete from rider where rider_id = 202")
                
             

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")