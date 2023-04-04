# Define a function to get a valid input from the user
def get_valid_input(prompt, validator):
    while True:
        user_input = input(prompt)
        if validator(user_input):
            return user_input
        else:
            if validator == is_valid_month:
                print("Error: Invalid Month Input")
            elif validator == is_valid_day:
                print("Error: Invalid Day Input")
            elif validator == is_valid_year:
                print("Error: Invalid Year Input")

# Define a function to validate a month input


def is_valid_month(month):
    return month.isdigit() and 1 <= int(month) <= 12

# Define a function to validate a day input


def is_valid_day(day):
    return day.isdigit() and 1 <= int(day) <= 31

# Define a function to validate a year input


def is_valid_year(year):
    return year.isdigit() and len(year) == 2


# Get input from user for month, day, and year
month = get_valid_input("Enter the month in numeric form: ", is_valid_month)
day = get_valid_input("Enter the day in numeric form: ", is_valid_day)
year = get_valid_input(
    "Enter the year as two numerical digits: ", is_valid_year)

# Print success message and formatted date
print("Success: Congratulations! you entered the correct date.")
print("{}/{}/{}".format(month, day, year))
