import os
import numpy
from datetime import datetime
import time
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
booking_info = os.path.join(folder, 'booking_info.csv')
columns= ["First Name", "Last Name", "Phone Number", "Cleaning Option", "Price", "Date", "Time"]
df = pd.DataFrame(columns=columns)
df = pd.read_csv(booking_info, index_col=0)

current_date = datetime.now()

q = 0
while q == 0:
    print()
    print("=======Menu=======")
    print("1) List / remove bookings")
    print("2) Number of employees needed")
    print("3) Quit")
    print()

    option = int(input("Please enter a number from the options above: "))
    if option < 1 or option > 3:
        continue

    if option == 1:
        print()
        print("===Current Bookings===")
        print(df)
        opt = input("Enter a booking row number to remove or 'q' to quit: ")
        if opt != "q" and opt.isnumeric() == True:
            opt = int(opt)
            df.drop([opt], inplace=True)
            df.to_csv(booking_info)
            print()

    elif option == 2:
        print()
        number_of_bookings = len(df)
        filtered_date = (df['Date'].astype(str).str.contains(str(current_date)))
        filtered_date_df = df[filtered_date]
        
        if number_of_bookings < 5 and number_of_bookings > 1:
            print("One employee needed.")
        elif number_of_bookings > 5 and number_of_bookings < 10:
            print ("Two employees needed.")
        elif number_of_bookings > 10 and number_of_bookings < 15:
            print("Three employees needed.")
        elif number_of_bookings > 15 and number_of_bookings < 20:
            print("Four employees needed.")

    elif option == 3:
        q = 1
    else:
        continue
