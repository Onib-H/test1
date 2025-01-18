from flask import Flask
from Login.views import login_blueprint

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(login_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
