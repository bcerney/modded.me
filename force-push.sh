#!/bin/bash

set -xe

git add -A

git commit --amend --no-edit

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ "$CURRENT_BRANCH" != "master" ]; then
    git push -f origin $CURRENT_BRANCH
else
    echo "On master branch, do not force push"
fi
