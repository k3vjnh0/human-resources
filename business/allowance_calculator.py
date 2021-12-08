from entity.staff import Staff
from entity.teacher import Teacher
from entity.EDegree import Degree
from entity.EPosition import Position


class Allowance_Calculator:
    def calculate_allowance(self, employee):
        allowance = 0

        if isinstance(employee, Staff):
            s = Staff(employee)
            if s.get_position() == Position.HEAD:
                allowance = 2000

            if s.get_position() == Position.VICE_HEAD:
                allowance = 1000

            if s.get_position() == Position.STAFF:
                allowance = 500

        if isinstance(employee, Teacher):
            t = Teacher(employee)
            if t.get_degree() == Degree.BACHELOR:
                allowance = 300

            if t.get_degree() == Degree.MASTER:
                allowance = 500

            if t.get_degree() == Degree.DOCTOR:
                allowance = 1000

        return allowance
