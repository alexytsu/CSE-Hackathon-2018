from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Another_highly_secret_key'

