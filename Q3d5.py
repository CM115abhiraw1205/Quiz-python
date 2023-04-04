# Define a function to convert a salary to a different currency.
def convert_salary(salary, country):
    # Define a dictionary of conversion rates for different countries.
    conversion_rates = {
        'Canada': 1.47,
        'USA': 1.10,
        'Cambodia': 4440.67,
        'United Kingdom': 0.88
    }
    # Define a dictionary of currency names for different countries.
    currency_names = {
        'Canada': 'CAD',
        'USA': 'USD',
        'Cambodia': 'Cambodian riel',
        'United Kingdom': 'Pound Sterling'
    }
    # Check if the input country is valid.
    if country not in conversion_rates:
        return f"Invalid input. {country} is not a valid country."

    # Convert the salary to the currency of the specified country.
    converted_salary = salary / conversion_rates[country]
    # Get the currency name.
    currency_name = currency_names[country]
    # Return the converted salary and the currency name.
    return (converted_salary, currency_name)

# Define a function to compare a converted salary to the average salary in a country.


def compare_salary(converted_salary, country):
    # Define a dictionary of average salaries for different countries.
    average_salaries = {
        'Canada': 64000,
        'USA': 56516,
        'Cambodia': 5649856,
        'United Kingdom': 35423
    }
    # Check if the input country is valid.
    if country not in average_salaries:
        return f"Invalid input. {country} is not a valid country."
    # Get the average salary in the specified country.
    avg_salary = average_salaries[country]
    # Compare the converted salary to the average salary in the specified country.
    if converted_salary > avg_salary:
        return f"You will be rich in {country} with a salary of {converted_salary:.2f} {currency_name}"
    else:
        return f"You will be poor in {country} with a salary of {converted_salary:.2f} {currency_name}"


# Get input from the user for the salary in Germany and the country they want to migrate to.
salary = input("Please enter your salary in Germany: ")
country = input("Enter the country you want to migrate to: ")

# Convert the salary to a float.
try:
    salary = float(salary)
except ValueError:
    print("Invalid input. Salary must be a number.")
    exit()

# Convert the salary to the currency of the specified country.
converted_salary, currency_name = convert_salary(salary, country)
# Compare the converted salary to the average salary in the specified country.
print(compare_salary(converted_salary, country))
