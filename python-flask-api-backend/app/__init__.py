from flask import Flask
from flask_cors import CORS
from config import Config
from .extension import db, ma

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

from .routes.customer_route import customer_bp
from .routes.employee_route import employee_dp
from .routes.menu_route import menu_dp
from .routes.order_route import order_dp

app.register_blueprint(customer_bp, url_prefix='/customers')
app.register_blueprint(employee_dp, url_prefix='/employees')
app.register_blueprint(menu_dp, url_prefix='/menu')
app.register_blueprint(order_dp, url_prefix='/orders')

with app.app_context():
    db.create_all()
