
import webapp2
import os
import jinja2
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)



class MainHandler(webapp2.RequestHandler):
    def get(self):
            template_values = {'name': 'SomeGuy', 'verb': 'extremely enjoy'}
            template = jinja_env.get_template('index.html')
            self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
