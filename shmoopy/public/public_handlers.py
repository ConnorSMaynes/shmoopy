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

