import os
from flask import Flask
app = Flask(__name__)
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
from .rating import rating as rating_blueprint
app.register_blueprint(rating_blueprint)
from .feedback import feedback as feedback_blueprint
app.register_blueprint(feedback_blueprint)
from .customer_support import support as support_blueprint
app.register_blueprint(support_blueprint)
from .output_api import output as output_blueprint
app.register_blueprint(output_blueprint)
if __name__ == '__main__':
    app.run(threaded=True, port=5000)