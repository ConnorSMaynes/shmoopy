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
        webapp2.Route(r'/', handler=public_handlers.HomeHandler, name='home'),
        webapp2.Route(r'/contact', handler=public_handlers.ContactHandler, name='contact'),
        webapp2.Route(r'/contact/submit', handler=public_handlers.ContactSubmitHandler, name='contact_submit'),
        webapp2.Route(r'/twitter/bot', handler=public_handlers.TwitterHandler, name='twitter_bot'),
        webapp2.Route(r'/twitter/oauth', handler=public_handlers.TwitterOauthHandler, name='twitter_oauth')
    ],
    config=webapp2_config, debug=True)
