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

from urllib.parse import urljoin
import os.path

from django.conf import settings
from django.template import Library, TemplateSyntaxError

from ..thumbnail import ThumbError
from ..djangothumbnail import DjangoThumbnail


register = Library()


@register.filter
def sorethumb(file_field, processor_name):
    """ Returns the url path to a thumbnail for a given thumbnail processor. """

    try:
        processor = DjangoThumbnail.get_processor(processor_name)
    except ThumbError as e:
        raise TemplateSyntaxError(str(e))

    image_path = os.path.join(settings.MEDIA_ROOT, str(file_field))
    path = processor.process(image_path)

    return path
