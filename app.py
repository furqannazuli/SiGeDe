from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inisialisasi objek di luar create_app()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sigede.db'

    db.init_app(app)
    login_manager.init_app(app)

    # Import blueprint DI DALAM fungsi untuk hindari circular import
    from routes.auth import auth_bp
    from routes.main import main_bp  # tambahkan ini
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)  # dan ini

    return app

# Jalankan aplikasi
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
