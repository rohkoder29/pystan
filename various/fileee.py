# use Python to execute shell (bash) commands

from os import system
from genericpath import exists
# from sys import argv

# print(system("echo `uptime`"))

file_path = "/home/rohkoder29/delete_snap_firefox.txt"
print(f"(Processing file) '{file_path}'")
with open(file_path, "r", encoding="utf-8") as stream:
    paths = stream.readlines()
for path in paths:
    if not exists(path.strip()):
        print(f"File '{path.strip()}' does not exist so not deleted.")
        continue
    file = path.strip()
    system(f"sudo rm {file}")
    print(f"File '{file}' deleted!")
