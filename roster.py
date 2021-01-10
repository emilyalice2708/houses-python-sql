from cs50 import SQL
from sys import argv, exit

#check number of arguments
if len(argv) != 2:
    print("Incorrect number of arguments given")
    exit(1)

# Connect with student database
db = SQL("sqlite:///students.db")

# Save input as house variable
house = argv[1]

# Query the database
students = db.execute(("SELECT * FROM students WHERE house = ? ORDER BY last, first"), house)

# For each row, print names and birth, accounting for potential NULL middle name
for row in students:
    print(f"{row['first']} {row['middle'] + ' ' if row['middle'] else ''}{row['last']}, born in {row['birth']}")

