import sqlite3

connection  = sqlite3.connect("STUDENTS.db")
cursor = connection.cursor()

create_table_querry = """
    CREATE TABLE IF NOT EXISTS STUDENTS(
        NAME VARCHAR(25),
        MARKS INT,
        COURSE VARCHAR(25),
        SECTION VARCHAR(25)
        );
    """

cursor.execute(create_table_querry)


sql_query_add= """INSERT INTO STUDENTS(NAME, MARKS, COURSE, SECTION) VALUES (?,?,?,?)"""

values = [
    ('ALI', 92, 'DATA SCIENCE', 'A'),
    ('Arslan', 22, 'DATA SCIENCE', 'B'),
    ('Ahmad', 42, 'DATA SCIENCE', 'A'),
    ('Hamza', 62, 'DATA SCIENCE', 'B'),
    ('Wali', 82, 'DATA SCIENCE', 'C'),
    ('BAsit', 42, 'DATA SCIENCE', 'C'),
    ('Shahroz', 62, 'DATA SCIENCE', 'C'),
    ('Hurrarah', 87, 'DATA SCIENCE', 'B'),
    ('Shoaib', 78, 'DATA SCIENCE', 'B'),
]


data = cursor.executemany(sql_query_add,values)
connection.commit()

data = cursor.execute("""SELECT * FROM STUDENTS""")

for row in data:
    print(row)

if connection:
    connection.close()