from flask import Blueprint, render_template


feedback = Blueprint('feedback', __name__)


@feedback.route('/feedback')
def index():
    # todo 
    return render_template('feedback/Feedback.html')

