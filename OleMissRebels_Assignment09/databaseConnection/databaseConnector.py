# File Name : OleMissRebels_Assignment09
# Student Name: Jack Driehaus and Drew Wolfe
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   04/03/2024
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  Work in a team to aacess the SQL server, extract data, and produce some interesting results

# Brief Description of what this module does: Connects to the SQL server database
# Citations: 

# Anything else that's relevant:

import pyodbc

def get_connection():
    conn_str = (
    'Driver={SQL Server};'
    'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
    'Database=GroceryStoreSimulator;' 
    'UID=IS4010Login;'
    'PWD=P@ssword2;'
    'TrustServerCertificate=yes;'
)
    return pyodbc.connect(conn_str)


