from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'aassaass asssasss'


    from .read import read
    from .pdf import pdf

    app.register_blueprint(read,url_prefix='/')
    app.register_blueprint(pdf,url_prefix='/tables')

    
    return app
