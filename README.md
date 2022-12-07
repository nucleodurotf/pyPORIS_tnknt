# pyPORIS_user

An example of how to use pyPORIS to model your own instruments

The purpose of this repo is provide an starting point to fork, so every user can have her/his own modeling environment with her/his own models under control system.
The repo uses the pyPORIS toolchain (https://github.com/cosmoBots/pyPORIS) which is obtained as a submodule.
The toolchain commands (files with *.sh) are just copied from the pyPORIS ones and adapted to the new models location.

The models are located in the models folder.  You can find there some examples which you can delete once you've validated your toolchain.


## Requirements

- Java
- Python 3

Install python libraries:

    pip3 install bs4
    pip3 install lxml
    pip3 install pyexcel_ods
    pip3 install python-redmine

NOTE: In Windows you should use 'pip' instead of 'pip3'

## Forking

Just go to Github https://github.com/cosmoBots/pyPORIS_user and press the fork button.  Set the new path, let's say you create the fork in https://github.com/myname/myporismodels

Then copy the clone link for the new forked repository and execute the typical clone action, something like this:

    git clone git@github.com:myname/myporismodels.git

Then you can enter the cloned repository folder:

    cd myporismodels

## Preparation after forking

Execute:

    git submodule update --init --recursive

It will populate pyPORIS folder and the AstroPorisPlayer binaries.  pyPORIS contains the PORIS toolkit toolchain to parse models in GraphML diagrams and convert them to ODS and XML files, and to create a Python class from the model, and AstroPorisPlayer allows you to interactively play with a configuration panel (using Java Swing technology) so you can check your model fits your expectations.

## Using the toolchain

This repo has been done so you can execute some of the features pyPORIS provides.  Not all the features provided from pyPORIS have been translated to this repository.  Please check https://github.com/cosmoBots/pyPORIS/blob/main/README.md for details.

The features currently added are:

- porispanel.sh Creates a PORIS representation in ODS and XML format from a PORIS diagram in GraphML, and launches a configuration panel to validate the model.
- porispanel_csys.sh Adds to porispanel.sh the synchronization with a cosmoSys instance.
- redoPorisPython.sh and doPorisPython.sh converts an ODS representation of a PORIS model into convenient Python classes.

The toolchain commands have been adapted to have the same behaviour of the pyPORIS ones, but acting on ./models and ./output folders of this repo instead of acting on ./pyPORIS/models or ./pyPORIS/output

Apart from this transparent adaptation, the syntax is the same.

## Updating the toolchain as time passes

The pyPORIS submodule is cloned and initialized from an specific commit entry, identified by a hash.  If you would like to update the submodule to point to another commit entry you should update it manually.  Let's say you want to update to a new commit entry 9343abf...

    cd pyPORIS
    git fetch --all
    git checkout -b 9343abf
    git pull
    cd ..
    git commit pyPORIS
    git commit -m "Updated to a different pyPORIS version"

If you want to prepare your local copy to be regularly updating it to use latest pyPORIS version in the main branch:

    cd pyPORIS
    git fetch --all
    git checkout -b main
    git pull
    cd ..
    git commit pyPORIS
    git commit -m "Updated to the latest commit in main branch of pyPORIS"

and then, regularly update your pyPORIS using the following sentence.

    git submodule update --init --recursive

Take into account that pyPORIS might be changing the syntaxes or the procedures, so you will be responsible of keeping your *.sh or *.bat files compatible with the version of pyPORIS you are using.

HINT: From time to time we at cosmoBots.eu update the repository you initially forked from.  You can check the changes occurred in it to have an idea of the adaptations needed to support newer versions of pyPORIS

## Conclusion
Happy modeling!

cosmoBots.eu
