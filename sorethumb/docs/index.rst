.. Sore Thumb documentation master file, created by
   sphinx-quickstart on Mon Jun 14 11:02:15 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Sore Thumb's documentation!
======================================

Sore Thumb is a Python module to process images in to thumbnails, and apply effects that may be difficult or impossible to do in the browser. Sore Thumb comes with Django intergration, but may be used with other web frameworks or in a stand-alone fashion.

About Sore Thumb
================

Sore Thumb was originally written for http://2degreesnetwork.com, and has been used in production for some months before it was open sourced. It was written by Will McGugan and Euan Goddard, and is maintained by Will McGugan (http://www.willmcgugan.com/). Sore Thumb is copyright 2010 2Degrees Limited, and is released under the BSD License.

Introduction
============

Thumbnails are declared in Sore Thumb with a thumbnail specification class which defines the filters that should be applied to the original image, and some other pieces of information to control the thumbnail output.

Here's an example of a thumbnail declaration that produces a 120x100 pixel thumbnail with curved corners and a gray edge::

    from sorethumb.djangothumbnail import DjangoThumbnail
    from sorethumb.filters.defaultfilters import ThumbnailFilter
    from sorethumb.filters.drawfilters import RoundedCornerFilter

    class RoundedCornersEdged(DjangoThumbnail):    
        format = 'png'
        filters = [ThumbnailFilter(120, 100),
                   RoundedCornerFilter(10, border='#333')] 

Once the above code has been imported the `RoundedCornersEdged` thumbnail specification becomes available to Django templates. After loading the `sorethumb` templatetag library, you can use the `sorethumb` filter which when applied to an `image_field` will return the url to the thumbnail. For example, let's say we have a profile object in the template context containing an image field called `photo`. To display the small rounded corners version, we can apply the sorethumb filter::

    {% load sorethumb %}
    
    <img src="{{ profile.photo|sorethumb:"rounded_corners_edged" }} />

The thumbnail will be generated the first time this template is rendered.


Guide:

.. toctree::
   :maxdepth: 3
   
   djangointegration.rst
   thumbnailspec.rst
   sorethumbsettings.rst
   writingfilters.rst
   thumbnailoutput.rst
   

Further Information
-------------------

For further information on Sore Thumb, see http://www.willmcgugan.com/tag/sorethumb/

   
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

