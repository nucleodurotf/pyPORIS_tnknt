##!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

FILE3=models/$1.xml

if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi
java -jar pyPORIS/AstroPorisPlayer/bin/AstroPorisPlayer.jar $FILE3
