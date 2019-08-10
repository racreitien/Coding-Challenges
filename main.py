from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '19sdfk130jar2380ha08hfoun1094jo'

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/register')
def register():
    form=RegistrationForm()
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
