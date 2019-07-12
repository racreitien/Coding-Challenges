from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return 'The form has been submitted! The username is {}. The password is {}.'.format(form.username.data, form.password.data)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)