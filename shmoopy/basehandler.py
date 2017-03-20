import logging
import os
from datetime import date
import webapp2
from webapp2_extras import sessions
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):
    '''Holds auth and session properties so they are reachable for all requests'''

    def dispatch(self):
        '''Get the session store for this request'''
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            # save all sessions
            self.session_store.save_sessions(self.response)

    def handle_exception(self, exception, debug):
        logging.exception(exception)  # log an error
        page_title = 'Ohh Snapp!!'
        page_description = 'Error'
        # if an HTTP exception, show its code; otherwise, show 500
        if isinstance(exception, webapp2.HTTPException):
            if int(exception.code) == 403:
                message = 'Sorry, your request cannot be completed right now.'
            elif int(exception.code) == 404:
                message = 'Oops. There should be a page here. My bad.'
            else:
                message = 'A server error occurred'
        else:
            page_title = 'Error - 500'
            message = 'A server error occurred'
        context = {
            'page_title': page_title,
            'page_description': page_description,
            'message': message
        }
        self.render_response('public/error.html', **context)  # display the error page to the user

    @webapp2.cached_property  # the function is evaluated the first time and then just returns that first calculation for the session.
    def session(self):
        '''returns the session using the default cookie key'''
        return self.session_store.get_session()

    @webapp2.cached_property
    def messages(self):
        '''returns the messages for the session that need to be displayed to the user'''
        return self.session.get_flashes(key='_messages')

    def add_message(self, message, level=None):
        '''add a message that needs to be displayed to the user to the current session. returns nothing'''
        self.session.add_flash(message, level, key='_messages')

    @webapp2.cached_property
    def dev_server(self):
        '''return True if running on development server. return False if running live.'''
        return os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

    @webapp2.cached_property
    def jinja2(self):
        '''returns a jinja2 page renderer cached in the app registry'''
        j = jinja2.get_jinja2(app=self.app)
        j.environment.globals.update(
            {
                'uri_for': webapp2.uri_for,  # local var. use to create a link.
                # ...
            })

        def format_datetime(self, value, format='%H:%M / %d-%m-%Y'):
            '''returns formatted value'''
            return value.strftime(format)

        j.environment.filters['datetime'] = format_datetime
        return j

    def render_response(self, filename, **kwargs):
        '''apply the values provided to the template using the kwargs dictionary.'''
        if self.messages:  # if there are messages, add them to the template, so they will be displayed
            kwargs['messages'] = self.messages
        self.response.write(self.jinja2.render_template(filename, **kwargs))
