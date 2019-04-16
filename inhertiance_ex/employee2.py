# Programmer: Victoria Mendoza

# imports
import employee

def main():
    # inputs
    emp_name = input("Please enter your name: ")
    emp_num = int(input("Please enter your employee number: "))
    shift_num = int(input("Please enter your shift number: "))

    valid_shift = [1, 2]
    while True:
        if shift_num in valid_shift:
            break
        else:
            print("Please enter a valid shift number!")
            shift_num = int(input("Please enter your shift number: "))

    pay_rate = float(input("Please enter your pay rate: "))

    if shift_num == 1:
        shift_name = 'Day shift'
    elif shift_num == 2:
        shift_name = "Night shift"

    # create an instance of class
    emp = employee.ProductionWorker(emp_name, emp_num, shift_num, pay_rate)

    # display info
    print("")
    print("---------Employee Info---------")
    print("Employee Name:", emp_name)
    print("Employee Number:", emp_num)
    print("Shift Number:", shift_num)
    print("Shift Name:", shift_name)
    print("Pay Rate:", '${:,.2f}'.format(pay_rate))


main()
