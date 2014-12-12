Major
=====

Strict build lifecycles with flexible build steps.

Install:
```
export MAJOR_PATH=/opt/Major
mkdir $MAJOR_PATH
git clone https://github.com/MitchK/Major.git $MAJOR_PATH
echo "export MAJOR_PATH=$MAJOR_PATH" >> ~/.bash_profile (or .bashrc on Linux)
echo "export PATH=$MAJOR_PATH/bin:$PATH" >> ~/.bash_profile (or .bashrc on Linux)
chmod a+x $MAJOR_PATH/bin/major
source  ~/.bash_profile (or .bashrc on Linux)
major ping
```
