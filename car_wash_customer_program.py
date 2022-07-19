import os
from select import select
from time import time
from numpy import number
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from datetime import date, datetime
import pandas as pd

times = [("1."," 08:00 AM"),
         ("2."," 08:30 AM"),
         ("3."," 09:00 AM"),
         ("4."," 09:30 AM"),
         ("5."," 10:00 AM"),
         ("6."," 10:30 AM"),
         ("7."," 11:00 AM"),
         ("8."," 11:30 AM"),
         ("9."," 12:00 PM"),
         ("10.","12:30 PM"),
         ("11.","01:00 PM"),
         ("12.","01:30 PM"),
         ("13.","02:00 PM"),
         ("14.","02:30 PM"),
         ("15.","03:00 PM"),
         ("16.","03:30 PM"),
         ("17.","04:00 PM"),
         ("18.","04:30 PM"),
         ("19.","05:00 PM"),
         ("20.","05:30 PM"),]

time = {
    1: "8:00 AM",
    2: "8:30 AM",
    3: "9:00 AM",
    4: "9:30 AM",
    5: "10:00 AM",
    6: "10:30 AM",
    7: "11:00 AM",
    8: "11:30 AM",
    9: "12:00 PM",
    10: "12:30 PM",
    11: "1:00 PM",
    12: "1:30 PM",
    13: "2:00 PM",
    14: "2:30 PM",
    15: "3:00 PM",
    16: "3:30 PM",
    17: "4:00 PM",
    18: "4:30 PM",
    19: "5:00 PM",
    20: "5:30 PM",
}


cleaning_options = [("1.","Interior Cleaning","$35"),
                    ("2.","Exterior Cleaning","$26"),
                    ("3.","Interior and Exterior","$45"),
                    ("4.","Detailing","$120")]

folder = os.path.dirname(os.path.abspath(__file__))
booking_info = os.path.join(folder, 'booking_info.csv')
df = pd.read_csv(booking_info)
column_Names = ["First Name", "Last Name", "Phone Number", "Cleaning Option", "Price", "Date", "Time"]
df = pd.DataFrame(columns=column_Names)

def verify(number):
    return str(number).startswith("04")

while True:

    """Collets contact information from the user"""
    
    print("==Contact Information==")

    while True:
        F_name = input("Enter your first name: ")
        L_name = input("Enter your last name: ")
        if F_name.isnumeric() == True or L_name.isnumeric() == True:
            print("Please use letters.")
        else:
            break

    while True: 
        P_number = input("Enter your phone number: ")
        if verify(P_number) == True and len(P_number) == 10 and P_number.isnumeric() == True:
            break
        else:
            print("Please enter a valid phone number. ")

    """Collects booking information"""
    while True:
        current_date = datetime.now()
        booking_date = input("Enter your booking date in DD/MM/YY: ")
        try:
            future_date = datetime.strptime(booking_date, "%d/%m/%y")
        except ValueError:
            print("Please make sure the date is in the correct format.")
            continue
        if future_date.date() < current_date.date():
            print("Please enter a date into the future.")
        else:
            break

    for Num, Time in times:
        print(Num, Time)

    while True:
        selected_time = int(input("Select a cleaning time from the list above: "))
        option = ""
        if selected_time in range(1, 21):
            option = time[selected_time]
            break
        else:
            print("The selected number is not on the list. ")
            continue

    for sel, opt, price in cleaning_options:
        print(sel, opt, price)

    while True:
        c_option = ""
        c_price = ""
        selected_cleaning = int(input("Select a cleaning option from above: "))
        if selected_cleaning < 1 or selected_cleaning > 4:
            print("The selected number is not on the list. ")
        elif  selected_cleaning == 1:
            c_option = "Interior Cleaning"
            c_price = "$35"
            break
        elif  selected_cleaning == 2:
            c_option = "Exterior Cleaning"
            c_price = "$26"
            break
        elif  selected_cleaning == 3:
            c_option = "Interior and Exterior"
            c_price = "$45"
            break
        elif  selected_cleaning == 4:
            c_option = "Detailing"
            c_price = "$120"
            break   
            