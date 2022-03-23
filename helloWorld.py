# Core web app using flask
# Download flask if you haven't
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

# If you want to put this on the internet, use something like heroku to deploy it.
