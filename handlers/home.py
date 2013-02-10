from . import BaseHandler


class HomeHandler(BaseHandler):
    """
    Home page.
    """
    template_name = 'home.html'

    def post(self):
        context = self.get_context_data()
        image = self.request.files.get('image', [None])[0]

        if image is None:
            context['messages'].append(
                self.add_message(
                    self._("Image field is required."), 'error'))

        return self.render(self.template_name, **context)
