from flask import Blueprint, render_template


rating = Blueprint('rating', __name__)


@rating.route('/rating')
def index():
    return render_template('rating/Rating.html')

