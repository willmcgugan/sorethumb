.. Sore Thumb documentation master file, created by
   sphinx-quickstart on Mon Jun 14 11:02:15 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Sore Thumb's documentation!
======================================

Sore Thumb is a Python module to process images in to thumbnails, and apply effects that may be difficult or impossible to do in the browser. Sore Thumb comes with Django intergration, but can be used with other web frameworks or in a stand-alone fashion.

Thumbnails are declared in Sore Thumb with a thumbnail specification class, which specifies which filters should be applied to the original image, and some other pieces of information to control the thumbnail output.

Here's an example of a thumbnail declaration that produces a thumbnail with curved corners and a gray edge, which will fit in to 120x100 pixels::

    from sorethumb.djangothumbnail import DjangoThumbnail
    from sorethumb.filters.defaultfilters import ThumbnailFilter
    from sorethumb.filters.drawfilters import RoundedCornerFilter

    class RoundedCornersEdged(DjangoThumbnail):    
        format = 'png'
        filters = [ThumbnailFilter(120, 100),
                   RoundedCornerFilter(10, border='#333')] 

Once the above code has been rendered the `RoundedCornersEdged` thumbnail specification becomes available in Django templates. After loading the `sorethumb` templatetag library, you can use the `sorethumb` filter which can be applied to an image_field and returns a url to the thumbnail. For example, let's say we pass a profile object containing an image field called `photo`. To retrieve the small rounded corners version, we can apply the sorethumb filter::

    {% load sorethumb %}
    
    <img src="{{ profile.photo|sorethumb:"rounded_corners_edged" }} />

Sore Thumb converts the name of the filter specification to lower case with underscores (if an explicit name attribute isn't supplied). The filter will generate the thumbnail the first time the thumbnail is rendered.



Guide:

.. toctree::
   :maxdepth: 3
   
   thumbnailspec.rst
   sorethumbsettings.rst
   writingfilters.rst
   thumbnailoutput.rst 
   
   
Code Documentation
------------------
   
.. toctree::
   :maxdepth: 3
      
   filters.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

