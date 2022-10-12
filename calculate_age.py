# Project: Calculate age in seconds

def calculate_age():
    seconds_or_years = input("Give me seconds (s) or years (y) : ")

    if seconds_or_years == 's':
        # Convert seconds to years
        user_value = input("Enter the number of seconds you've lived for: ")
        age_in_years = int(user_value) / 60 / 60 / 24 / 365
        print(f"You've lived for {age_in_years} years")

    elif seconds_or_years == 'y':
        # Convert the years to seconds
        user_value = input("Enter the number of years you've lived for: ")
        age_in_seconds = int(user_value) * 365 * 24 * 60 * 60
        print(f"You've lived for {age_in_seconds} seconds")


calculate_age()
