#!/bin/bash
# remove existing docs if they exist
if [ -d "docs" ]; then
    rm -rf docs
fi

# generate new docs
pdoc --html -o docs src/poldracklab

# add new docs to git
git add docs
git commit -m "Update documentation"
	