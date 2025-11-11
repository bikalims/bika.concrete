# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory

from bika.lims.api import get_request
from bika.concrete.interfaces import IBikaConcreteLayer

PRODUCT_NAME = "bika.concrete"
PROFILE_ID = "profile-{}:default".format(PRODUCT_NAME)
logger = logging.getLogger(PRODUCT_NAME)
_ = MessageFactory(PRODUCT_NAME)


def is_installed():
    """Returns whether the product is installed or not"""
    request = get_request()
    return IBikaConcreteLayer.providedBy(request)
