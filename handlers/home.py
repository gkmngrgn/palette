from . import BaseHandler


class HomeHandler(BaseHandler):
    """
    Home page.
    """
    def get(self):
        return self.render('home.html')
