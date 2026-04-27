from functools import wraps
from flask import session,redirect, jsonify

def auth(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if not session.get('user'):
            print('auth midddleware working')
            return jsonify({
                'message' : 'sesssion not found'
            }),401
            # return redirect('/login')
        print('2auth midddleware working',  session.get('user'))
        return f(*args,**kwargs)
    return wrapper