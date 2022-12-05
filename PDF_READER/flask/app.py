from website import create_app

app = create_app()


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug=True)
      







# from flask import Flask, jsonify, render_template
# import socket

# app = Flask(__name__)


# # funtion to fetch hostname and ip
# def fetchDetails():
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#     return str(hostname), str(ip_address) 


# @app.route("/")
# def index():
#     hostname,ip = fetchDetails()
#     return render_template('index.html', hostname=hostname, ip=ip)


# def create_app():
#    return app

# @app.route('/up')
# def up():
#     return jsonify(
#         status = 'UP'
#     )


# if __name__ == '__main__':
#       app.run(host='0.0.0.0', port=80)