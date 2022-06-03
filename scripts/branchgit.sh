#!/bin/bash

## functions
branch_exists() {
    local branch=${1}
    local existed_in_local=$(git branch --list ${branch})
    if [[ -z ${existed_in_local} ]]; then
        echo 0
    else
        echo 1
    fi
}

## Args
BN=$1 # Branch Name

echo "# running $0 with branch name '$BN'"

if [[ $(branch_exists $BN) -eq "1" ]]; then
    git checkout $BN
    git pull
else
    echo "# wait that's a new branch. making new branch named '$BN'..."
    git checkout -b $BN
    git push --set-upstream origin $BN
fi

## Tips
# List all current Git Branches: git branch --list