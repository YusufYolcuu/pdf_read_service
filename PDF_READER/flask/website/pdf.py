from flask import Blueprint, render_template


pdf = Blueprint('pdf', __name__)

@pdf.route('/tables', methods=['GET', 'POST'])
def tables():
    return render_template('table.html')