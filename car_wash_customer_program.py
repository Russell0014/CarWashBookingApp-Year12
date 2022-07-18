import os
from numpy import number
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
booking_info = os.path.join(folder, 'booking_info.csv')
df = pd.read_csv(booking_info)

def verify(number):
    return str(number).startswith("04")

while True:
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


