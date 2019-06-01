from flask import Flask
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("wallet.html")

# include this for local dev

if __name__ == '__main__':
    app.run()
