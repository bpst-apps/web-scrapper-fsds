# import packages
from application.image import blueprint


@blueprint.route('/image-classification')
def image_classification():
    return 'image classification'
