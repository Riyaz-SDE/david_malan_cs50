from flask import Blueprint, session, render_template
logoutRoute = Blueprint('logoutRoute',__name__)
@logoutRoute.route('/', methods = ['POST'])
def logoutApi():
    
    if session.get('user') :
        session.clear() 
        print('session cleared')
    print('session cleared')
    return render_template('index.html')