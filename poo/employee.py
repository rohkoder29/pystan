#!/usr/bin/env python3


class Employee:
    company = "RohkoTek"

    def __init__(self, f_name, l_name, age, gender, email) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.email = email


emp1 = Employee("John", "Smith", 34, "M", "j.smith@rktek.com")
print(f"M. {emp1.l_name} is {emp1.age}", flush=True)
print("Working with us since whatever.")
