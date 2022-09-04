from flask import Flask

from config import config

# Routes
from routes import Status, Category, Role, UserRole
app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Status.main, url_prefix='/api/status')
    app.register_blueprint(Category.main, url_prefix='/api/categories')
    app.register_blueprint(Role.main, url_prefix='/api/role')
    app.register_blueprint(UserRole.main, url_prefix='/api/user')

    app.run()
