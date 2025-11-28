# -*- coding: utf-8 -*-

from bika.lims import api
from bika.concrete import PRODUCT_NAME
from bika.concrete import PROFILE_ID
from bika.concrete import logger
from bika.concrete.setuphandlers import setup_catalogs
from bika.concrete.setuphandlers import add_location_to_supplier
from bika.concrete.setuphandlers import setup_id_formatting

from senaite.core.catalog import SETUP_CATALOG
from senaite.core.upgrade import upgradestep

version = "1.0.3"
OLD_PACKAGE = 'bika.cement'
NEW_PACKAGE = 'bika.concrete'


@upgradestep(PRODUCT_NAME, version)
def upgrade(tool):
    portal = tool.aq_inner.aq_parent
    setup = portal.portal_setup
    ver_from = "1000"

    logger.info(
        "Upgrading {0}: {1} -> {2}".format(PRODUCT_NAME, ver_from, version)
    )

    # -------- ADD YOUR STUFF BELOW --------

    setup.runImportStepFromProfile(PROFILE_ID, "typeinfo")

    logger.info("{0} upgraded to version {1}".format(PRODUCT_NAME, version))
    return True


def reindex_mix_materials(tool):
    logger.info("Reindexing mix material ...")
    setup_catalogs(api.get_portal())
    cat = api.get_tool(SETUP_CATALOG)
    for brain in cat(portal_type="MixMaterial"):
        obj = brain.getObject()
        logger.info("Reindex mix material: %r" % obj)
        obj.reindexObject()
    for brain in cat(portal_type="MixMaterialAmount"):
        obj = brain.getObject()
        logger.info("Reindex mix material: %r" % obj)
        obj.reindexObject()
    logger.info("Reindexing mix materials [DONE]")


def add_brands(tool):
    portal = tool.aq_inner.aq_parent
    setup = portal.portal_setup
    # -------- ADD YOUR STUFF BELOW --------

    setup.runImportStepFromProfile(PROFILE_ID, "typeinfo")
    setup_id_formatting(portal)
    add_location_to_supplier(portal)
