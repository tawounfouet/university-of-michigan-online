import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("Counts.sqlite")
cur = conn.cursor()

# Create a new table 'Counts'
cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute(
    """
CREATE TABLE Counts (org TEXT, count INTEGER)
"""
)

# Prompt for file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"

# Open the file with 'latin-1' encoding to avoid UnicodeDecodeError
with open(fname, "r", encoding="latin-1") as fh:
    for line in fh:
        if not line.startswith("From: "):
            continue
        pieces = line.split()
        email = pieces[1]
        domain = email.split("@")[1]

        cur.execute("SELECT count FROM Counts WHERE org = ? ", (domain,))
        row = cur.fetchone()

        if row is None:
            cur.execute(
                """INSERT INTO Counts (org, count)
                    VALUES (?, 1)""",
                (domain,),
            )
        else:
            cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (domain,))
    conn.commit()

# Retrieve and print the top 10 organizations by email count
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
