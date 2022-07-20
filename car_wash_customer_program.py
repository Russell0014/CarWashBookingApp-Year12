import os
from time import time, sleep
from numpy import number
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from datetime import date, datetime
import pandas as pd

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
    20: "5:30 PM",}

cleaning_options = [("1)","Interior Cleaning","$35"),
                    ("2)","Exterior Cleaning","$26"),
                    ("3)","Interior and Exterior","$45"),
                    ("4)","Detailing","$120")]

folder = os.path.dirname(os.path.abspath(__file__))
booking_info = os.path.join(folder, 'booking_info.csv')
columns= ["First Name", "Last Name", "Phone Number", "Cleaning Option", "Price", "Date", "Time"]
df = pd.DataFrame(columns=columns)
df = pd.read_csv(booking_info, index_col=0)


def verify(number):
    return str(number).startswith("04")

while True:

    """Collects contact information from the user"""
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

    print()

    """Collects booking information"""
    print("==Booking Information==")
    while True:
        current_date = datetime.now()
        booking_date = input("Enter your booking date in DD/MM/YY: ")
        try:
            future_date = datetime.strptime(booking_date, "%d/%m/%y")
        except ValueError:
            print("Please make sure the date is in the correct format.")
            continue

        filtered_date = (df['Date'].astype(str).str.contains(booking_date))
        filtered_date_df = df[filtered_date]

        if future_date.date() < current_date.date():
            print("Please enter a date into the future.")
        elif len(filtered_date_df) == 19:
            print("Sorry that date is fully booked.")
        else:
            print()
            break

    for Num, Times in time.items():
        print(str(Num) + ')' ,Times)
    
    while True:
        selected_time = int(input("Enter option number from the cleaning times above: "))
        option = ""
        if selected_time in range(1, 21):
            option = time[selected_time]
            filtered = (df['Time'].astype(str).str.contains(option)) & (df['Date'].astype(str).str.contains(booking_date))
            filtered_df = df[filtered]

            if len(filtered_df) == 0:
                break
            else:
                print("sorry that time slot is not available.")
                continue
        else:
            print("The selected number is not on the list. ")
            continue
    print()

    for sel, opt, price in cleaning_options:
        print(sel, opt, price)

    while True:
        c_option = ""
        c_price = ""
        selected_cleaning = int(input("Enter option number from the cleaning options above: "))
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

    print()

    """booking confirmation"""
    print("==Booking confirmation")
    print(F_name, L_name)
    print("On", booking_date)
    print("At", option)
    print(c_option, c_price)
    
    while True:
        confirm = input("Is your booking information correct? (y/n)")
        if confirm == "y" or confirm == "Y" or confirm == "yes" or confirm == "Yes":
            df = df.append({"First Name" : F_name, "Last Name" : L_name, "Phone Number" : str(P_number), "Cleaning Option" : c_option, "Price" : c_price, "Date" : booking_date, "Time" : option}, ignore_index=True)
            sleep(1)
            os.system('cls')
            df.to_csv(booking_info)
            break
        else:
            os.system('cls')
            break
