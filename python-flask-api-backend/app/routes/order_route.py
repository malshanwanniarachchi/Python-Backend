from flask import Blueprint, request, jsonify
from app.models.order_model import Order
from app.models.menu_model import Menu

order_dp = Blueprint('orders', __name__)
order_model = Order()
menu_model = Menu()

@order_dp.route('/create/order', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data['user_id']
    menu_item_id = data['menu_item_id']
    quantity = data['quantity']
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT price FROM Menu WHERE id = %s", (menu_item_id,))
    price = cur.fetchone()[0]
    total_price = price * quantity

    order_model.create_order(user_id, menu_item_id, quantity, total_price)
    return jsonify({'message': 'Order created successfully!'})
