
# Includes all modules in this project.
import sys
import os
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0, app_path)
base_path = os.path.join(app_path, '..')
sys.path.insert(0, base_path)

from flask import Flask
from api import controller

import logging
logger = logging.getLogger(__name__)



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.register_blueprint(controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9083)