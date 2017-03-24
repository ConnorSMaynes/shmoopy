import webapp2
from shmoopy import basehandler


class TwitterHandler(basehandler.BaseHandler):
    def get(self):
        page_title = 'schmoopy - The Social Network Bot System'
        page_description = page_title
        context = {
                    'page_title': page_title,
                    'page_description': page_description,
                  }
        self.render_response('public/splash.html', **context)

<<<<<<< HEAD

class TwitterOauthHandler(basehandler.BaseHandler):
    def get(self):
        '''get the user's authorization from twitter to access their account.'''


class ContactHandler(basehandler.BaseHandler):
    def get(self):
        '''render the contact form'''
        page_title='contact shmoopy'
        page_description = 'contact shmoopy'

        context = {'page_title': page_title,
                   'page_description': page_description,
                   'form_contact': self.form_contact,
                   'contact_action': webapp2.uri_for('contact/submit')
                   }
        self.render_response('public/contact.html', **context)

    @webapp2.cached_property
    def form_contact(self):
        '''generate an instance of the contact form to pass to the splash page.'''
        try:
            return forms.ContactForm(self.request.POST)
        except Exception, e:  # record the error and then show error message to user
            logging.error('_shmoopy Error - HomeHandler(FORM) - %s' % str(e))
            self.abort(403)

class HomeHandler(basehandler.BaseHandler):
    '''render the home page with all necessary information.'''
    def get(self):
        '''render the splash home page'''
        page_title = 'shmoopy - The Social Networking Bot System'
        page_description = 'Create a system of bots for all popular social networks.'

        context = {'page_title': page_title,
                   'page_description': page_description,
                   }
        self.render_response('public/splash.html', **context)


=======
class HomeHandler(basehandler.BaseHandler):
    def get(self):
        page_title = 'schmoopy - The Social Network Bot System'
        page_description = page_title
        context = {
                    'page_title': page_title,
                    'page_description': page_description,
                  }
        self.render_response('public/splash.html', **context)
        
>>>>>>> origin/master
class ContactSubmitHandler(basehandler.BaseHandler):
    def post(self):
        if self.form.validate():    # check if form passes validators
            name = self.form.name.data
            email = self.form.email.data
            message = self.form.message.data

            # do something with the data

        for field, errors in self.form.errors.items():  # if validation fails, add messages
            for error in errors:
                field_name = getattr(self.form, field).label.text
                self.add_message(u'Error in the ( %s ) form field - %s' % (
                    field_name,
                    error
                ), 'error')

        self.redirect(webapp2.uri_for('home', _full=True))  # redirect back to home page

    @webapp2.cached_property
    def form(self):
        '''return the ContactForm and save in cache'''
        try:
            return forms.ContactForm(self.request.POST)
        except Exception, e:
            logging.error('schmoopy Error - ContactSubmitHandler(FORM) - %s' % str(e))
            self.abort(403)

