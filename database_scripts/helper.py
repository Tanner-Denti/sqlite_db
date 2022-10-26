from table_classes.customer import Customer
from table_classes.representative import Representative
from table_classes.project import Project
from table_classes.timesheet import Timesheet

import sqlite3

class Helper:
    
    def __init__(self, database_name = ':memory:'):
        # Will create a new database if one doesn't already exist, otherwise connect to an existing db
        self.connection = sqlite3.connect(f'{database_name}')

        # Create a cursor object
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Use the cursor to create tables -----------------------------------------------------------

        # Representative
        self.cursor.execute("""CREATE TABLE representative (
            representative_id integer, 
            first_name text, 
            last_name text, 
            rank text, 
            wage integer, 
            street_address text, 
            city text, 
            state text
        )
        """)

        # Customer
        self.cursor.execute("""CREATE TABLE customer (
            customer_id integer, 
            first_name text, 
            last_name text,  
            pay_rate integer,  
            city text, 
            state text
        )
        """)

        # Project
        self.cursor.execute("""CREATE TABLE project (
            project_id integer, 
            representative_id integer,
            customer_id integer, 
            homeowner text,
            street_address text, 
            city text, 
            state text, 
            hours_worked real
        )
        """)

        # Timesheet
        self.cursor.execute("""CREATE TABLE timesheet (
            time_id integer,
            representative_id integer,
            customer_id integer, 
            project_id integer, 
            clock_in int,
            clock_out int
        )
        """)

        self.connection.commit()

    # Insert for each table -----------------------------------------------------------------------------
    def insert_representative(self, rep: Representative):
        with self.connection:
            self.cursor.execute("INSERT INTO representative VALUES\
            (:representative_id, :first_name, :last_name, :rank, :wage, :street_address, :city, :state)",
            {'representative_id' : rep.representative_id,
             'first_name' : rep.first_name,
             'last_name' : rep.last_name,
             'rank' : rep.rank,
             'wage' : rep.wage,
             'street_address' : rep.street_address,
             'city' : rep.city,
             'state' : rep.state
            })
            self.connection.commit()

    def insert_customer(self, cust: Customer):
        with self.connection:
            self.cursor.execute("INSERT INTO customer VALUES\
            (:customer_id, :first_name, :last_name, :pay_rate, :city, :state)",
            {'customer_id' : cust.customer_id,
             'first_name' : cust.first_name,
             'last_name' : cust.last_name,
             'pay_rate' : cust.pay_rate,
             'city' : cust.city,
             'state' : cust.state
            })
            self.connection.commit()

    def insert_project(self, project: Project):
        with self.connection:
            self.cursor.execute("INSERT INTO project VALUES\
            (:project_id, :representative_id, :customer_id, :homeowner, :street_address, :city, :state, :hours_worked)",
            {'project_id' : project.project_id,
             'representative_id' : project.representative_id,
             'customer_id' : project.customer_id,
             'homeowner' : project.homeowner,
             'street_address' : project.street_address,
             'city' : project.city,
             'state' : project.state,
             'hours_worked' : project.hours_worked
            })
            self.connection.commit()

    def enter_time(self, timesheet: Timesheet):
        with self.connection:
            self.cursor.execute("\
                INSERT INTO timesheet VALUES\
                (:time_id, :representative_id, :customer_id, :project_id, :clock_in, :clock_out)",
                {'time_id' : timesheet.time_id,
                 'representative_id' : timesheet.representative_id,
                 'customer_id' : timesheet.customer_id,
                 'project_id' : timesheet.project_id,
                 'clock_in' : timesheet.clock_in,
                 'clock_out' : timesheet.clock_out
                 })

    # Queries --------------------------------------------------------------------------------------------
    def get_rep_by_name(self, first_name: str, last_name: str):
        self.cursor.execute("\
            SELECT first_name, last_name, rank, wage, street_address, city, state\
            FROM representative\
            WHERE first_name = :first_name AND last_name = :last_name",
            {'first_name' : first_name, 'last_name' : last_name})
        return self.cursor.fetchall()

    def get_cust_by_name(self, first_name: str, last_name: str):
        self.cursor.execute("\
            SELECT first_name, last_name, pay_rate, city, state\
            FROM customer\
            WHERE first_name = :first_name AND last_name = :last_name",
            {'first_name' : first_name, 'last_name' : last_name})
        return self.cursor.fetchall()

    def get_project_by_homeowner(self, homeowner: str):
        self.cursor.execute("\
            SELECT homeowner, street_address, city, state, hours_worked\
            FROM project\
            WHERE homeowner = :homeowner",
            {'homeowner' : homeowner})
        return self.cursor.fetchall()
    
    # Update methods -------------------------------------------------------------------------
    def update_rep_wage(self, first_name: str, last_name: str, new_wage : int):
        with self.connection:
            self.cursor.execute("\
            UPDATE representative SET wage = :wage\
            WHERE first_name = :first_name AND last_name = :last_name",
            {'wage' : new_wage, 'first_name' : first_name, 'last_name' : last_name})

    def update_cust_pay_rate(self, first_name, last_name, new_rate):
        with self.connection:
            self.cursor.execute("\
            UPDATE customer SET pay_rate = :pay_rate\
            WHERE first_name = :first_name AND last_name = :last_name",
            {'pay_rate' : new_rate, 'first_name' : first_name, 'last_name' : last_name})

    def update_project_hours(self, homeowner, additional_hours):
        with self.connection:
            self.cursor.execute("\
            UPDATE project SET hours_worked = hours_worked + :hours\
            WHERE homeowner = :homeowner",
            {'homeowner' : homeowner, 'hours' : additional_hours})

    # Close the connection to the database once we are finished
    def close_connection(self):
        self.connection.close()


    

    