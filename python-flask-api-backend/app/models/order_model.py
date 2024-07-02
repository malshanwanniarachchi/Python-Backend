from flask_mysqldb import MySQL

class Order :
    def __init__(self):
        self.MYSQL = MySQL

        def create_order(self, user_id, menu_item_id, quantity, total_price):
            cur = self.mysql.connection.cursor()
            cur.execute("INSERT INTO Orders (user_id, menu_item_id, quantity, total_price) VALUES (%s, %s, %s, %s)", 
                    (user_id, menu_item_id, quantity, total_price))
            self.MYSQL.connection.commit()
            cur.close()