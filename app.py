from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Application Flask
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simulated user database
users = {"user@example.com": {"password": "password123"}}

# User class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Login form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=50)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# Register form
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=50)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

# Routes
@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/index')
@login_required
def index():
    return render_template("index.html", user=current_user.id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email in users and users[email]["password"] == password:
            user = User(email)
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email not in users:
            users[email] = {"password": password}
            flash("Registration successful! You can now log in.", "success")
            return redirect(url_for('login'))
        else:
            flash("Email already exists.", "danger")
    return render_template("register.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
