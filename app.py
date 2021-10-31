from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'
@app.route('/greet')
@app.route('/greet/khan')
def greet(name="khan"):
    return "Hello {}".format(name)

if __name__ == '__main__':
    app.run()
