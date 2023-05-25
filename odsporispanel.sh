##!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

FILE1=models/$1.ods
FILE3=models/$1.xml

if test -f "$FILE1"; then
    echo "Input $FILE1 exists, continuing"
else
    echo "Input $FILE1 does not exist, aborting"
    exit 1;
fi
rm $FILE3
python3 pyPORIS/poris2xml.py $FILE1 || { echo "poris2xml could not be processed"; exit 1; } 
if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi
java -jar pyPORIS/AstroPorisPlayer/bin/AstroPorisPlayer.jar $FILE3
