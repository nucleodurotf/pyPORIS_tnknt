##!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

DIR=models/$1
FILE1=models/$1/$1.ods
FILE3=models/$1/$1.xml

if test -d "$DIR"; then
    echo "Input $DIR exists, continuing"
else
    echo "Input $DIR does not exist, aborting"
    exit 1;
fi

rm $FILE1
rm $FILE3

cp pyPORIS/config_csys_disabled.py pyPORIS/config_csys.py
python3 pyPORIS/graphdir2poris.py $DIR || { echo "graph2poris could not be processed"; exit 1; }
if test -f "$FILE1"; then
    echo "Input $FILE1 exists, continuing"
else
    echo "Input $FILE1 does not exist, aborting"
    exit 1;
fi
python3 pyPORIS/poris2xml.py $FILE1 || { echo "poris2xml could not be processed"; exit 1; } 
if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi
java -jar pyPORIS/AstroPorisPlayer/bin/AstroPorisPlayer.jar $FILE3
