from flask import Blueprint, jsonify
from app.models.menu_model import Menu

menu_dp = Blueprint('menu', __name__)
menu_model = Menu()

@menu_dp.route('/menu', methods=['GET'])
def get_menues():
    menues = menu_model.get_all_menues()
    return jsonify(menues)