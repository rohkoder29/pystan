qtyStud = int(input("How many students? "))
allStud = []

for _ in range(qtyStud):
    student = {
        "name": input("Enter student's name: "),
        "notes": [
            int(input(f"Enter student's note for period {i+1}: "))
            for i in range(3)
        ],
    }
    student["avg"] = round((sum(student.get("notes")) / 3))
    allStud.append(student)


for item in allStud:
    print(
        f'Student {item["name"].title()} averages {item["avg"]}/10 this year.'
    )
    if item["avg"] > 5:
        print(">> Eligible to promote.")

# print(allStud)
