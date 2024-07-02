from flask_mysqldb import MySQL

class Menu :
    def __init__(self):
        self.MYSQL = MySQL

    def get_all_menues(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM Menues")
        menues = cur.fetchall()
        cur.close()

        return menues