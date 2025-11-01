# -*- coding: utf-8 -*-

from bika.lims import api
from senaite.core.catalog import SETUP_CATALOG


def get_mix_design(self):
    import pdb; pdb.set_trace()
    batch = self
    query = {
        "portal_type": "MixDesign",
        "path": {
            "query": api.get_path(batch),
        },
    }
    brains = api.search(query, SETUP_CATALOG)
    if len(brains) == 1:
        return api.get_object(brains[0])

    values = batch.values()
    mix_design = [md for md in values if md.portal_type == "MixDesign"]
    if len(mix_design) == 1:
        return mix_design[0]
    return None
