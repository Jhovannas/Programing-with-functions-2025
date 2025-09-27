from tkinter import Tk, Label, Entry, Button
import datetime
import mysql.connector

def reserve_appointment():
    try:
        # Get user input
        customer_first_name = input("First Name: ")
        customer_last_name = input("Last Name: ")
        phone_number = input("Phone Number: ")
        service = input("Service: ")
        appointment_date = input("Date: ")
        appointment_time = input("Time: ")

        # Save the appointment details to the database
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="password",
            database="Appointments"
        )
        cursor = db.cursor()
        sql = "INSERT INTO online_appointment (first_name, last_name, phone_number, service, appointment_date, appointment_time) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (customer_first_name, customer_last_name, phone_number, service, appointment_date, appointment_time)
        cursor.execute(sql, values)
        db.commit()
        print("Appointment reserved successfully!")
    except mysql.connector.Error as error:
        print("Error while reserving appointment:", error)

def main():
    reserve_appointment()

if __name__ == "__main__":
    main()