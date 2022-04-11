from flask import Flask
from routes.auth import routes_auth
from routes.test_service import test_service
from dotenv import load_dotenv
app = Flask(__name__)

app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(test_service, url_prefix="/api")


if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port="4000", host="0.0.0.0")
    