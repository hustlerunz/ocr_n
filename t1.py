from flask import Flask, redirect, url_for, request ,render_template
import os 
from ocr_pro import ocr_core
UPLOAD_FOLDER = '/static/image/'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif','tiff','tif'])
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return redirect(url_for('upload'))
		userEmail = request.form['username']
		userPassword = request.form['password']
		return flask.redirect('/')
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template("index.html")

@app.route('/gen')
# ‘/’ URL is bound with hello_world() function.
def hello_world2():
    return 'gen'  

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))  
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()