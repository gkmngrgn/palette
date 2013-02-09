import os.path

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))

settings = dict(
    template_path=os.path.join(PROJECT_DIR, 'templates'),
    static_path=os.path.join(PROJECT_DIR, 'static'),
    cookie_secret='__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__'
)

# options
option_list = [
    dict(name='port', default=8000, help="run on the given port", type=int),
]
