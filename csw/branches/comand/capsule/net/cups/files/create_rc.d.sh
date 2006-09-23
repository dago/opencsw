#!/bin/sh

prg=`basename $0`
destdir="$1"
runlevel_dirs="rc0.d rc1.d rc2.d rc3.d rcS.d"
init_script=cswcups
startlevel=98
stoplevel=14

if [ "$destdir" = "" ]; then
  echo "usage: $prg <destdir>" 1>&2
  exit 1
fi

echo "Checking for $destdir/etc/init.d..."
test -d "$destdir/etc/init.d" || mkdir -p "$destdir/etc/init.d"

echo "Copying init script..."
cp -p "files/$init_script" "$destdir/etc/init.d"

for d in $runlevel_dirs; do
  echo "Processing runlevel directory $d..."
  if [ "$d" = "rc3.d" ]; then
    linkname="S$startlevel$init_script"
  else
    linkname="K$stoplevel$init_script"
  fi
  test -d "$destdir/etc/$d" || mkdir "$destdir/etc/$d"
#  echo "cd $destdir/etc/$d; ln -s ../init.d/$init_script $linkname"
  (cd "$destdir/etc/$d"; \
    test -h "$linkname" || ln -s "../init.d/$init_script" "$linkname")
done
