import streamlit as st
import pandas as pd

# Program to display the data
import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "yourusername",
password = "yourpass",
database = "yourdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM CUSTOMERS")

# This SQL statement selects all data from the CUSTOMER table.
result = mycursor.fetchall()

# Printing all records or rows from the table.
# It returns a result set.
for all in result:
  st.info(all)
