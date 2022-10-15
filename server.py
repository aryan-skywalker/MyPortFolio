from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

#on powershell
#$env:FLASK_APP = "server"
#$env:FLASK_ENV = "development"
#flask run

#@app.route('/')
# def hello_world():
#    return render_template('index.html')

#FREE HTML TEMPLATES
#https://html5up.net/

#or for more specific = user has to give a name then followed by page no to access thr website
@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/blog')
def blog():
    return render_template('about.html')


@app.route('/blog/2022/dogs')
def blog2():
    return 'Doggy!'
