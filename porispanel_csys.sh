#!/bin/bash
#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1;
fi

FILE=models/$1.graphml
if test -f "$FILE"; then
    echo "Input $FILE exists, continuing"
else
    echo "Input $FILE does not exist, aborting"
    exit 1;
fi
rm models/$1.ods
rm models/$1.xml
cp pyPORIS/config_csys_enabled.py pyPORIS/config_csys.py || { echo "config_rm_enabled.py missing"; exit 1; } 
python3 pyPORIS/graph2poris.py models/$1.graphml || { echo "graph2poris could not be processed"; exit 1; }
timestamp=$(date +%s)
cp models/$1.graphml models/$1.$timestamp.backup
mv models/$1.graphml models/$1.old.graphml
mv models/$1.out.graphml models/$1.graphml
python3 pyPORIS/poris2xml.py models/$1.ods || { echo "poris2xml could not be processed"; exit 1; } 
java -jar pyPORIS/AstroPorisPlayer/bin/AstroPorisPlayer.jar models/$1.xml

