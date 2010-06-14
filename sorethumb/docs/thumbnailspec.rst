Thumbnail Specifications
========================

Sore Thumb uses a declarative style to specify thumbnail, similar to Django's models and forms.

To create a thumbnail specification derive a class from `DjangoThumbnail`, and supply a few parameters as class attributes.

 * **default** - A path to a default image, if the file field is None
 * **format** - The format of the derived thumbnail ('png' or 'jpg' are probably the best choices)
 * **filters** - A list of filter classes to apply to the original image
 * **name** - The name of the thumbmail specification used in templates, or the name of the class converted to lower case and underscores if `name` is not supplied
 * **quality** - An integer from 1 to 100 that will be used as the quality for jpeg thumbnails
 * **version** - The version of the specification, as an integer. Increase this to force the thumbnail to be regenerated 

Example Thumbnail Specification 
-------------------------------

Here's an example of a typical Thumbnail specification::

	from sorethumb.filters.defaultfilters import *
	from sorethumb.filters.drawfilters import *
	from sorethumb.djangothumbnail import DjangoThumbnail

	class RoundedCornersBackground(DjangoThumbnail):
	    name = 'small_profile_image'
	    format = 'png'
	    filters = [ThumbnailFilter(120, 100),
		       RoundedCornerFilter(10, border='#333'),               
		       ResizeCanvasFilter(130, 110, '#fff'),
		       OpaqueFilter('#fff')] 

To use a thumbnail specification in a template it must first be imported -- it doesn't matter where as long as it is done prior to using the thumbnail in a template. A good approach would be to put all your thumbnail specifications in a field called `thumbs.py` and import it in any of your view files the render templates with thumbnails.
