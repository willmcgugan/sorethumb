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

"""Filters which require the aggdraw module to work

"""

from PIL import Image, ImageDraw
import aggdraw

from sorethumb.filters import Filter, parse_color, html_color


class RoundedCornerFilter(Filter):

    """ Rounds the corners of an image with a given radius, and optionally
    draws a border.

    """

    def __init__(self, radius, border=None):
        """
        :param radius: The radius for the corners
        :param border: The border color as HTML string or tuple
        
        """
        
        Filter.__init__(self, radius, border)
        self.radius = radius
        self.border = parse_color(border)

    def __call__(self, img):

        w, h = img.size
        r = self.radius
        d = r * 2
                        
        circle = Image.new('L', (d, d))
        draw = aggdraw.Draw(circle)

        pen = aggdraw.Pen(255)
        brush = aggdraw.Brush(255)
        draw.ellipse((1, 1, d - 1, d - 1), pen, brush)
        draw.flush()

        # Cut it in to four pieces
        tl = circle.crop((0, 0, r, r)) # Top left
        tr = circle.crop((r, 0, d, r)) # Top right
        bl = circle.crop((0, r, r, d)) # Bottom left
        br = circle.crop((r, r, d, d)) # Bottom right

        # Create an alpha image with the four pieces at the corners
        alpha = Image.new('L', img.size, 255)
        alpha.paste(tl, (0, 0))
        alpha.paste(tr, (w - r, 0))
        alpha.paste(bl, (0, h - r))
        alpha.paste(br, (w - r, h - r))

        # Replace the alpha with our new image
        img = img.convert('RGBA')
        img.putalpha(alpha)

        if self.border is None:
            return img        

        # Draw a border with curved corners
        draw = aggdraw.Draw(img)
        pen = aggdraw.Pen(self.border)

        # The +.5s are so that agg doesn't draw over pixel boundries
        draw.arc((0.5, 0.5, d - .5, d - .5), 90, 180, pen)
        draw.line((r, .5, w - r, .5), pen)

        draw.arc((w - d + .5, 0.5, w - .5, d - .5), 0, 90, pen)
        draw.line((w - .5, r, w - .5, h-r), pen)

        draw.arc((w - d + .5, h - d + .5, w - .5, h - .5), 270, 360, pen)
        draw.line((w - r, h - .5, r, h - .5), pen)

        draw.arc((0.5, h - d + .5, d - .5, h - .5), 180, 270, pen)
        draw.line((0.5, h - r, 0.5, r), pen)

        draw.flush()

        return img

