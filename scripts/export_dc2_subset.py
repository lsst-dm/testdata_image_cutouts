#!/usr/bin/env python
"""Create a gen3 exports.yaml file containing a few filters on one patch from
a weekly run on `/repo/dc2` on the lsst-devl cluster.
"""

import itertools
import lsst.daf.butler

# Update the weekly version and ticket number here to use a newer run.
# You will then have to change the collection in the tests then, too.
collection = "2.2i/runs/test-med-1/w_2022_03/DM-33223"

patch = 24
tract = 3828


def main():
    butler = lsst.daf.butler.Butler('/repo/dc2', collections=collection)
    with butler.export(filename="dc2-exports.yaml") as export:
        where = f"instrument='LSSTCam-imSim' and patch={patch} and tract={tract} and skymap='DC2'"
        for datasetType, band in itertools.product(('deepCoadd_calexp', ), ('g', 'r', 'i')):
            export.saveDatasets(butler.registry.queryDatasets(datasetType=datasetType,
                                                              where=where + f" and band='{band}'"))

        export.saveDatasets(butler.registry.queryDatasets(collections='skymaps',
                                                          datasetType='skymap'))
        export.saveDataIds(
            butler.registry.queryDataIds(
                ["patch"],
                where=f"tract={tract} AND skymap='DC2'"
            ).expanded()
        )


if __name__ == "__main__":
    main()
