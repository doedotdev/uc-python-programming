import os
import webapp2
import jinja2
import urlparse
import re
import collections
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
			<p id="name">Data Cleaner</p>
			<a href="mailto:hornbd3196@gmail.com"><p id="email">hornbd9631@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Welcome to Data Cleaner</h4>
		<div id="forms">

		<form action="/submit" method="get">
		        <input type="checkbox" name="duplicate" value="1">Remove Duplicates<br>
        <input type="checkbox" name="special" value="1">Remove Special Characters<br>
        <input type="checkbox" name="letters" value="1">Remove everything but letters<br>
        <input type="checkbox" name="numbers" value="1">Remove everything but numbers<br>
        <input type="checkbox" name="lower" value="1">Change All to lowercase<br>
        <input type="checkbox" name="show_analytics" value="1">SHOW DATA ANALYTICS<br>
      			Text:<br>
      			<div><textarea name="text_to_clean" rows="10" cols="=50"></textarea></div>
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

PAGE_HTML_1 = """\
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
	margin-left: 20px;
	margin-right: 20px;
	margin-top: -10px;
	font-family: Garamond, serif;
	height:100vh;
	color: #000000;
	overflow: scroll;
}

li {
	list-style-type: square;
}

a:hover {
	font-weight: bold;
}

.left {
	position: absolute;
	float: left;
	margin-top: 50px;
	width: 10%;
	height: 400px;
	background-color: #B9D7D9;
	margin-bottom: 10px;
		height:100vh;
}

.right {
	position: relative;
	float: right;
	margin-top: 50px;
	width: 88%;
	height: 400px;
	background-color: #F4EBC3;
	margin-bottom: 10px;
		height:100%;
		overflow: scroll;
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
	bottom: 0;
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
			<p id="name">Data Cleaner</p>
			<a href="mailto:hornbd3196@gmail.com"><p id="email">hornbd9631@gmail.com</p></a>
		</div>
		<div class="left"></div>
		<div class="right">
			<h4>Welcome to Data Cleaner</h4>
		<div id="forms">

		<form action="/submit" method="get">
		        <input type="checkbox" name="duplicate" value="1">Remove Duplicates<br>
        <input type="checkbox" name="special" value="1">Remove Special Characters<br>
        <input type="checkbox" name="letters" value="1">Remove everything but letters<br>
        <input type="checkbox" name="numbers" value="1">Remove everything but numbers<br>
        <input type="checkbox" name="lower" value="1">Change All to lowercase<br>
        <input type="checkbox" name="show_analytics" value="1">SHOW DATA ANALYTICS<br>

      			Text:<br>
      			<div><textarea name="text_to_clean" rows="10" cols="=50"></textarea></div>
      			<div><input type="submit" value="SUBMIT"></div>
    		</form>
    	<h4> Original Data </h4>
"""
PAGE_HTML_2 = """\
        <h4> Cleaned Data </h4>
		"""
PAGE_HTML_3 = """\
		</div>
		</div>
		<div id="footer">
			<p>Benjamin Horn, University of Cincinnati, OH | Computer Science</p>
		</div>
	</body>
</html>
"""
##############################################
def removeDuplicates(str):
    str = str.split()
    str = list(set(str))
    ret = ""
    for each in str:
        ret += each +' '
    return ret

def toLower(str):
    return str.lower()

def removeSpecChar(str):
    return re.sub('[^0-9a-zA-Z]+', ' ', str)

def removeNonLetters(str):
    return re.sub('[^a-zA-Z]+', ' ', str)

def removeNonNumbers(str):
    return re.sub('[^0-9]+', ' ', str)

def getData(str):
    master_list = collections.namedtuple('Data', 'Occurrences Value')
    d = {} # instantiating a empty list; Doesn't do anything
    str = str.split()
    for each in str:
        if each != '':
            if each in d:
                d[each]+=1
            else:
                d[each] = 1
    ordered_master_list = sorted([master_list(v,k) for (k,v) in d.items()], reverse=True)
    print('\n\n')
    print('Words + Occurrences')
    self.response.write('<br><br>Words + Occurrences')
    for k, v in ordered_master_list:
        print "%s : %i." % (v, k)

################################################
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class showText(webapp2.RequestHandler):
    def get(self):
        self.response.write(PAGE_HTML_1)
        words = self.request.get('text_to_clean')
        self.response.write(words)
        self.response.write('<br><br>')
        total_words_1 = 0
        if self.request.get('show_analytics') == '1':
            str = words
            master_list = collections.namedtuple('Data', 'Occurrences Value')
            d = {} # instantiating a empty list; Doesn't do anything
            str = str.split()
            for each in str:
                total_words_1 += 1
                if each != '':
                    if each in d:
                        d[each]+=1
                    else:
                        d[each] = 1
            ordered_master_list = sorted([master_list(v,k) for (k,v) in d.items()], reverse=True)
            self.response.write('<br><br>Words + Occurrences<br>')
            for k, v in ordered_master_list:
                self.response.write(v)
                self.response.write(' : ')
                self.response.write(k)
                self.response.write('<br>')
                print "%s : %i." % (v, k)
        self.response.write('<h4>Total Words: ')
        self.response.write(total_words_1)
        self.response.write('</h4><br><br>')
        self.response.write(PAGE_HTML_2)
        #######################
        if self.request.get('lower') == '1':
            words = toLower(words)
        if self.request.get('special') == '1':
            words = removeSpecChar(words)
        if self.request.get('letters') == '1':
            words = removeNonLetters(words)
        if self.request.get('numbers') == '1':
            words = removeNonNumbers(words)
        if self.request.get('duplicate') == '1':
            words = removeDuplicates(words)


        #######################
        self.response.write(words)
        total_words_2 = 0
        if self.request.get('show_analytics') == '1':
            str = words
            master_list = collections.namedtuple('Data', 'Occurrences Value')
            d = {} # instantiating a empty list; Doesn't do anything
            str = str.split()
            for each in str:
                total_words_2 += 1
                if each != '':
                    if each in d:
                        d[each]+=1
                    else:
                        d[each] = 1
            ordered_master_list = sorted([master_list(v,k) for (k,v) in d.items()], reverse=True)
            self.response.write('<br><br>Words + Occurrences<br>')
            for k, v in ordered_master_list:
                self.response.write(v)
                self.response.write(' : ')
                self.response.write(k)
                self.response.write('<br>')
                print "%s : %i." % (v, k)
        self.response.write('<h4>Total Words: ')
        self.response.write(total_words_2)
        self.response.write('</h4><br><br>')
        self.response.write(PAGE_HTML_3)


app = webapp2.WSGIApplication([('/', MainPage),
                                   ('/submit', showText)], debug=True)