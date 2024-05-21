

```sql
sqlite3 pitch.sqlite3

CREATE TABLE Ages ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
  name VARCHAR(128), 
  age INTEGER
);


DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Elidh', 18);
INSERT INTO Ages (name, age) VALUES ('Dominick', 14);
INSERT INTO Ages (name, age) VALUES ('Karimas', 36);
INSERT INTO Ages (name, age) VALUES ('Sarra', 32);
INSERT INTO Ages (name, age) VALUES ('Concetta', 18);
INSERT INTO Ages (name, age) VALUES ('Milandra', 36);


SELECT hex(name || age) AS X FROM Ages ORDER BY X;

-- Output
436F6E63657474613138
446F6D696E69636B3134
456C6964683138
4B6172696D61733336
4D696C616E6472613336
53617272613332

.quit
```