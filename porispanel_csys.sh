#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

FILE=models/$1.graphml
FILE1=models/$1.ods
FILE2=models/$1.out.graphml
FILE3=models/$1.xml

if test -f "$FILE"; then
    echo "Input $FILE exists, continuing"
else
    echo "Input $FILE does not exist, aborting"
    exit 1;
fi

rm $FILE1
rm $FILE3

cp pyPORIS/config_csys_enabled.py pyPORIS/config_csys.py || { echo "config_csys_enabled.py missing"; exit 1; } 
python3 pyPORIS/graph2poris.py $FILE || { echo "graph2poris could not be processed"; exit 1; }
if test -f "$FILE1"; then
    echo "Input $FILE1 exists, continuing"
else
    echo "Input $FILE1 does not exist, aborting"
    exit 1;
fi

if test -f "$FILE2"; then
    echo "Input $FILE2 exists, continuing"
else
    echo "Input $FILE2 does not exist, aborting"
    exit 1;
fi
timestamp=$(date +%s)
cp $FILE models/$1.$timestamp.backup
mv $FILE models/$1.old.graphml
mv $FILE2 $FILE
python3 pyPORIS/poris2xml.py $FILE1 || { echo "poris2xml could not be processed"; exit 1; } 
if test -f "$FILE3"; then
    echo "Input $FILE3 exists, continuing"
else
    echo "Input $FILE3 does not exist, aborting"
    exit 1;
fi
java -jar pyPORIS/AstroPorisPlayer/bin/AstroPorisPlayer.jar $FILE3

