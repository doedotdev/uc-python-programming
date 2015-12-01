import cgi
from google.appengine.api import users
import webapp2
import datetime
from google.appengine.ext import db
import os
import jinja2
import urllib




template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

template = jinja_env.get_template('index.html')



MAIN_PAGE_HTML = """\
<html>

<style>
div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Welcome to Blogic</h4>
		<div id="forms">
		<form action="/submit" method="get">
      			Email/ Username:<br>
      			<div><textarea name="username" rows="1" cols="15"></textarea></div>
      			Password:<br>
      			<div><textarea name="password" rows="1" cols="15"></textarea></div>
      			<div><input type="submit" value="SUBMIT"></div>
    		</form>
    		<form action="/createAccount" method="post">
      			Don't Have an Account? Create One!
      			<div><input type="submit" value="Add Account"></div>
    		</form>
    		<form action="/X" method="get">
      			Don't Have an Account? Create One!
      			<div><input type="submit" value="GO"></div>
    		</form>
		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""

ADD_ACCOUNT_HTML = """\
<html>
<style>


div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Account Registration</h4>
		<div id="forms">



 		<form action="/added" method="post">
     			Email/ Username:<br>
      			<div><textarea name="user_name" rows="1" cols="15"></textarea></div>
      		Password:<br>
      		<div><textarea name="pass_word" rows="1" cols="15"></textarea></div>
      		<div><input type="submit" value="Create Account"></div>
    		</form>
   		 <form action="/" method="get">
     		 <div><input type="submit" value="Back to Login Account"></div>
   		 </form>


		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""

ADD_POST_HTML = """\
<html>
<style>


div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
	font-size: 32px
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 600px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 600px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}

</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>New Post</h4>
		<div id="forms">

    <form action="/reSubmit" method="post">
      Title:<br>
      <div><textarea name="title" rows="1" cols="15"></textarea></div>
      Bodyt:<br>
      <div><textarea name="body" rows="15" cols="50"></textarea></div>
      <div><input type="submit" value="SUBMIT"></div>
      <br>
    </form>
     <form action="/viewAll" method="post">
      Done Posting?
      <br>
      <div><input type="submit" value="View All Posts"></div>
    </form>


		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""

VIEW_ALL_POST_HTML = """\
<html>
<style>


div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
	font-size: 32px
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 600px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 600px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>All Posts</h4>
		<div id="forms">

    <form action="/backToSub" method="post">
      <div><input type="submit" value="Create New Post"></div>
    </form>
   <table id="myTable">
        <thead>
            <tr>
                <th>My Header</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>aaaaa</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td>My footer</td>
            </tr>
        <tfoot>
    </table>


    <form action="/backToSub" method="post">
      <div><input type="submit" value="Create New Post"></div>
    </form>
		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""

#DONE
LOG_IN_VERIFIED = """\
<!DOCTYPE html>
<html>
<style>
div {
	border-radius: 5px;
}
#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}
#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}

</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>You Are In!</h4>
		<div id="forms">



 	       <form action="/continue" method="post">
     			 <div><input type="submit" value="Continue to Site"></div>
    		</form>


		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""


class postDataBase123(db.Model):
    title = db.StringProperty()
    body = db.TextProperty()
    date = db.StringProperty()

class userDataBase(db.Model):
    user_name = db.StringProperty()
    pass_word = db.StringProperty()


class continueOn(webapp2.RequestHandler):
    def get(self):
        entered_user_name = cgi.escape(self.request.get('username'))
        entered_pass_word = cgi.escape(self.request.get('password'))
        #self.response.write(entered_user_name)
        #self.response.write(entered_pass_word)
        v = userDataBase.all()
        v.filter('user_name =', entered_user_name)
        z = userDataBase.all()
        z.filter('pass_word =', entered_pass_word)

        if not v.get() or not z.get():
            self.response.write("Error: Invalid username or password!")
            self.response.write('<br><br> Invalid entry for: ')
            self.response.write(entered_user_name)
            self.response.write('<br><br>')
            self.response.write(MAIN_PAGE_HTML)
            self.response.write('<br><br>')
            return
        self.response.write(LOG_IN_VERIFIED)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        self.query = postDataBase123.all()
        db.delete(self.query)

        self.response.write(MAIN_PAGE_HTML)
        #template = jinja_env.get_template('index.html')
        #self.response.out.write(template.render())

        self.query2 = userDataBase.all()

        #for self.each in self.query2:
           # self.response.write('<p> %s  %s</p>' % (self.each.user_name, self.each.pass_word))


class enterNewPost(webapp2.RequestHandler):
    def post(self):
        #self.response.write('<html><body>Logged in as:<pre>')
        #self.response.write(cgi.escape(self.request.get('username')))
        #self.response.write('<br><br><br>')

        self.response.write('</pre></body></html>')
        title_text = self.request.get('title')
        title_text = str(title_text)

        body_text = self.request.get('body')
        body_text = str(body_text)
        if title_text != "" and body_text != "":
            self.temp_title = postDataBase123(title=title_text, body=body_text, date=str(datetime.datetime.now()))
            self.temp_title.put()
        self.response.write(ADD_POST_HTML)


class createAccount(webapp2.RequestHandler):
    def post(self):
        title_text = self.request.get('user_name')
        title_text = str(title_text)

        body_text = self.request.get('pass_word')
        body_text = str(body_text)
        if title_text != "" and body_text != "":
            self.temp_title = userDataBase(user_name = title_text, pass_word = body_text)
            self.temp_title.put()
        self.response.write(ADD_ACCOUNT_HTML)


PRACTICE = """\
<html>
<style>


div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
	font-size: 32px
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 600px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 600px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>All Posts</h4>
		<div id="forms">

    <form action="/backToSub" method="post">
      <div><input type="submit" value="Create New Post"></div>
    </form>



"""

PRACTICE2 = """\

    <form action="/backToSub" method="post">
      <div><input type="submit" value="Create New Post"></div>
    </form>
		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""

class viewAllPosts(webapp2.RequestHandler):
    def post(self):
        self.response.out.write(PRACTICE)
        #self.response.write('<html><body>Logged in as:<pre>')
        #self.response.write(cgi.escape(self.request.get('username')))
        self.response.write('</pre></body></html>')
        #self.response.write(VIEW_ALL_POST_HTML)
        self.query = postDataBase123.all()
        #htmlcode = HTML.table

        self.response.write('<html><head><title>Table Time</title></head>'
                            '<body>'
                            '<table style="border-collapse:collapse;">'
                            '<thead><tr><th colspan="3"; style = "color: red">'
                            'Blogic All Posts</th>'
                            '</tr>'
                            '<tr style="border-bottom:1px solid black;">'
                            '<th style="padding:5px;"><em>Post Title</em></th>'
                            '<th style="padding:5px;border-left:3px solid black;"><em>Date</em></th>'
                            '<th style="padding:5px;border-left:3px solid black;"><em>Contents</em></th>'
                            '</tr></thead><tbody>')
        my_int = 0
        for self.each in self.query:
            my_home = '<a href="'
            my_home2 = '/viewPost'
            my_home3 = '">'
            parameters = urllib.urlencode({'title':self.each.title, 'date':self.each.date, 'body':self.each.body})
            self.response.write(' <tr><td style="padding:5px;border-left:3px solid black;">')
            self.response.write(my_home+my_home2+'?'+parameters+ my_home3)
            self.response.write(self.each.title)
            self.response.write('</td><td style="padding:5px;border-left:3px solid black;">')
            self.response.write(self.each.date)
            self.response.write('</td>')
            self.response.write('<td style="padding:5px;border-left:3px solid black;">')
            self.response.write(self.each.body)
            self.response.write('</td></tr>')
            my_int += 1

        self.response.write('</tbody></table></body></html>')
        self.response.write(PRACTICE2)



#############################################################################################

import webapp2
import hashlib
from google.appengine.ext import db
import datetime


LOG_IN_HTML_NEW = """\
<html>

<style>
div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;

	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Welcome to Blogic</h4>
		<div id="forms">
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
		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""


LOG_IN_SUCCES_HTML_NEW = """\
<html>

<style>
div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Continue to Site</h4>
		<div id="forms">
			<form action="/welcomeX" method="get">
      			<div><input type="submit" value="CONTINUE"></div>
        		</form>


		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""


CREATE_ACCOUNT_HTML_NEW = """\
<html>

<style>
div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Create Account</h4>
		<div id="forms">
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


		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""


ACCOUNT_CREATED_HTML_NEW = """\
<html>

<style>
div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title>Account Created</title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Account Created!</h4>
		<div id="forms">
		<form action="/" method="get">
      			<div><input type="submit" value="Continue"></div>
    		</form>



		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""

TO_SITE_HTML_NEW = """\
    <html>
	<head>
		<title>WElcom</title>
	</head>
	<body>
	    <p id="name">welcome Welcome</p>
	</body>
</html>
"""

VIEW_ONE_POST_HTML = """\
    <html>
	<head>
		<title>WElcom</title>
	</head>
	<body>
	    <p id="name">welcome Welcome</p>
	</body>
</html>
"""

#######

PRACTICE3 = """\
<html>
<style>


div {
	border-radius: 5px;
}

#header {
	z-index: 1;
	position: fixed;
	width: 97.5%;
	margin-top: -20px;
	height: 60px;
	background-color: #668284;
	margin-bottom: 10px;
}

#name {
	float:left;
	margin-left: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

#email{
	float:right;
	margin-right: 5px;
	padding-top: 5px;
	font-size: 16px;
	font-family: Verdana, sans-serif;
	color: #ffffff;
}

h4 {
	margin-left: 5px;
	margin-bottom: 15px;
	font-family: Verdana, sans-serif;
	font-size: 32px
}

.right p {
	margin-left: 5px;
	margin-right: 5px;
	margin-top: -10px;
	font-family: Garamond, serif;
	color: #000000;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: relative;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 600px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 600px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
}

#footer {
	position: relative;
	height: 50px;
	background-color: #668284;
	clear: both;
	font-family: Verdana, sans-serif;
	font-size: 14px;
	text-align: center;
	color: #ffffff;
}

#footer p {
	position: relative;
	padding-top: 15px;
}



</style>
	<head>
		<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
		<title></title>
	</head>
	<body>
		<div id="header">
			<p id="name">Blogic</p>
			<a href="mailto:bendoe31@gmail.com"><p id="email">bendoe31@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>View Post</h4>
		<div id="forms">

    <form action="/backToSub" method="post">
      <div><input type="submit" value="Create New Post"></div>
    </form>



"""

PRACTICE4 = """\
    <br>
    <br>
    <br>
    <form action="/backToSub" method="post">
      <div><input type="submit" value="Create New Post"></div>
    </form>
		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""
#######


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

class accountCreateSecure(webapp2.RedirectHandler):
    def post(self):
        self.response.write(CREATE_ACCOUNT_HTML_NEW)

class accountHandlerSecure(webapp2.RedirectHandler):
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
                self.response.write(ACCOUNT_CREATED_HTML_NEW)
            else:
                self.response.write("Something was left empty!!!!")
                self.response.write(CREATE_ACCOUNT_HTML_NEW)
        else:
            self.response.write("Username already Exists")
            self.response.write(CREATE_ACCOUNT_HTML_NEW)

class logInCheckSecure(webapp2.RequestHandler):
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
            self.response.write(LOG_IN_HTML_NEW)
            self.response.write('<br><br>')
            return
        else:
            self.response.write(LOG_IN_SUCCES_HTML_NEW)
            self.query2 = v
            for self.each in self.query2:
                self.response.write('<p> %s  %s  ..   %s -   %s - -   - Member Since: - - %s</p>' % (unScribble(self.each.my_name_first), unScribble(self.each.my_name_last),  unScribble(self.each.user_name),unScribble(self.each.my_user_email), self.each.date_created))


class entrySecure(webapp2.RequestHandler):
    def get(self):
        self.response.write(LOG_IN_VERIFIED)

class MainHandlerSecure(webapp2.RequestHandler):
    def get(self):
        self.response.write(LOG_IN_HTML_NEW)
        #self.query2 = myUsers.all()
        #for self.each in self.query2:
            #self.response.write('<p> %s  %s  ..   %s -   %s - -  %s  - - - %s</p>' % (self.each.my_name_first, self.each.my_name_last,  self.each.user_name,self.each.my_user_email, self.each.pass_word, self.each.date_created))


class viewOnePost(webapp2.RequestHandler):
    def get(self):
        self.response.write(PRACTICE3)
        self.response.write(self.request.GET.get('title'))
        self.response.write('<br><br>')
        self.response.write(self.request.GET.get('date'))
        self.response.write('<br><br>')
        self.response.write(self.request.GET.get('body'))
        self.response.write(PRACTICE4)


'''
app = webapp2.WSGIApplication([
    ('/X', MainHandlerSecure),
    ('/createAccountX',accountCreateSecure),
    ('/loginSubmitX',logInCheckSecure),
    ('/accountSuccessX', accountHandlerSecure),
    ('/welcomeX',entrySecure ),
    ('/continueX',logInCheckSecure)
], debug=True)
'''
##############################################################################################


app = webapp2.WSGIApplication([
    #('/', MainPage),
    ('/submit', continueOn),
    ('/reSubmit', enterNewPost),
    ('/continue', enterNewPost),
    ('/createAccount', createAccount),
    ('/viewAll', viewAllPosts),
    ('/added', createAccount),
    ('/backToSub', enterNewPost),
    ('/', MainHandlerSecure),
    ('/createAccountX',accountCreateSecure),
    ('/loginSubmitX',logInCheckSecure),
    ('/accountSuccessX', accountHandlerSecure),
    ('/welcomeX',entrySecure ),
    ('/continueX',logInCheckSecure),
    ('/viewPost',viewOnePost)
], debug=True)