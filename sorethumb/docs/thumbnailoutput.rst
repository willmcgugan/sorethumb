Thumbnail Storage
=================

Thumbnails are written to a location defined by the following scheme::

	<SORETHUMB_OUTPUT_PATH>/<thumbnail specification id>/<image path>/<image name+".thumb"+extension>

SORETHUMB_OUTPUT_PATH should be defined in Django's settings.py file. All thumbnails will be saved underneath this path.

The thumbnail specification id is a unique name derived from the filter specification, which will change if any of the filters or parameters are adjusted. The reasoning behind this is that if you tweak the thumbnail specifications, Sore Thumb will re-generate the thumbnails automatically.

The directory structure beneath the specification id will correspond to the path of the original image under the SORETHUMB_IMAGE_ROOT directory.

The filename of the thumbnail consists of the filename of the original plus the extension ".thumb" and the extension for the format declared in the specification (defaults to jpg).

To clarify the above rules, lets say your profile objects has a FileField with `upload_to` set to "uploads", and the following values in settings::

	MEDIA_ROOT = /home/will/projects/djangoapp/media
	SORETHUMB_OUTPUT_PATH = MEDIA_ROOT+'/thumbs'
	SORETHUMB_IMAGE_ROOT = MEDIA_ROOT

And the following in your template::

	{{ profile.photo|sorethumb:"rounded_corners10" }}


Then the thubnail will be saved to a location, similar to the following::

	/home/will/projects/djangoapp/media/thumbs/rounded_corners10.ffb152b0aac4234b.v1/uploads/myphoto.jpg.thumb.png

Missing Images
--------------

If the original image doesn't exist, Sore Thumb will generate a 100% magenta default image. This is because a missing image generally indicates an error and shouldn't happen on live, so it is better to make it obvious that something is wrong. If this scheme is not what you need, take a look at `get_missing_image` in `thumbnail.py`.

Pre-generating Images
---------------------

The sorethumb template filter generates the thumbnails on-the-fly, which is fine for most use-cases. The down-side of this approach is that the first time a page is rendered could potentially be expensive in terms of cpu usage, if there are many thumbnails to render. A solution would be to pre-render the thumbnails when the image is first uploaded; either in the view or a signal hander.

Here's how to render a thumbnail directly in Python code::

    DjangoThumbnail.render("rounded_corners10", profile.photo)

Generally though, this won't be neccesary. The Python Image Library is pretty fast and the first cpu-hit will be barely noticable.

