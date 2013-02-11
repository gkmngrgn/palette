try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from wand.image import Image as WandImage


class Image(object):
    def __init__(self, image):
        self.image = image

    def get_image_data(self):
        image_data = 'data:%s;base64,%s' % (
            self.image.content_type, self.image.body.encode('base64'))

        return image_data

    def get_palette(self):
        image = StringIO(self.image.body)
        palette = {}

        with WandImage(file=image) as img:
            img.trim()
            img.resize(width=100, height=100, filter='box')

            for row in img:
                for col in row:
                    palette.update({
                        col.string: palette.get(col.string, 0) + 1
                    })

        palette = palette.keys()
        return palette
