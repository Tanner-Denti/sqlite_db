# Overview

I created a relational database for my wifes business. Here, she will be able to store and access data about people in her company, clients, projects, and hours worked on projects.

This software provides helper functions that make it simple to create tables, insert data, update data, and query data. The user can specify what they want by using this class framework.

I wanted to start this project in order to learn sqlite3, and make something that may be useful to my wife. 


[Software Demo Video](https://www.loom.com/share/6bf82d89d86e4223a5d945d08435e6b3)

# Relational Database

This is a SQLite relational database

This database has four tables. The representative and customer tables both have a one to many relationship with the project table, and all three of those tables have a one to many relationship with the timesheet table.

# Development Environment

SQLite comes natively with python, so all you need to do is import the sqlite3 library to get started.

I felt like SQLite was very convenient for this project, however it does feel slightly different than other relational databases like MySQL and Oracle. 

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [sqlite3 python docs](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)
* [sqlite3 docs](https://www.sqlite.org/datatype3.html)

# Future Work

* Expand this database to be more comprehensive so that every piece of data that my wife would like to store can be stored.
* Create a GUI where a user can run preset queries, insert, update, and delete rows of data, and create new tables would be really nice. 
* Create more advanced and helpful queries.