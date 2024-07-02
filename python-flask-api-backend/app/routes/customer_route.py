from flask import Blueprint, request, jsonify
from app.models.customer_model import Customer
from app.extension import db

customer_bp = Blueprint('customers', __name__)

@customer_bp.route('/show/customer', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    result = [{'id': customer.id, 'name': customer.name, 'email': customer.email} for customer in customers]
    return jsonify(result)

@customer_bp.route('/add/customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added!'}), 201

@customer_bp.route('/update/customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    customer = Customer.query.get_or_404(customer_id)
    
    customer.name = data.get('name', customer.name)
    customer.email = data.get('email', customer.email)
    
    db.session.commit()
    
    return jsonify({'message': 'Customer updated!'})

@customer_bp.route('/delete/customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500