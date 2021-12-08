from employee import Employee
from business.allowance_calculator import Allowance_Calculator


class Staff(Employee):
    def __init__(self):
        self.department = ''
        self.working_days = 0
        self.position = None
        self.allowance = Allowance_Calculator.calculate_allowance(self)

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_working_days(self):
        return self.working_days

    def set_working_days(self, working_days):
        self.working_days = working_days

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_salary(self):
        return (
            self.get_salary_ratio * 730
            + self.get_allowance
            + self.get_working_days * 30
        )

    def __str__(self):
        return (
            self.get_full_name()
            + ', '
            + self.get_department()
            + ', '
            + self.get_position()
            + ', '
            + self.get_salary_ratio()
            + ', '
            + self.get_allowance()
            + ', '
            + self.get_working_days()
            + ', '
            + self.get_salary()
        )
