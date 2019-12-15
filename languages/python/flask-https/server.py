from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(ssl_context=('./server.crt', './server.key'))
    #app.run('0.0.0.0', debug=True, port=5000, ssl_context='adhoc')
