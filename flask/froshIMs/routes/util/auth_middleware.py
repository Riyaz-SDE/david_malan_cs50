from functools import wraps
from flask import session,redirect

def auth(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if not session.get('user'):
            print('auth midddleware working')
            return redirect('/login')
        print('2auth midddleware working',  session.get('user'))
        return f(*args,**kwargs)
    return wrapper