from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/welcome/')
def welcome():
    return "welcome"

if __name__=="__main__":
    app.run()