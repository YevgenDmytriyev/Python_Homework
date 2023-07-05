# task 1
import datetime
# Get the current datetime
current_datetime = datetime.datetime.now()
# Extract the year from the current datetime and convert it to a string
year = current_datetime.strftime("%Y")
# Print the year
print(year)

# task 2
from datetime import datetime
# Create a datetime object for a specific date
some_date = datetime(2021, 7, 14)
# Get the weekday of the given date (Monday is 0 and Sunday is 6)
current_weekday = some_date.weekday()
# Print the weekday
print(current_weekday)

# task 3
# Prompt the user to enter a year and convert it to an integer
year = int(input("Year:"))  
# Check if the year is a leap year
# Leap years are divisible by 4, but not divisible by 100 unless they 
# are also divisible by 400
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year")  # Print the message indicating that the year is a leap year
else:
    print(f"{year} is not a leap year")  # Print the message indicating that the year is not a leap year

# task 4
from datetime import datetime
# Prompt the user to enter a date string
date_as_string = input("date_as_string =")  
# Example input: "Feb 14 2021 8:30AM"
datetime_object = datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")
# Convert the date string to a datetime object using strptime() function
# The format code "%b %d %Y %I:%M%p" specifies the expected format of the date string
print(datetime_object)  # Print the datetime object

# task 5
from datetime import datetime
date_format = "%Y-%m-%d"
# Get the first date from the user input :2023-06-01
date1 = input("Enter the first date (YYYY-MM-DD): ")
date1_obj = datetime.strptime(date1, date_format)
# Get the second date from the user input :2023-06-08
date2 = input("Enter the second date (YYYY-MM-DD): ")
date2_obj = datetime.strptime(date2, date_format)
# Calculate the number of days between the two dates
delta = date2_obj - date1_obj
num_days = delta.days
# Display the result
print(f"The number of days between {date1} and {date2} is {num_days}.")

# task 6
from datetime import datetime
# Prompt the user to enter the two datetimes in the specified format: 
# 2023-06-09 10:00:00 and 2023-06-09 15:30:00
date1_str = input("Enter the first datetime (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second datetime (YYYY-MM-DD HH:MM:SS): ")
# Convert the input strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
# Calculate the difference between the two datetimes
diff = date2 - date1
# Calculate the number of hours between the two datetimes
hours = diff.total_seconds() / 3600
# Display the result
print(f"The number of hours between {date1} and {date2} is: {hours} hours")