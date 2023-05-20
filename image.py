from PIL import Image


class Imager:
    """A class to represent, analyze, and manipulate images."""

    def __init__(self, file):
        """Initialize image."""
        self.filename = file
        self.img = Image.open(file)
        self.width, self.height = self.analyze_image()

    def analyze_image(self):
        """Returns the width and height of an image."""
        return self.img.size[0], self.img.size[1]

    def resize_width(self, new_width, keep_ratio=True):
        """Resizes the width of an image."""
        if keep_ratio:
            new_height = int(self.height * (new_width / self.width))
        else:
            new_height = self.height

        self.resize(new_width, new_height)

    def resize_height(self, new_height, keep_ratio=True):
        """Resizes the height of an image."""
        if keep_ratio:
            new_width = int(self.width * (new_height / self.height))
        else:
            new_width = self.width

        self.resize(new_width, new_height)

    def resize(self, new_width, new_height):
        """Resizes the width and height of an image."""
        self.img = self.img.resize((new_width, new_height), Image.LANCZOS)

    def save(self, format='JPEG', quality=90, filename=None):
        """Save the image to file."""
        try:
            self.filename = filename if filename else self.filename
            self.img.save(self.filename, format, quality=quality)
        finally:
            self.close()

    def close(self):
        """Close the image file."""
        self.img.close()
