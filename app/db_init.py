import psycopg2
from app.config import Config


def init():
    conn = psycopg2.connect(dbname=Config.POSTGRES_DB,
                            user=Config.POSTGRES_USER,
                            password=Config.POSTGRES_PASSWORD,
                            host=Config.DB_HOST)
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
