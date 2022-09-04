from flask import Flask

from config import config

# Routes
from routes import Status
app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Status.main, url_prefix='/api/status')
    app.run()
