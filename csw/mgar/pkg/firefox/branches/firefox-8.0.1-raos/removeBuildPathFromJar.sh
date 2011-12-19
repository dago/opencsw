#!/opt/csw/bin/bash -x

if [ -d ~/.tempextractjar ] ; 
then 
	rm -fr ~/.tempextractjar
fi 
mkdir ~/.tempextractjar

BACKUP_OLD_DIR=`pwd` 
export REPLACEDIR=$2/$3/$4

cd ~/.tempextractjar
jar xvf $BACKUP_OLD_DIR/$1

gfind . -name "*.js" -exec bash -x -c " mv {} {}.temp && gsed -e  s_\$REPLACEDIR\_\_g {}.temp > {} && rm {}.temp"  \; 

rm $1
jar cvf $BACKUP_OLD_DIR/$1 *

cd $BACKUP_OLD_DIR

rm -fr ~/.tempextractjar
