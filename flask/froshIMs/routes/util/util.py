from flask import Flask, render_template, request, session, redirect

def checkFieldExist(request = request, *fields, method = None):
    # def f():
    #     cond = False
    #     for field in fields:
    #         cond = cond or field not in request.form
    #     return cond
    # if f():
    #     return 'invalid data'
    if "username" not in request.form or "password" not in request.form :
        return 'invalid form data'
def isDataNull(*data):
    for value in data:
        if value:
            # break
            return ' one of the value is null' 
def auth(fieldName):
    if not session.get(fieldName):
        return redirect('/login')
