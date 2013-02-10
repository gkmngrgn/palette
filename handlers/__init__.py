import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """
    It has some custom method for the project.
    """
    template_name = None

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

        # for translatable strings
        self._ = self.locale.translate

    def add_message(self, msg, msg_type='info'):
        """
        Adds flash notification message to context.
        """
        return {'content': msg, 'type': msg_type}

    def get(self):
        context = self.get_context_data()
        return self.render(self.template_name, **context)

    def get_context_data(self):
        return {'messages': []}

    def post(self):
        return super(BaseHandler, self).get()
