from . import BaseHandler
from utils.image import Image


class HomeHandler(BaseHandler):
    """
    Home page.
    """
    template_name = 'home.html'

    def get_context_data(self):
        context = super(HomeHandler, self).get_context_data()
        context.update({'palette': None})

        return context

    def post(self):
        context = self.get_context_data()
        image = self.request.files.get('image', [None])[0]

        # form validation
        if image is None:
            message = self.add_message(
                self._("Image field is required."), 'error')
        elif not image.content_type.startswith('image/'):
            message = self.add_message(
                self._("File should be image format."), 'error')
        else:
            message = self.add_message(
                self._("Your color palette is ready."), 'success')

        # add flash notification message to context
        context['messages'].append(message)

        if message['type'] == 'success':
            image = Image(image)

            context.update()
            context.update({
                'palette': image.get_palette(),
                'image_data': image.get_image_data()
            })
            context['palette'] = image.get_palette()

        return self.render(self.template_name, **context)
