from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from .models import ThumbTest

from sorethumb.filters.defaultfilters import *
from sorethumb.filters.drawfilters import *
from sorethumb.djangothumbnail import DjangoThumbnail


class SmallThumb(DjangoThumbnail):

    filters = [ThumbnailFilter(120, 100)]


class Square(DjangoThumbnail):

    filters = [ThumbnailFilter(100, 100),
              SquareFilter(),]


class RoundedCorners5(DjangoThumbnail):

    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(5)]


class RoundedCorners10(DjangoThumbnail):

    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(10)]


class RoundedCorners20(DjangoThumbnail):

    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(20)]


class RoundedCornersEdged(DjangoThumbnail):

    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(10, border='#000')]


class RoundedCornersBackground(DjangoThumbnail):

    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(10, border='#333'),
               ResizeCanvasFilter(130, 110, '#fff'),
               OpaqueFilter('#fff'),]


class RoundedCornersBackgroundGradient(DjangoThumbnail):

    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(10, border='#000'),
               ResizeCanvasFilter(130, 110, '#e2e2ff', background_opacity=0),
               VerticalGradientFilter('#fff', '#88e'),]


# class MaskThumb(DjangoThumbnail):

#     format = 'png'
#     filters = [ThumbnailFilter(120, 100),
#                ResizeCanvasFilter(120, 100, '#000', background_opacity=0),
#                MaskFilter(settings.MEDIA_ROOT+'/alpha.png')]


class GrayThumb(DjangoThumbnail):

    filters = [ThumbnailFilter(120, 100),
               GrayscaleFilter()]


class FadedThumb(DjangoThumbnail):

    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               OpacityFilter(.5)]


# class OverlayThumb(DjangoThumbnail):
#     format = 'png'
#     filters = [ThumbnailFilter(120, 100),
#                OverlayFilter(settings.MEDIA_ROOT+'/user.png')]


thumb_examples = [

    {
    'thumb':'small_thumb',
    'title':'Basic thumbnail',
    'description':"""Here we have a basic thumbnail that uses PIL's thumbnail operation to reduce an image to fit in a defined dimensions.""",

    'code' : '''class SmallThumb(DjangoThumbnail):
    filters = [ThumbnailFilter(120, 100)]'''
    },

    {
    'thumb':'square',
    'title':'Square',
    'description':'As above, but cropped to be square. Since uploaded images can be any old size, they can tend to look ragged when presented in rows. Square thumbs look better in rows, at the expense of a little cropping',

    'code':"""class Square(DjangoThumbnail):
    filters = [ThumbnailFilter(100, 100),
               SquareFilter()] """
    },

    {
    'thumb':'rounded_corners5',
    'title':'5 pixels rounded corner',
    'description':"""Rounded corners without CSS3, on a transparent background. What is it with designers and rounded corners anyway?""",
    'code':"""class RoundedCorners5(DjangoThumbnail):
    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(5)] """,

    },

    {
    'thumb':'rounded_corners10',
    'title':'10 pixels rounded corner',
    'description':'As above, but 10 pixels.',
    },

    {
    'thumb':'rounded_corners20',
    'title':'20 pixels rounded corner',
    'description':'Even more rounded corners',
    },

    {
    'thumb':'rounded_corners_edged',
    'title':'Rounded corners with a border',
    'description':'The rounded corner filter also supports a coloured border',
    'code':"""class RoundedCornersEdged(DjangoThumbnail):
    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(10, border='#333')]""",
    },

    {
     'thumb':'rounded_corners_background',
     'title':"Rounded corners on an opaque background",
     'description':"Rounded corners on an opaque backround for browsers with poor support for per-pixel transparency &mdash; IE6 I'm looking at you!",
     'code':"""class RoundedCornersBackground(DjangoThumbnail):
    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(10, border='#333'),
               ResizeCanvasFilter(130, 110, '#fff'),
               OpaqueFilter('#fff')] """
     },

    {
     'thumb':'rounded_corners_background_gradient',
     'title':"Rounded corners on a gadient",
     'description':"As above, but on a gradient background. The vertical gradient filter replaces transparent areas with a smooth gradient between two colours.",
     'code':"""class RoundedCornersBackgroundGradient(DjangoThumbnail):
    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               RoundedCornerFilter(10, border='#000'),
               ResizeCanvasFilter(130, 110, '#e2e2ff', background_opacity=0),
               VerticalGradientFilter('#fff', '#88e')]  """
     },

#      {'thumb':'mask_thumb',
#       'title':'Masked thumbnail',
#       'description': 'This thumbnail uses MaskFilter which replaces the alpha channel with another image, to create some interesting effects.',
#       'code':"""class MaskThumb(DjangoThumbnail):
#     format = 'png'
#     filters = [ThumbnailFilter(120, 100),
#                ResizeCanvasFilter(120, 100, '#000', background_opacity=0),
#                MaskFilter(settings.MEDIA_ROOT+'/alpha.png')]
# """
#       },

     {
      'thumb':'gray_thumb',
      'title':'Grayscale',
      'description':'A grayscale thumb, could be used as a hover state.',
      'code':"""class GrayThumb(DjangoThumbnail):
    filters = [ThumbnailFilter(120, 100),
               GrayscaleFilter()]"""
      },

      {
      'thumb':'faded_thumb',
      'title':'50% opacity',
      'description':'The OpacityFilter sets the opacity of the thumbnail.',
      'code':"""class FadedThumb(DjangoThumbnail):
    format = 'png'
    filters = [ThumbnailFilter(120, 100),
               OpacityFilter(.5)] """
      },


    # {
    # 'thumb':'overlay_thumb',
    # 'title':'Thumbnail with overlay',
    # 'description':"""A thumbnail with an overlayed transparent png. Could be used to indicate online status.""",

    # 'code' : '''class OverlayThumb(DjangoThumbnail):
    # format = 'png'
    # filters = [ThumbnailFilter(120, 100),
    #           OverlayFilter(settings.MEDIA_ROOT+'/user.png')]'''
    # },

]

def examples(request):

    context = {'examples':thumb_examples}

    if request.method == 'POST':
        thumb = ThumbTest(image_file=request.FILES.get('file'))
        thumb.save()

    try:
        dbobject = ThumbTest.objects.all().order_by('-pk')[0]
    except IndexError:
        dbobject = None

    context['dbobject'] = dbobject

    return render_to_response('thumbs.html',
                              context,
                              RequestContext(request))
