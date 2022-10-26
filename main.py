from time import strftime
from table_classes.customer import Customer
from table_classes.representative import Representative
from table_classes.project import Project
from table_classes.timesheet import Timesheet

from database_scripts.helper import Helper

import sqlite3
import datetime

def main():
    # Create a database helper object
    # Uncomment this line, and comment out the one below it if you wish to save the database file for reuse
    #helper = Helper("my_database_name.db") # Saves the db in storage, long term
    helper = Helper() # Saves the db in RAM, short term

    # Startup the project tables
    helper.create_tables()

    # Create some objects to hold data
    representative_one = Representative(1, 'Rebekah', 'Barzee', 'Owner', 0, '1111 bottom of the sea', 'Rexburg', 'Idaho')
    representative_two = Representative(2, 'Adam', 'Chamberline', 'Employee', 18, '2222 middle of nowhere', 'Arlington', 'Virginia')

    customer_one = Customer(1, 'Tony', 'McCammon', 50, 'St. George', 'Utah')

    project_one = Project(1, 2, 1, 'Savorie', '3333 pineapple grove', 'Burleson', 'Utah', 0)

    # Insert time using datetime
    # time_in = datetime.time(hour=14, minute=30)
    # time_out = datetime.time(hour=17, minute=45)
    # timesheet_one = Timesheet(1, 2, 1, 1, strftime('%s'('time_in',)), strftime('%s', ('time_out',)))

    # Insert rows into the different tables
    helper.insert_representative(representative_one)
    helper.insert_representative(representative_two)
    helper.insert_customer(customer_one)
    helper.insert_project(project_one)
    #helper.enter_time(timesheet_one)

    # Take a look at what we just inserted
    print()
    print(helper.get_rep_by_name('Rebekah', 'Barzee'))
    print(helper.get_rep_by_name('Adam', 'Chamberline'))
    print(helper.get_cust_by_name('Tony', 'McCammon'))
    print(helper.get_project_by_homeowner('Savorie'))
    print()

    # Update rep wages
    helper.update_rep_wage('Adam', 'Chamberline', 22)
    helper.update_cust_pay_rate('Tony', 'McCammon', 75)
    helper.update_project_hours('Savorie', 8)
    print()

    # Display the updates
    print(helper.get_rep_by_name('Adam', 'Chamberline'))
    print(helper.get_cust_by_name('Tony', 'McCammon'))
    print(helper.get_project_by_homeowner('Savorie'))

    # Close the connection to the database once we are finished
    helper.close_connection()

if __name__ == "__main__":
    main()