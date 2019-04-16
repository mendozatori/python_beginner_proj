# Programmer: Victoria Mendoza

class Employee:
    def __init__(self, emp_name, emp_num):
        self.__emp_name = emp_name
        self.__emp_num = emp_num

# set methods
    def set_emp_name(self, emp_name):
        return self.__emp_name

    def set_emp_num(self, emp_num):
        return self.__emp_num
# get methods
    def get_emp_name(self):
        return self.__emp_name

    def get_emp_num(self):
        return self.__emp_num


class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_num, shift_num, pay_rate):
        # reference super class and its attributes
        Employee.__init__(self, emp_name, emp_num)

        # new attributes
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

# set methods
    def set_shift_num(self, shift_num):
        return self.__shift_num

    def set_pay_rate(self, pay_rate):
        return self.__pay_rate

# get methods
    def get_shift_num(self):
        return self.__shift_num

    def get_pay_rate(self):
        return self.__pay_rate



