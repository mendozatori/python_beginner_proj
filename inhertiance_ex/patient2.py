# Programmer: Victoria Mendoza

# imports
import patient
import datetime

def main():
    # patient instance
    patient1 = patient.Patient('Victoria', 'Tori', 'Mendoza', '123 Road', 'Waco', 'TX', '76706', '(123)456-7891',
                      'Mom Mendoza', '(234)567-8910')

    patient1.display_patient()

    # procedure 1
    procedure1 = patient.Procedure('Physical Exam', f"{datetime.datetime.now():%m-%d-%Y}", 'Dr. Irvine', '${:,.2f}'.format(250.00))

    procedure1.display_procedure()

    # procedure 2
    procedure2 = patient.Procedure('X-ray', f"{datetime.datetime.now():%m-%d-%Y}", 'Dr. Jamison',
                                        '${:,.2f}'.format(500.00))

    procedure2.display_procedure()

    # procedure 3
    procedure3 = patient.Procedure('Blood Test', f"{datetime.datetime.now():%m-%d-%Y}", 'Dr. Smith',
                                        '${:,.2f}'.format(200.00))

    procedure3.display_procedure()

# call on main function
main()
