import webapp2
import hashlib
from google.appengine.ext import db
import datetime


LOG_IN_HTML = """\
<html>
	<head>
		<title>Login</title>
	</head>
	<body>
	    <p id="name">Welcome to the Site</p>
		<form action="/loginSubmitX" method="get">
      			Email/ Username:<br>
      			<div><textarea name="username" rows="1" cols="15"></textarea></div>
      			Password:<br>
      			<div><textarea name="password" rows="1" cols="15"></textarea></div>
      			<div><input type="submit" value="SUBMIT"></div>
    		</form>
    		<form action="/createAccountX" method="post">
      			Don't Have an Account? Create One!
      			<div><input type="submit" value="Add Account"></div>
    		</form>
	</body>
</html>
"""


LOG_IN_SUCCES_HTML = """\
<html>
	<head>
		<title>Sucess</title>
	</head>
	<body>
	    <p id="name">Log in Successful</p>
	    Continue to the Site
		<form action="/welcomeX" method="get">
      			<div><input type="submit" value="CONTINUE"></div>
        </form>
	</body>
</html>
"""


CREATE_ACCOUNT_HTML = """\
<html>
	<head>
		<title>LoginTab</title>
	</head>
	<body>
	    <p id="name">MyTitle</p>
		<form action="/accountSuccessX" method="get">
		        First Name:
		        <div><textarea name="first" rows="1" cols="15"></textarea></div>
		        Last Name:
		        <div><textarea name="last" rows="1" cols="15"></textarea></div>
		        Email:
		        <div><textarea name="email" rows="1" cols="15"></textarea></div>
      			Username:
      			<div><textarea name="user" rows="1" cols="15"></textarea></div>
      			Password:
      			<div><textarea name="pass" rows="1" cols="15"></textarea></div>
      			<div><input type="submit" value="SUBMIT"></div>
    		</form>
	</body>
</html>
"""


ACCOUNT_CREATED_HTML = """\
<html>
	<head>
		<title>Success</title>
	</head>
	<body>
	    <p id="name">Account Created</p>
		<form action="/X" method="get">
      			<div><input type="submit" value="Continue"></div>
    		</form>
	</body>
</html>
"""

TO_SITE_HTML = """\
    <html>
	<head>
		<title>WElcom</title>
	</head>
	<body>
	    <p id="name">welcome Welcome</p>
	</body>
</html>
"""


def myHash(str):
    str = hashlib.md5(str)
    str = str.hexdigest()
    return str

def myScribble(str):
    new_strs = []
    for letter in str:
        x = ord(letter)
        x = x + 3
        new_strs.append(chr(x))
    return "qa1zwsxedc7rfvtgbyh3nujmiko8lp" + "".join(new_strs)

def unScribble(str):
    str = str.split("qa1zwsxedc7rfvtgbyh3nujmiko8lp")
    str = str[1]
    new_strs = []
    for letter in str:
        x = ord(letter)
        x = x - 3
        new_strs.append(chr(x))
    return "".join(new_strs)


class myUsers(db.Model):
    my_name_first = db.StringProperty()
    my_name_last = db.StringProperty()
    my_user_email = db.StringProperty()
    user_name = db.StringProperty()
    pass_word = db.StringProperty()
    date_created = db.StringProperty()

class accountCreate(webapp2.RedirectHandler):
    def post(self):
        self.response.write(CREATE_ACCOUNT_HTML)

class accountHandler(webapp2.RedirectHandler):
    def get(self):
        first = self.request.get('first')
        last = self.request.get('last')
        email = self.request.get('email')
        username = self.request.get('user')
        password = self.request.get('pass')

        password = myHash(password)
        username = myScribble(username)
        email = myScribble(email)
        first = myScribble(first)
        last = myScribble(last)

        v = myUsers.all()
        exists = 0
        v.filter('user_name =', username)
        for self.each in v:
            exists += 1
            self.response.write('<p> %s  %s  ..   %s -   %s - -  %s  - - - %s</p>' % (self.each.my_name_first, self.each.my_name_last,  self.each.user_name,self.each.my_user_email, self.each.pass_word, self.each.date_created))
        if exists == 0:
            if first != "" and last != "" and email != "" and username != "" and password != "":
                self.my_temp = myUsers(my_name_first=first, my_name_last=last, my_user_email = email,user_name = username, pass_word= password,  date_created =str(datetime.datetime.now()))
                self.my_temp.put()
                self.response.write(ACCOUNT_CREATED_HTML)
            else:
                self.response.write("Something was left empty!!!!")
                self.response.write(CREATE_ACCOUNT_HTML)
        else:
            self.response.write("Username already Exists")
            self.response.write(CREATE_ACCOUNT_HTML)

class logInCheck(webapp2.RequestHandler):
    def get(self):
        entered_user_name = self.request.get('username')
        entered_pass_word = self.request.get('password')
        entered_user_name = myScribble(entered_user_name)
        entered_pass_word = myHash(entered_pass_word)
        v = myUsers.all()
        v.filter('user_name =', entered_user_name)
        z = myUsers.all()
        z.filter('pass_word =', entered_pass_word)

        if not v.get() or not z.get():
            self.response.write("Error: Invalid username or password!")
            self.response.write('<br><br> Invalid entry for: ')
            self.response.write(entered_user_name)
            self.response.write('<br><br>')
            self.response.write(LOG_IN_HTML)
            self.response.write('<br><br>')
            return
        else:
            self.response.write(LOG_IN_SUCCES_HTML)
            self.query2 = v
            for self.each in self.query2:
                self.response.write('<p> %s  %s  ..   %s -   %s - -   - Member Since: - - %s</p>' % (unScribble(self.each.my_name_first), unScribble(self.each.my_name_last),  unScribble(self.each.user_name),unScribble(self.each.my_user_email), self.each.date_created))


class entry(webapp2.RequestHandler):
    def get(self):
        self.response.write(TO_SITE_HTML)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(LOG_IN_HTML)
        #self.query2 = myUsers.all()
        #for self.each in self.query2:
            #self.response.write('<p> %s  %s  ..   %s -   %s - -  %s  - - - %s</p>' % (self.each.my_name_first, self.each.my_name_last,  self.each.user_name,self.each.my_user_email, self.each.pass_word, self.each.date_created))

app = webapp2.WSGIApplication([
    ('/X', MainHandler),
    ('/createAccountX',accountCreate),
    ('/loginSubmitX',logInCheck),
    ('/accountSuccessX', accountHandler),
    ('/welcomeX',entry ),
    ('/continueX',logInCheck)
], debug=True)
