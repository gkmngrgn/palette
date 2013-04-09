import operator

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    import Image as MagickImage
except ImportError:
    from PIL import Image as MagickImage


class Image(object):
    def __init__(self, image):
        self.image = image

    def get_image_data(self):
        image_data = 'data:%s;base64,%s' % (
            self.image.content_type, self.image.body.encode('base64'))

        return image_data

    def get_palette(self):
        image = MagickImage.open(StringIO(self.image.body))
        width, height = image.size
        pixels = image.load()
        palette = {}

        for w in range(width):
            for h in range(height):
                pixel = '#%02x%02x%02x' % pixels[w, h]
                palette.update({pixel: palette.get(pixel, 0) + 1})

        sorted_palette = sorted(
            palette.iteritems(), key=operator.itemgetter(1), reverse=True)
        palette = filter(lambda x: x[1] > 10, sorted_palette)

        return palette
