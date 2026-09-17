from flask import Flask

app = Flask("myapp")

@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello, {name}!'