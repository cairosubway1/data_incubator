from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TESTING"] = True


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/uploader', methods = ['GET','POST'] )
def upload_photo():
	if request.method == 'POST':
		photo = request.files['photo']
		resp = app.make_response(photo.read())	
		resp.mimetype = 'image/jpeg'
		return resp
	
if __name__ == '__main__':
	app.run(debug=True)








