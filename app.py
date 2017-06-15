from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/uploader', methods = ['POST'] )
def upload_photo():
	photo = request.files['photo']
	resp = app.make_response(photo.read())
	resp.mimetype = 'image/jpeg'
	return resp

if __name__ == '__main__':
	app.run(debug = True)








