'''
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import datetime
now=datetime.datetime.now()
print("year | month ")
print(now.strftime("%Y-%m"))