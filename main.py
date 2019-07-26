from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f35ce59fdef81e127fd51e37008d4e13'

@app.route('/')
@app.route('/home')
def hello():
    return render_template('index.html')

@app.route('/login')
def form():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
