Writing Sore Thumb filters
==========================

A Sore Thumb filter is a class derived from `sorethumb.filters.Filter`. To implement a working Filter class, you need only implement the `__call__` method which accepts a PIL image and returns an image (the same object or a new instance), or None if no changes are to be made.

Here's how the built-in ThumbnailFilter is implemented::

	class ThumbnailFilter(Filter):

	    def __init__(self, width, height):
		Filter.__init__(self, width, height)
		self.new_size = (width, height)

	    def __call__(self, img):
		img = img.thumbnail(self.new_size, Image.ANTIALIAS)
		return img

If the filter accepts parameters in the constructor, it is important to call the base Filter.__init__ with the same parameters. This is because Sore Thumb uses the parameters of the filters to create a folder that is unique for that the combination of filters and parameters used.
