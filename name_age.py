from datetime import date

# get name as a string
name = input("Hey what's ya name?!? ")

# get age as an int
age = int(input("How old are you? "))

# calculate birth year
current_year = date.today().year
birth_year = current_year - age

# print greeting
print(f"Hello, {name}! You were born in {birth_year}.")

