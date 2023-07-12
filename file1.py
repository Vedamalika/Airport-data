import mysql.connector
import pandas as pd

# Establishing a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    
    password='Kunjara123@',
    database='Flight_data'
)

# Creating  a cursor object
cursor = conn.cursor()
#changing the csv to dataframe
flight_df = pd.read_csv("/home/kunjara/Downloads/modified_flight_schedule_2.csv")

# Iterating  over the rows of the DataFrame
for _, row in flight_df.iterrows():
    # Extracting the values from the row
    s_no = row['S.No']
    flight_no = row['flight_no']
    arrival_airport_id = row['arrival_airport_id']
    departure_airport_id = row['departure_airport_id']
    departure_time = row['departure_time']
    arrival_time = row['arrival_time']
    frequency = row['Frequency']
    effected_from = row['effected_from']
    effected_to = row['effected_to']
    transit_time = row['transit_time']
    saturday = row['saturday']
    sunday = row['sunday']
    monday = row['monday']
    tuesday = row['tuesday']
    wednesday = row['wednesday']
    thursday = row['thursday']
    friday = row['friday']

    # SQL INSERT statement
    sql = "INSERT INTO Flight_schedule_3 (S_No, flight_no, arrival_airport_id, departure_airport_id, departure_time, arrival_time, Frequency, effected_from, effected_to, transit_time, saturday, sunday, monday, tuesday, wednesday, thursday, friday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Executing the INSERT statement with the row values
    cursor.execute(sql, (
        s_no, flight_no, arrival_airport_id, departure_airport_id, departure_time, arrival_time,
        frequency, effected_from, effected_to, transit_time,
        saturday, sunday, monday, tuesday, wednesday, thursday, friday
    ))

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()

# we can use this code too for inserting the values 
for index, row in flight_df.iterrows():
    sql = """
    INSERT INTO light_schedule_3 (S_No, flight_no, arrival_airport_id, departure_airport_id, departure_time,
    arrival_time, Frequency, effected_from, effected_to, transit_time, saturday, sunday, monday, tuesday,
    wednesday, thursday, friday)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (row['S.No'], row['flight_no'], row['arrival_airport_id'], row['departure_airport_id'], row['departure_time'],
              row['arrival_time'], row['Frequency'], row['effected_from'], row['effected_to'], row['transit_time'],
              row['saturday'], row['sunday'], row['monday'], row['tuesday'], row['wednesday'], row['thursday'], row['friday'])

    cursor.execute(sql, values)
    conn.commit()

cursor.close()
conn.close()