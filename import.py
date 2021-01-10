import csv
from sys import argv, exit
from cs50 import SQL

# Set up database connection with student database:
db = SQL("sqlite:///students.db")

# If incorrect number of arguments given, error and exit:
if len(argv) != 2:
    print("Incorrect number of arguments given")
    exit(1)

# Save csv file to a variable
csv_file = (argv[1])
# Open csv file for reading
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        birth = int(row["birth"])
        house = row["house"]
        # Split names on spaces
        name = row["name"].split()
        first_name = name[0]
        # Account for differences in name lengths
        if len(name) == 2:
            middle_name = None
            last_name = name[1]
        else:
            middle_name = name[1]
            last_name = name[2]

        # Insert data for each row into the student database
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
            first_name, middle_name, last_name, house, birth)

