import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres_password', host='localhost')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS groups ("
            "group_id SERIAL PRIMARY KEY,"
            "title VARCHAR(5) NOT NULL);")

cur.execute("CREATE TABLE IF NOT EXISTS students ("
            "student_id SERIAL PRIMARY KEY,"
            "name VARCHAR(100) NOT NULL, "
            "age SMALLINT NOT NULL, "
            "group_id INT REFERENCES groups(group_id));")

conn.commit()

cur.execute("INSERT INTO groups (title) VALUES ('К-31'), ('СО-31'), ('РТ-31');")

conn.commit()

cur.execute("INSERT INTO students (name, age, group_id) "
            "VALUES ('Карнаух Максим', 20, 1), ('Дубограй Денис', 19, 2), ('Журавко Егор', 19, 3);")

conn.commit()

cur.close()
conn.close()
