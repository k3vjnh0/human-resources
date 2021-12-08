from typing import List
from entity.employee import Employee
from entity.staff import Staff
from entity.teacher import Teacher
from entity.EDegree import Degree
from entity.EPosition import Position
import csv


class Employee_management:
    def __init__(self):
        self.lst_emp: List[Employee] = []

    def add_employee(self, employee: Employee):
        self.lst_emp.append(employee)

    def search_by_name(self, name: str):
        result = []

        for emp in self.lst_emp:
            if emp.get_full_name().lower() == name.lower():
                result.append(emp)

        return result

    def search_by_dept(self, dept: str):
        result = []

        for emp in self.lst_emp:
            if isinstance(emp, Staff):
                s = Staff(emp)
                if s.get_department().lower() == dept.lower():
                    result.append(emp)

            if isinstance(emp, Teacher):
                t = Teacher(emp)
                if t.get_faculty().lower() == dept.lower():
                    result.append(emp)

        return result

    def list_all(self):
        return self.lst_emp.sort()

    def save(self, employee: Employee, filename: str):
        with open(filename, "w", newline="") as data:
            writer = csv.writer(data)

            if isinstance(employee, Staff):
                s = Staff(employee)
                writer.writerow('Staff, ' + s + '\n')

            if isinstance(employee, Teacher):
                t = Teacher(employee)
                writer.writerow('Teacher, ' + t + '\n')

    def load(self, filename: str):
        pass
