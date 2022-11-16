import psycopg2
from app.config import Config


def load_all_students():
    conn = psycopg2.connect(dbname=Config.POSTGRES_DB,
                            user=Config.POSTGRES_USER,
                            password=Config.POSTGRES_PASSWORD,
                            host=Config.DB_HOST)
    cur = conn.cursor()

    cur.execute("SELECT students.name, g.title FROM students "
                "JOIN groups g on g.group_id = students.group_id;")

    students = []
    for row in cur.fetchall():
        students.append({"name": row[0], "group": row[1]})

    cur.close()
    conn.close()
    return students


if __name__ == '__main__':
    print(load_all_students())
