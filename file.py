import mysql.connector

def create_mysql_connection():
    try:
        conn_mysql = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kunjara123@"
        )
        print("MySQL connection created")
        return conn_mysql

    except mysql.connector.Error as e:
        print("MySQL connection error:", e)

# Creating the MySQL connection
conn_mysql = create_mysql_connection()


#created a table in mysql and imported the data using mysql wizard
def create_table(conn):
        cursor_mysql = conn.cursor()

        cursor_mysql.execute("USE Flight_data")

        create_table1_query = """
        CREATE TABLE Flight_schedule (
            S_no int,
            flight_no VARCHAR(255),
            arrival_airport_id VARCHAR(255),
            departure_airport_id VARCHAR(255),
            departure_time int,
            arrival_time int,
            Frequency VARCHAR(255),
            Via VARCHAR(255),
            effected_from VARCHAR(255),
            effected_to VARCHAR(255),
            transit_time int,
            saturday int,
            sunday int,
            monday int,
            tuesday int,
            wednesday int,
            thursday int,
            friday int
        )
        """
        cursor_mysql.execute(create_table1_query)
        print("Table 'Flight_schedule' is created successfully")

        cursor_mysql.close()
        conn.close()  

create_table(conn_mysql)



#created a another table
def create_table(conn):
        cursor_mysql = conn.cursor()

        cursor_mysql.execute("USE Flight_data")

        create_table1_query = """
        CREATE TABLE Flight_schedule_3 (
            S_no int,
            flight_no VARCHAR(255),
            arrival_airport_id VARCHAR(255),
            departure_airport_id VARCHAR(255),
            departure_time int,
            arrival_time int,
            Frequency VARCHAR(255),
            effected_from VARCHAR(255),
            effected_to VARCHAR(255),
            transit_time int,
            saturday int,
            sunday int,
            monday int,
            tuesday int,
            wednesday int,
            thursday int,
            friday int
        )
        """
        cursor_mysql.execute(create_table1_query)
        print("Table 'Flight_schedule_3' is created successfully")

        cursor_mysql.close()
        conn.close()  

create_table(conn_mysql)



