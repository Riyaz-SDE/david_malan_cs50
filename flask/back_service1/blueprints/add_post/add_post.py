from flask import Blueprint, render_template, request

postApi = Blueprint("add_post",__name__,template_folder = 'login_templates')

@postApi.route('/',methods = ['POST'])
def addPost():
    # if request.form.length != 0:
    print(request.form)
    value = request.form
    return 'success'