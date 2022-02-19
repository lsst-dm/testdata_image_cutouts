######################
testdata_image_cutouts
######################

``testdata_image_cutouts`` is a package in the `LSST Science Pipelines <https://pipelines.lsst.io>`_.

This package contains a butler repo with a three coadd images for testing the image cutouts service.
Contains bands `gri` for `tract=3828` and `patch=24` with `skymap="DC"`.
Use `collection="2.2i/runs/test-med-1/w_2022_03/DM-33223/20220118T193330Z"` to read the `deepCoadd_calexp` data.
The images have been recompressed with fpack lossy Rice compression, to reduce the size of the repo (we don't actually care about preserving original pixel values here).

A clone of this repo takes up about 300MB of space.

Updating the repo
=================

To reproduce the data with a new weekly run of DC2, update the `collection` value in `scripts/export_dc2_subset.py`, run these commands from the root of this package on lsst-devl:

```
rm -r repo/
python scripts/export_dc2_subset.py
bash scripts/make_dc2_subset_repo.sh
```

In order for the butler datastore file integrity check to pass, change the `file_datastore_records` table in `repo/gen3.sqlite3` to set all three `file_size` fields to `-1`.

Test out the new data, and then commit the updated scripts, `dc2-exports.yaml` file, and `repo` directory (check that all relevant large files are using `git-lfs`).
