from flask import Flask
from flask_cors import CORS
from models import db
import config
import routes

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
CORS(app)

app.register_blueprint(routes.bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)