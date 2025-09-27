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

def reserve_appointment():
    def save_appointment():
        customer_first_name = first_name_entry.get()
        customer_last_name = last_name_entry.get()
        phone_number = phone_entry.get()
        service = services_entry.get()
        time_entry = time_entry.get()

        # Save the appointment details to the database
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="password",
            database="Appointments"
        )
        cursor = db.cursor()
        sql = "INSERT INTO online_appointment (first_name, last_name, phone_number, service, appointment_date, appointment_time) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (customer_first_name, customer_last_name, phone_number, service)
        cursor.execute(sql, values)
        db.commit()
        print("Appointment reserved successfully!")

        # Create the GUI
        window = Tk()
        window.mainloop()
    window = Tk()
    window.title("Appointment Reservation")
    window.geometry("400x400")

    first_name_label = Label(window, text="First Name:")
    first_name_label.pack()
    first_name_entry = Entry(window)
    first_name_entry.pack()

    last_name_label = Label(window, text="Last Name:")
    last_name_label.pack()
    last_name_entry = Entry(window)
    last_name_entry.pack()

    phone_label = Label(window, text="Phone Number:")
    phone_label.pack()
    phone_entry = Entry(window)
    phone_entry.pack()

    services_label = Label(window, text="Services:")
    services_label.pack()
    services_entry = Entry(window)
    services_entry.pack()

    date_label = Label(window, text="Date:")
    date_label.pack()
    time_entry = Entry(window)
    time_entry.pack()

    time_label = Label(window, text="Time:")
    time_label.pack()
    time_entry = Entry(window)
    time_entry.pack()

    save_button = Button(window, text="Save Appointment", command=save_appointment)
    save_button.pack()

    window.mainloop()

reserve_appointment()

def Customer(first_name, last_name, phone_number):
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password",
        database="Appointments"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM customer")
    result = cursor.fetchone()
    first_name = result[0]
    last_name = result[1]
    phone_number = result[2]
    return {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number
    }

def employee(first_name, role):
    print("Appointment reserved by:", employee)
    print("Appointment date and time:", date_time)
    return {
        'employee': employee,
        'date_time': date_time
    }

def Services():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password",
        database="salon_appointments"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM services")
    results = cursor.fetchall()
    services = []
    print("Select services from the list:")
    for result in results:
        service_id = result[0]
        service_name = result[1]
        print(f"{service_id}. {service_name}")
    print("Enter 'done' when finished selecting services.")
    while True:
        service = input("Enter service number: ")
        if service == 'done':
            break
        services.append(service)
    return services

def main():
    reserve_appointment()

if __name__ == "__main__":
    main()