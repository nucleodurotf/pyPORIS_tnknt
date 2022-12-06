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

## Converting model to *.ODS, *.XML and open a Java Swing Configuration panel

The PORIS toolkit allows you to convert your model in a GraphML file to models in ODS and XML files.
The ODS file is a representation of the model in an spreadsheet format, useful for later processes like creating Python or C++ classes from it, or importing into cosmoSys.
The XML file is used by the AstroPorisPlayer Java Swing frame app to show an interactive panel to explore/validate your model.
The last step of this conversion process is to show the AstroPorisPlayer panel.

The model must be specified by indicating the relative path from the "models" folder to the GraphML file, but without including the .graphml extension.
Example: if you would like to convert the ./models/example/example.graphml file, just provide example/example as an argument.

### Linux / *nix
Simply:

    ./porispanel.sh example/example

or, if wanting to sync it with a cosmoSys instance:

    ./porispanel_csys.sh example/example

The cosmoSys instance has to be configured by copying pyPORIS/config_rm_enabled.py.example to pyPORIS/config_rm_enabled.py and adding your secrets there.

### Windows

POLICY: In cosmoBots.eu we are targeted to produce open source code for open source platforms.  Windows or Mac adaptations are never maintained by us.  They appear into our projects as external contributions, and we never check possible regressions after we update our tools.  Maintenance for those external contributions shall be external too.  Pull requests are welcome.

(so thanks Claudia)

Simply:

    winporispanel.bat example\example

or, if wanting to sync it with a cosmoSys instance:

    winporispanel_csys.bat example\example

The cosmoSys instance has to be configured by copying pyPORIS\config_rm_enabled.py.example to pyPORIS\config_rm_enabled.py and adding your secrets there.

## Generating Python PORIS classes from your models

Requirement: you must have generated an ODS file, check above.

### Linux / *nix
./redoPorisPython example/example

Simply:

    ./redoPorisPython.sh example/example

### Windows

Not yet implemented, but collaborations are welcome.  

POLICY: In cosmoBots.eu we are targeted to produce open source code for open source platforms.  Windows or Mac adaptations are never maintained by us.  They appear into our projects as external contributions, and we never check possible regressions after we update our tools.  Maintenance for those external contributions shall be external too.  Pull requests are welcome.

HINTS: Someone might want to adapt the redoPorisPython.sh to a redoPorisPython.bat, and doPorisPython.sh to doPorisPython.bat.
The generator is using symbolic links to allow the generated code to live in separate folders but being easy to test.  A similar behaviour should be created for windows.  
Easiest way is copying the PORIS/PORIS.py class and the automatically generated output/modename/modelname/modelnamePORIS.py class inside the output/modelname/modelname_physical/ folder, but having duplicated files is alwayas a bad idea. 
In order to have a repo which is easy to maintain, windows symbolic links solutions have to be analysed.

## Conclusion
Happy modeling!

cosmoBots.eu
