from flask import Flask
from flask import render_template
from flask import abort
from flask import request


app = Flask(__name__)


@app.route('/')
def root_page():
    return render_template('index.html', title1='Rec', title2='repo')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
