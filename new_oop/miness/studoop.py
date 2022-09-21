import csv
from random import randint, uniform
from typing import Iterator


# class definition
class Student:
    all = []    # store all created objects
    def __init__(self, name, age, gpa) -> None:
        self.name = name
        self.age = age
        self.gpa = gpa

        # keep track of created objects
        Student.all.append(self)

    # convert objects into iterators
    def __iter__(self) -> Iterator:
        return iter([self.name, self.age, self.gpa])

    # format object represention
    def __repr__(self) -> str:
        return f'Student(Name: "{self.name.title()}", Age: {self.age}, GPA: {self.gpa})'


if __name__ == "__main__":
    ## instanciation
        # input validation
    def validate_input() -> int:
        while True:
            try:
                num_stud = int(input("How many students? "))
                assert num_stud >= 1
            except AssertionError:
                print("Number must be greater or equal to one (1).")
                continue
            except ValueError:
                print("Expected an integer. Please try again.")
            else:
                return num_stud
        # object creation
    def create_student() -> list:
        all_stud = []
        for i in range(validate_input()):
            stud = Student(input(f"Student {i + 1} name: "), randint(16, 19), round(uniform(2.8, 3.8), 1))
            all_stud.append(stud)
        return all_stud

    # add objects to database (CSV file)
    try:
        _file = "studoop.csv"
        with open(_file, "w", encoding="utf8", newline=None) as f:
            write = csv.writer(f)
                # add header (columns)
            header = ["name", "age", "gpa"]
            write.writerow(header)
                # add actual content (rows)
            content = create_student()  # ok at this point it... doesn't work
            write.writerows(content)    # so we gotta tweak around to convert
                                        # the objects into iterables
                                        # we can achieve that either by creating
                                        # a function or by implementing the __iter__
                                        # method directly in the class definition
                                        # I'll use the latter, and TADA!!
    except BaseException as e:
        print(f"BaseException: {_file}")

    # show the objects in the file
    with open(_file, "r", encoding="utf8", newline=None) as f:
        read = csv.reader(f, skipinitialspace=True)
        header = next(read)
        if header:
            for row in read:
                student = Student(*row)
                print(student)
