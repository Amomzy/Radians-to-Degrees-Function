import math

# Define the function and parameter(s)
def radians_to_degrees(rad):
    # Initialize main loop
    while True:
        degrees = rad * (180 / math.pi)
        print(f"{rad:.0f} radians = {degrees:.2f} degrees.")

        # Ask user if they want to continue
        choice = input("Would you like to enter another number? y/n ").lower()

        # Validate the input
        while choice not in ["y", "n"]:
            choice = input("Invalid input! Please select 'y' or 'n': ").lower()

        # Get new rad value to keep loop going OR end function
        if choice == "y":
            try:
                rad = float(input("Enter the new radians: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        else:
            return "Goodbye!"

# Prompt user for initial input and validate
while True:
    try:
        radians = float(input("Enter the radians of the angle: "))
        break # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input! Please restart and enter a numeric value.")

# Start conversion process
print(radians_to_degrees(radians))
