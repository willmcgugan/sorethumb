# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2010, 2degrees Limited <willmcgugan+2d@gmail.com>.
# All Rights Reserved.
#
# This file is part of sorethumb,
# which is subject to the provisions of the BSD at
# <http://dev.2degreesnetwork.com/p/2degrees-license.html>. A copy of the
# license should accompany this distribution. THIS SOFTWARE IS PROVIDED "AS IS"
# AND ANY AND ALL EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
# INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################

from PIL import Image, ImageOps
from math import ceil
from sorethumb.filters import Filter, parse_color, html_color
import hashlib


class ThumbnailFilter(Filter):

    """ Uses PIL's thumbnail method to reduce an image. """

    def __init__(self, width, height):
        """
        :param width: The maximum width of the thumbnail
        :param height: The maximum height of the thumbnail

        """
        Filter.__init__(self, width, height)
        self.new_size = (width, height)

    def __call__(self, img):
        img = img.thumbnail(self.new_size, Image.ANTIALIAS)
        return img


class ResizeFilter(Filter):

    """Resizes an image to new dimensions (may change the aspect ratio"""

    def __init__(self, width, height):
        """
        :param width: The required width of the thumbnail
        :param height: The required height of the thumbnail
        """
        Filter.__init__(self, width, height)
        self.new_size = (width, height)

    def __call__(self, img):
        return img.resize(self.new_size, Image.ANTIALIAS)


class SquareFilter(Filter):

    """Crops an image to be square (from center)"""

    def __call__(self, img):
        w, h = img.size

        if w == h:
            return img

        if w > h:
            x = (w - h) / 2
            return img.crop((x, 0, x + h, h))
        else:
            y = (h - w) / 2
            return img.crop((0, y, w, w + y))


class ResizeCanvasFilter(Filter):

    """Adjusts the canvas size and centers the image."""

    def __init__(self,
                 width,
                 height,
                 background_color='#000',
                 background_opacity=255):
        """
        :param width: Width of resized version
        :param height: Height of resized version
        :param background_color: Color for the canvas background
        :param background_opacity: Opacity for canvas background (255 is opaque)

        """
        Filter.__init__(self, width, height, background_color, background_opacity)
        self.new_size = (width, height)
        self.background_color = parse_color(background_color)
        self.background_opacity = background_opacity


    def __call__(self, img):
        r, g, b = self.background_color
        a = self.background_opacity

        new_img = Image.new('RGBA', self.new_size, (r, g, b, a))
        w, h = img.size
        nw, nh = self.new_size
        x = int((nw - w) / 2)
        y = int((nh - h) / 2)
        new_img.paste(img, (x, y))
        return new_img


class OpaqueFilter(Filter):

    """Renders an image with an alpha channel on to an opaque background"""

    def __init__(self, col):
        """
        :param col: The colour of the background as an HTML string or tuple

        """
        Filter.__init__(self, col)
        self.col = parse_color(col)

    def __call__(self, img):
        opaque = Image.new('RGBA', img.size, self.col)
        opaque.paste(img, (0, 0), img)
        opaque = opaque.convert('RGB')
        return opaque


class VerticalGradientFilter(Filter):

    """Renders a vertical gradient from colour 1 to colour 2"""

    def __init__(self, col1, col2):
        """
        :param col1: The colour at the top of the image
        :param col2: The colour at the bottom of the image

        """
        Filter.__init__(self, col1, col2)
        self.col1 = parse_color(col1)
        self.col2 = parse_color(col2)

    def __call__(self, img):
        r1, g1, b1 = map(float, self.col1)
        r2, g2, b2 = map(float, self.col2)

        gradient = Image.new('RGB', img.size)

        w, h = img.size
        fh = float(h)
        for y in range(h):
            i = (y / fh)
            r = r1 + (r2 - r1) * i
            g = g1 + (g2 - g1) * i
            b = b1 + (b2 - b1) * i
            row = Image.new('RGB', (w, 1), (int(r), int(g), int(b)))
            gradient.paste(row, (0, y))

        gradient.paste(img, (0, 0), img)
        gradient = gradient.convert('RGB')
        return gradient


class RectangularCropFilter(Filter):
    """Crops an image to the specified x/y ratio"""

    def __init__(self, ratio):
        """
        :param ratio: New aspect ratio for the image

        """
        Filter.__init__(self, ratio)
        self.ratio = ratio * 1.0

    def __call__(self, img):
        current_width, current_height = img.size

        current_ratio = float(current_width) / current_height

        # check to see whether a crop is necessary:
        if current_ratio != self.ratio:

            if current_ratio > self.ratio:
                # we've got an image which is more landscape than the
                # desired image:
                new_width = int(ceil(current_height / self.ratio))
                new_height = current_height

                new_left = (current_width - new_width) / 2
                new_right = new_left + new_width

                new_size = (int(new_left), 0, int(new_right), int(new_height))

            else:
                # we've got an image which is more portrait than the
                # desired image:
                new_width = current_width
                new_height = int(ceil(current_width / self.ratio))

                new_top = (current_height - new_height) / 2
                new_bottom = new_top + new_height

                new_size = (0, int(new_top), int(new_width), int(new_bottom))

            img = img.crop(new_size)

        return img


class FixedWidthFilter(Filter):
    """Resizes the image to the specified width respecting the aspect ratio"""

    def __init__(self, width, no_upscale=False):
        """
        :param width: New width
        :param no_upscale: If True the image will only be scaled down

        """
        Filter.__init__(self, width, no_upscale)
        self.width = int(width)
        self.no_upscale = bool(no_upscale)

    def __call__(self, img):
        orig_width, orig_height = img.size

        if self.no_upscale and orig_width <= self.width:
            return img

        orig_ratio = float(orig_width) / orig_height

        new_height = int(self.width / orig_ratio)
        img = img.resize((self.width, new_height), Image.ANTIALIAS)

        return img


class FixedHeightFilter(Filter):
    """ Resizes the image to the specified height respecting the aspect ratio """

    def __init__(self, height, no_upscale=False):
        """
        :param height: New height in pixels
        :param no_upscale: If True the image will only be scaled down

        """
        Filter.__init__(self, height, no_upscale)
        self.height = int(height)
        self.no_upscale = bool(no_upscale)

    def __call__(self, img):
        orig_width, orig_height = img.size

        if self.no_upscale and orig_height <= self.height:
            return img

        orig_ratio = float(orig_width) / orig_height
        new_width = int(self.height * orig_ratio)
        img = img.resize((new_width, self.height), Image.ANTIALIAS)

        return img


class OverlayFilter(Filter):
    """ Renders a translucent image over the image """

    def __init__(self, overlay_path):
        """
        :param overlay_path: System path to the overlay image

        """
        Filter.__init__(self, overlay_path)
        self.overlay_path = overlay_path

    def __call__(self, img):
        overlay_img = Image.open(self.overlay_path)
        img.paste(overlay_img, (0, 0), overlay_img)
        return img


class MaskFilter(Filter):
    """ Replaces the alpha channel with a new image """

    def __init__(self, mask_path):
        """
        :param mask_path: Path to mask image

        """
        Filter.__init__(self, mask_path)
        self.mask_path = mask_path

    def __call__(self, img):

        mask = Image.open(self.mask_path)
        mask = mask.convert('L')
        img.convert('RGBA')
        img.putalpha(mask)
        return img

        mask = Image.open(self.mask_path)
        img = img.convert("RGBA")
        r, g, b, a = mask.split()
        img.paste(mask, mask=mask)
        img = img.convert('RGB')
        return img


class OpacityFilter(Filter):
    """Sets the alpha channel to a given opacity"""

    def __init__(self, opacity=.5):
        """
        :param opacity: A floating point value between 0 and 1, where 0

        """
        Filter.__init__(self, opacity)
        self.opacity = opacity

    def __call__(self, img):
        opacity = max(0, min(255, int(self.opacity * 255.0)))
        img.putalpha(opacity)
        return img


class GrayscaleFilter(Filter):
    """Converts the image to grayscale"""

    def __call__(self, img):
        img = ImageOps.grayscale(img)
        return img


class InvertFilter(Filter):
    """Inverts the colours in the image"""

    def __call__(self, img):
        return ImageOps.invert(img)


