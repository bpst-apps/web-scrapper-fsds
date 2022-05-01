# import required packages
from application.home import blueprint
from flask import render_template


@blueprint.route('/dashboard')
def dashboard():
    return render_template('home/index.html', title='Flask Templates', username='bhanu')
