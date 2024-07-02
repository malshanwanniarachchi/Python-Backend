from flask import Blueprint, jsonify
from app.models.employee_model import Employee

employee_dp = Blueprint('employees',__name__)
employee_model = Employee()

@employee_dp.route('/employee', methods=['GET'])
def get_employee():
    employees = employee_model.get_all_employees()
    return  jsonify(employees)