from flask import Flask
from extensions import db
from flask_cors import CORS
from routes import journal, summary

def create_app(config_object="settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    CORS(app)

    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    #     print("table created")
    return app

def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)

    return None

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(journal.views.blueprint)
    app.register_blueprint(summary.views.blueprint)
    return None

app = create_app()

if __name__ == "__main__":    
    app.run()
