import webapp2
from webapp2_extras import routes
import os

from shmoopy.public import public_handlers

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')  # when public, should return False

webapp2_config = {}  # empty configuration dictionary
webapp2_config['webapp2_extras.sessions'] = {  # used to create session cookies
    'secret_key': 'Zjkejk2490unkn2JII0'
}

app = webapp2.WSGIApplication(
    [
        webapp2.Route(r'/twitter', handler=public_handlers.TwitterHandler, name='twitter_bot')
    ],
    config=webapp2_config, debug=True)
