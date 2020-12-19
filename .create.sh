#!/bin/bash 

# . means to source the contents of this file into the current shell

function create() {
    cd '/Users/Jack/Documents/Projects/project_auto/'
    source .env
    # $1 is the first positional argument in the script
    python create.py $1

    # Add notes.txt file to notes folder 
    cd $FILEPATH$1/notes/
    echo Notes > notes.txt

    # The standard git stuff
    cd $FILEPATH$1
    git init -b main
    git add .
    git commit -m "Project creation"
    git remote add origin https://github.com/$USERNAME/$1
    touch README.md
    git push -u origin main
}

