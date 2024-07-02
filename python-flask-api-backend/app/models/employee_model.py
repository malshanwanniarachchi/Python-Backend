from flask_mysqldb import MySQL

class Employee :
    def __init__(self):
        self.MYSQL = MySQL

    def get_all_employees(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM Employees")
        employees = cur.fetchall()
        cur.close()

        return employees