from flask import Blueprint,  render_template

loginapi = Blueprint('login', __name__, template_folder = 'templates')
# login_api.
@loginapi.route('/')
def login():
    print("hi")
    return render_template('index1.html')