from flask import Blueprint, render_template, request


read = Blueprint('read', __name__)

@read.route('/', methods=['GET', 'POST'])
def home():
    data = request.form
    print(data)
    return render_template('index.html')

@read.route('/tables', methods=['GET', 'POST'])
def tables():
    return render_template('table.html')