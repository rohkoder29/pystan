#!/usr/bin/env python3

'''
A CLI TODO list app in python as part of my learning process of OOP.
What it does is basically create a collection (which is a set of tasks)
and add task(s). Operations on collections include the CRUD stack.
A CSV file is used here to store the collections.
And I also use the rich library to make thing a little bit funky.
In-depth info in the respective files containing each part of the app.
Please be aware of the licensing aspect of this project.
'''

__author__ = 'rohkoder'
__version__ = '0.1.0'
__license__ = 'MIT'

# imports
from csv import reader, DictReader, writer, DictWriter
from os import SEEK_END, SEEK_SET
from string import punctuation
from typing_extensions import LiteralString
from collection import Collection
from task import Task
from menu import Menu


def main() -> None:
    '''  '''
    def validate_collection_name() -> str:
        while True:
            try:
                coll_title = input("Input collection name [1-50 characters]: ")
                assert not coll_title.isspace()
                assert coll_title not in punctuation
                assert 1 <= len(coll_title) <= 52
            except AssertionError:
                print("Please insert a valid title.\n")
            else:
                return coll_title

    def validate_collection_content() -> LiteralString:
        tasks = []
        while True:
            try:
                task_title = input("Input task [1-50 characters] [Enter to finish]: ")
                assert not task_title.isspace()
                assert len(task_title) <= 52
                if not task_title:
                    break
            except AssertionError:
                print("Please double check the entry.")
                continue
            else:
                tasks.append(task_title)
        return ";".join(tasks)

    def create_collection() -> dict:
        ''' Create a collection object and return a dict. '''
        col = Collection(validate_collection_name(), validate_collection_content())
        return {
            "title": col.getCollectionName(),
            "date": col.getCollectionDate(),
            "content": col.getCollectionContent(),
            "status": col.getCollectionStatus()}

    col1 = create_collection()
    print(col1)

    def add_collection_to_db() -> None:
        _file = "doclist.csv"
        header = ["title", "date", "content", "status"]
        with open(_file, "a+", encoding="utf8", newline=None) as stream:
            writedata = DictWriter(stream, fieldnames=header)
            writedata.writeheader()
            writedata.writerow(col1)
            print("Collection successfully added!")

    add_collection_to_db()


if __name__ == '__main__':
    ''' Entry point of the app '''
    main()
