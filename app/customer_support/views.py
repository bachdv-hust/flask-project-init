from flask import Blueprint, render_template


support = Blueprint('support', __name__)


@support.route('/customer_support')
def index():
    return render_template('customer_support/CustomerCare.html')

