# import packages
from application.image import blueprint
from flask import render_template


@blueprint.route('/image-classification')
def image_classification():
    return render_template('image/image-classification.html', title='Flask Templates', bhanu='image classification 1')
