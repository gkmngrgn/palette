from fabric.api import local


def test():
    """
    Runs tornado unit tests.
    """

    local('python -m tornado.test.runtests tests')


def server(port=None):
    """
    Runs tornado web server.

    Arguments:
    - `port`: server port, default value is defined in settings.py
    """
    command = 'python app.py'

    if port is not None:
        command += ' --port=%s' % port

    local(command)
