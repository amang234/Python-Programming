# The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. You are given the actual and the expected return dates. Calculate the fine as follows:
# a. If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
# b. If the book is returned in the same months the expected return date, Fine = 15 Rupees x Number of late days
# c. If the book is not returned in the same month but in the same year as the expected return date, Fine = 500 Rupees x Number of late months
# d. If the book is not returned in the same year, the fine is fixed at 10000 Rupees.

def calculate_fine(actual_return_date, expected_return_date):
    actual_day, actual_month, actual_year = map(int, actual_return_date.split())
    expected_day, expected_month, expected_year = map(int, expected_return_date.split())

    if actual_year > expected_year:
        return 10000
    elif actual_year == expected_year and actual_month > expected_month:
        return 500 * (actual_month - expected_month)
    elif actual_year == expected_year and actual_month == expected_month and actual_day > expected_day:
        return 15 * (actual_day - expected_day)
    else:
        return 0

# Example usage
actual_return_date = input("Enter the Actual Date")
expected_return_date = input("Enter the Expected Date")
fine = calculate_fine(actual_return_date, expected_return_date)
print(fine)
