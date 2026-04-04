from flask import Flask, render_template, request
from blueprints.login.login import loginapi
app = Flask(__name__)
app.register_blueprint(loginapi, url_prefix = '/login')
@app.route('/')

def index():
    # print(f'request intiated {request.args["`name`"]}')
    if "name" in request.args:
        print('d1')
        name = request.args["name"]
    else:
        print('d2')
        name = "world"
    return render_template("index.html",name = name)
    return ''

@app.route('/form') 
def form():
    return render_template("form.html")

@app.route('/greet')
def greet():
    if "name" in request.args:
        name = request.args["name"]
    else :
        name = "name"
    return render_template("index.html", name = name)
if __name__ == '__main__':
    app.run(debug = True)