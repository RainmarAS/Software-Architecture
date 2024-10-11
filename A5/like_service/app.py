from flask import Flask
from models import db
from routes import like_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///likes.db'
db.init_app(app)

app.register_blueprint(like_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5003, debug=True)