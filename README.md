# pyPORIS_user
An example of how to use pyPORIS to model your own instruments

* graph2poris.py: Creates a PORIS model in ODS format from a PORIS diagram in GraphML.
* poris2xml.py: Creates a PORIS xml file from a PORIS model in ODS format.

## Requirements
* Java
* Python 3
    * pip3 install bs4
    * pip3 install lxml
    * pip3 install pyexcel_ods
    * pip3 install python-redmine

NOTE: In Windows you should use 'pip' instead of 'pip3'

## Preparation after cloning
Execute:

    git submodule update --init --recursive

It will populate pyPORIS folder and the AstroPorisPlayer binaries.

## Using it
### Linux / *nix
Simply:

    ./porispanel.sh example

or, if wanting to sync it with a cosmoSys instance:

    ./porispanel_csys.sh example

The cosmoSys instance has to be configured by copying pyPORIS/config_rm_enabled.py.example to pyPORIS/config_rm_enabled.py and adding your secrets there.
### Windows
Simply:

    winporispanel.bat example

or, if wanting to sync it with a cosmoSys instance:

    winporispanel_csys.bat example

The cosmoSys instance has to be configured by copying pyPORIS\config_rm_enabled.py.example to pyPORIS\config_rm_enabled.py and adding your secrets there.

## Conclusion
Happy modeling!

cosmoBots.eu
