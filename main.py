from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('homepage.html')


@app.route("/homepage", methods = ['POST'])
def validate_signup():
  username = request.form['username']
  password = request.form['password']
  verify = request.form['verify']
  email = request.form['email']

  username_error = ''
  password_error = ''
  verify_error = ''
  email_error = ''

#username
  if int(len(username)) <= 0:
    username_error = "That's not a valid username"
    username = ''
  else:
    if " " in username or int(len(username)) > 20 or int(len(username)) < 3:
      username_error = "That's not a valid username(value range 3-20), no spaces"
      username = ''
#password
  if " " in password or int(len(password)) <= 0:
    password_error = "That's not a valid password"
    password = ''
  else:
    if int(len(password)) > 20 or int(len(password)) < 3:
      password_error = "That's not a valid password(value range 3-20), no spaces"
      password = ''
#verify
  if " " in verify or int(len(verify)) <= 0:
      verify_error = 'The passwords do not match'
      verify = ''
  else:
    if password !=verify:
      verify_error = "The passwords do not match"
      verify = ''
#email
  if int(len(email)) > 0:
        if "@" not in email and "." not in email:
            email_error = "That's not a valid email"
            email = ''
        elif " " in email or int(len(email)) >20 or int(len(email)) < 3:
            email_error = "That's not a valid email"
            email = ''

  if not username_error and not password_error and not verify_error and not email_error:
    username=str(username)
    return redirect('/welcome?username={0}'.format(username))
  else:
    return render_template('homepage.html', username=username, username_error=username_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)


app.run()