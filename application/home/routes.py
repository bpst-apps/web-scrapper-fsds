# import required packages
from application.home import blueprint


@blueprint.route('/')
def index():
    return 'welcome to actual home'
