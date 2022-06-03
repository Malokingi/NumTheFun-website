#!/bin/bash

## Args
CM=$1 # Commit Message

echo "# running $0 with commit message '$CM'"

git add .
git commit -m "$CM"
git push