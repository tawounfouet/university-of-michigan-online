import sqlite3

# Create a connection to the SQLite database in memory
db = sqlite3.connect(':memory:')

# Get a cursor object
cursor = db.cursor()

# Create the Ages table
cursor.execute('''
CREATE TABLE Ages (
    name VARCHAR(128),
    age INTEGER
)
''')

# Ensure the table is empty
cursor.execute('DELETE FROM Ages')

# Insert the specified rows
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Amieleigh', 34)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Choire', 34)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Aden', 34)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Lukas', 35)")

# Commit the changes to the database
db.commit()

# Select the required data
cursor.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

# Retrieve the first row
user1 = cursor.fetchone()

# Print the first column retrieved (hex value)
print("The first row in the resulting record set: " + user1[0])

# Close the database connection
db.close()
