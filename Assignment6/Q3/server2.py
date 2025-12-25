from flask import Flask

server = Flask(__name__)

@server.get('/')
def homepage():
    return "This is a home page"

@server.get('/welcome')
def welcome():
    return "<html><body><h1>Welcome to Student Management System</h1></body></html>"

@server.post('/lightintensity/<int:light>')
def post_lightintensity(light):
    print(f"light = {light}")
    return f"{light} is received"

server.run(host="127.0.0.1", port=5001, debug=True)