#!/bin/bash
# Create the subset repo from the export file.
# Must be run on the lsst-devl cluster.

butler create repo
butler import -t copy --export-file dc2-exports.yaml repo /repo/dc2

# Recompress the images using lossy compression to cut file sizes.
find repo/2.2i/ -name "*.fits" | xargs funpack -F 
find repo/2.2i/ -name "*.fits" | xargs fpack -q 2 -r -F -Y
