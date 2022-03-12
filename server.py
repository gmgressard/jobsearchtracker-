from flask import Flask, render_template 
from model import connect_to_db

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('home.html')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')