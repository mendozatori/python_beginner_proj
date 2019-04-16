# Programmer: Victoria Mendoza

class Patient:
    # define the accepted arguments
    def __init__(self, fname, mname, lname, address, city, state, zip, phone, emergency_name, emergency_phone):
        self.__fname = fname
        self.__mname = mname
        self.__lname = lname
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone = phone
        self.__emergency_name = emergency_name
        self.__emergency_phone = emergency_phone

# set methods
    def set_fame(self, fname):
        return self.__fname

    def set_mname(self, mname):
        return self.__mname

    def set_lname(self, lname):
        return self.__lname

    def set_address(self, address):
        return self.__address

    def set_city(self, city):
        return self.__city

    def set_state(self, state):
        return self.__state

    def set_zip(self, zip):
        return self.__zip

    def set_phone(self, phone):
        return self.__phone

    def set_emergency_name(self, emergency_name):
        return self.__emergency_name

    def set_emergency_phone(self, emergency_phone):
        return self.__emergency_phone

# get methods
    def get_fame(self):
        return self.__fname

    def get_mname(self):
        return self.__mname

    def get_lname(self):
        return self.__lname

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def get_phone(self):
        return self.__phone

    def get_emergency_name(self):
        return self.__emergency_name

    def get_emergency_phone(self):
        return emergency_phone

# method to display the patient info
    def display_patient(self):
        print("-----------Patient Info-----------")
        print("First Name:", self.__fname)
        print("Middle Name:", self.__mname)
        print("Last Name:", self.__lname)
        print("Address:", self.__address)
        print("City:", self.__city)
        print("State:", self.__state)
        print("Zip:", self.__zip)
        print("Phone:", self.__phone)
        print("Emergency Contact:", self.__emergency_name)
        print("Emergency Contact Phone:", self.__emergency_phone)



class Procedure:
    # define the accepted arguments
    def __init__(self, procedure, date, practitioner, charges):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges
# set methods
    def set_procedure(self, procecure):
        return self.__procedure

    def set_date(self, date):
        return self.__date

    def set_practitioner(self, practitioner):
        return self.__practitioner

    def set_charges(self, charges):
        return self.__charges
# get methods
    def get_procedure(self):
        return self.__procedure

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

# method to display the procedure
    def display_procedure(self):
        print("----------Procedure----------")
        print("Procedure name:", self.__procedure)
        print("Date:", self.__date)
        print("Practitioner:", self.__practitioner)
        print("Charge:", self.__charges)







