import datetime
import io

import pytesseract
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for, session
from flask_oidc import OpenIDConnect

app = Flask(__name__)

# Secret key for sessions encryption
#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
oidc = OpenIDConnect(app)

@app.route('/')
def home():
    #return render_template("index.html", title="Image Reader")
    return 'hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)