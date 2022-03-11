
Python 2.6 أو أعلى مطلوب لتركيب Flask. يمكنك البدء في Flask الاستيراد من حزمة Flaskعلى أي بيثون IDE. للتثبيت على أي بيئة، يمكنك النقر فوق رابط التثبيت الوارد أدناه.
لاختبار أنه إذا كان التثبيت يعمل، تحقق من هذا الرمز الوارد أدناه.
# an object of WSGI application
from flask import Flask	
app = Flask(__name__) # Flask constructor

# A decorator used to tell the application
# which URL is associated function
@app.route('/')	
def hello():
	return 'HELLO'

if __name__=='__main__':
app.run()
باستخدام المتغيرات فيFlask :                          

from flask import Flask
app = Flask(__name__)

# routing the decorator function hello_name
@app.route('/hello/<name>')
def hello_name(name):
return 'Hello %s!' % name

if __name__ == '__main__':
app.run(debug = True)
......................................
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<postID>')
def show_blog(postID):
return 'Blog Number %d' % postID

@app.route('/rev/<revNo>')
def revision(revNo):
return 'Revision Number %f' % revNo

if __name__ == '__main__':
app.run()

# say the URL is http://localhost:5000/blog/555
.............................................
بناء عنوان URL في Flask:                                               
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin') #decorator for route(argument) function
def hello_admin():	 #binding to hello_admin call
return 'Hello Admin'	

@app.route('/guest/<guest>')
def hello_guest(guest): #binding to hello_guest call
return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):	
if name =='admin': #dynamic binding of URL to function
	return redirect(url_for('hello_admin'))
else:
	return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__':
app.run(debug = True)
.............................................
التعامل مع الملفات الثابتة:                                          
    from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
return render_template("index.html")

if __name__ == '__main__':
app.run(debug = True)
..................................................
رمز HTML التالي:                                                          
    <html>

<head>
	<script type = "text/javascript"
		src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
</head>
	
<body>
	<input type = "button" onclick = "sayHello()" value = "Say Hello" />
</body>
	
</html>
.................................................
Cookies:

    from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
return render_template('index.html')

HTML code for index.html
<html>
<body>
	
	<form action = "/setcookie" method = "POST">
		<p><h3>Enter userID</h3></p>
		<p><input type = 'text' name = 'nm'/></p>
		<p><input type = 'submit' value = 'Login'/></p>
	</form>
		
</body>
</html>
.................................................
أضف هذا الرمز إلى ملف Python المحدد أعلاه                           
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
if request.method == 'POST':
	user = request.form['nm']
	
resp = make_response(render_template('cookie.html'))
resp.set_cookie('userID', user)
	
return resp

@app.route('/getcookie')
def getcookie():
name = request.cookies.get('userID')
return '<h1>welcome '+name+'</h1>'

HTML code for cookie.html
<html>
	<body>
		<a href="/getcookie">Click me to get Cookie</a>
</body>
</html>
.......................................................
and following python code of Flask is:

    
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
  
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
      
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'          
if __name__ == '__main__':
   app.run(debug = True)
..................................................

إرسال بيانات النموذج إلى ملف HTML للخادم:                    
    from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student():
return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
if request.method == 'POST':
	result = request.form
	return render_template("result.html", result = result)

if __name__ == '__main__':
app.run(debug = True)

……………………………..
<!doctype html>
<html>
<body>
	
	<table border = 1>
		{% for key, value in result.items() %}
		
			<tr>
			<th> {{ key }} </th>
			<td> {{ value }} </td>
			</tr>
			
		{% endfor %}
	</table>
		
</body>
</html>
................................................
<html>
<body>
	
	<form action = "http://localhost:5000/result" method = "POST">
		<p>Name <input type = "text" name = "Name" /></p>
		<p>Physics <input type = "text" name = "Physics" /></p>
		<p>Chemistry <input type = "text" name = "chemistry" /></p>
		<p>Maths <input type ="text" name = "Maths" /></p>
		<p><input type = "submit" value = "submit" /></p>
	</form>
</body>
</html>

.............................................
الرسالة هي النص الفعلي الذي سيتم عرضه وفئة هو اختياري هو تقديم أي خطأ أو معلومات.
from flask import Flask
app = Flask(__name__)

# /login display login form
@app.route('/login', methods = ['GET', 'POST'])

# login function verify username and password
def login():	
error = None
	
if request.method == 'POST':
	if request.form['username'] != 'admin' or \
		request.form['password'] != 'admin':
		error = 'Invalid username or password. Please try again !'
	else:

		# flashes on successful login
		flash('You were successfully logged in')
		return redirect(url_for('index'))
return render_template('login.html', error = error)

