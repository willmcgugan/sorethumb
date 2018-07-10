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

def parse_color(col):
    """ Transforms an html style color (ie #fe23dd) in to a tuple of three
    values. Any values which are not strings, are passed through unaltered.

    """
    if isinstance(col, (bytes, str)):
        col = col.lstrip('#')
        try:
            if len(col) == 6:
                return tuple([int(c, 16) for c in (col[0:2], col[2:4], col[4:6])])
            elif len(col) == 3:
                return tuple([int(c, 16) * 17 for c in col])
            else:
                raise ValueError("html colours must be 3 or 6 hex characters")
        except ValueError as e:
            raise ValueError("'%s' is not an html colour (%s)" % (col, e.message))
    return col


def html_color(col):
    """ Generates an html colour from a tuple of three values. """
    return ''.join(['%02x' % c for c in col])


class Filter(object):
    """ The base class for thumb filters. """

    def __init__(self, *args, **kwargs):
        self._params = (args, kwargs)

    def get_params(self):
        return self._params

    def __call__(self, img):
        """ The call method should return a PIL image instance (or the same one)
        or None, if no changes are required.

        """
        raise NotImplementedError


