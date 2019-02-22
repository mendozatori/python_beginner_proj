# Average Rainfall Application

# CONSTANTS
NUM_MONTHS = 12

# initialize
total_inches = 0.0

# input
years = int(input("How many years are we calculating for? "))
while years < 0:
        print("Please enter a valid number of years!")
        years = int(input("How many years are we calculating for? "))

# x will continue to increment by 1 until it reaches number of years inputted
for x in range(years):
    print('')
    print('---------------------')
    print("RAINFALL FOR YEAR " + str(x + 1))
    print('---------------------')
    print('')
    # y will continue to increment by 1 until it reaches 12 "months"
    for y in range(NUM_MONTHS):
        month_rain = float(input("Inches of rainfall for month " + str(y + 1) + ": "))
        while month_rain < 0:
            print("Please enter a valid number of inches of rainfall!")
            month_rain = float(input("Inches of rainfall for month " + str(y + 1) + ": "))
        total_inches = total_inches + month_rain

# calculations
total_months = NUM_MONTHS * years
average_rainfall = total_inches / total_months

print('')
print("-------SUMMARY--------")
print("Number of months: ", total_months)
print("Total inches of rainfall: ", total_inches)
print("Average rainfall per month: ", average_rainfall)