import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """
    It has some custom method for the project.
    """
    def get_current_user(self):
        """
        Returns current user for the session.
        """
        # TODO: please fill this method after integrated mongodb database.
        return
