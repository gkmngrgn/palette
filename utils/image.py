import operator
import colorific
from PIL import Image as Im

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class Image(object):
    def __init__(self, image):
        self.image = image

    def get_image_data(self):
        image_data = 'data:%s;base64,%s' % (
            self.image.content_type, self.image.body.encode('base64'))

        return image_data

    def get_palette(self):
        image = Im.open(StringIO(self.image.body))
        palette = colorific.extract_colors(image)
        palette_dict = {}
        for color in palette.colors:
            color_hex = colorific.rgb_to_hex(color.value)
            palette_dict[color_hex] = color.prominence

        colors = sorted(
            palette_dict.iteritems(), key=operator.itemgetter(1),
            reverse=True)
        return colors
