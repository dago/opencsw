#!/usr/bin/bash
set -e

# NOTE: if creatpkg -r fails: rm -rf  /var/spool/pkg/CSWlighttpd

VERSION="1.4.28"
TARBALL="lighttpd-$VERSION.tar.gz"
ROOT_TB="lighttpd-$VERSION"
PKG_NAME="lighttpd"
REV=",REV=`date +%Y.%m.%d`"
CURRENT="$HOME/opencsw/lighttpd"

#export PATH="/usr/ccs/bin:/usr/bin:/opt/csw/bin:/opt/sfw/bin:/opt/local/bin:$PATH"
#export PATH="$PATH:/opt/studio/SOS11/SUNWspro/bin:/opt/studio/SOS11/SUNWspro/lib"
# For Studio
#export PATH="/opt/studio/SOS11/SUNWspro/bin:/opt/studio/SOS11/SUNWspro/lib:$PATH:/opt/csw/bin:/usr/ccs/bin"
# For gcc
export PATH="/opt/csw/gcc4/bin:/opt/csw/gcc4/lib:$PATH:/opt/csw/bin:/usr/ccs/bin"

rm -rf  /var/spool/pkg/CSWlighttpd

# 1. prepare metadata
rm -rf $HOME/pkgs/$PKG_NAME
mkdir -p $HOME/pkgs/$PKG_NAME
# Stuff for smf support
cp checkinstall preremove postinstall i.smfno i.smfyes space $HOME/pkgs/$PKG_NAME
cd  $HOME/pkgs/$PKG_NAME
rm -rf $HOME/build/$ROOT_TB
mkdir -p $HOME/build

(
cat <<-EOF
PKG=CSWlighttpd
NAME=lighttpd - Security, speed, compliance, and flexibility http server
VERSION=$VERSION$REV
CATEGORY=application
VENDOR=http://www.lighttpd.net/ packaged for CSW by David Rio Deiros
HOTLINE=http://www.opencsw.org/bugtrack/
EMAIL=drio@opencsw.org
EOF
) > ./pkginfo

# 2. compile source code
cd $HOME/build
rm -rf $ROOT_TB
echo "Untaring..."
gtar zxvf $HOME/src/$TARBALL > /dev/null
cp $HOME/patches/lighttpd.drio.patch .
# Not needed anymore
#gpatch -p0 < ./lighttpd.drio.patch
cd $ROOT_TB
cp COPYING $HOME/pkgs/$PKG_NAME/copyright

#export CFLAGS="-xarch=386"
#./configure --prefix=/opt/csw --with-openssl --with-pcre
./configure --prefix=/opt/csw --with-openssl-includes=/opt/csw/include --with-openssl-libs=/opt/csw/lib --disable-ipv6
#make
gmake -j4

stagepkg
cd cswstage

# 3. create start/stop scrip (for smf also)
mkdir -p ./etc/init.d/
cp $CURRENT/cswlighttpd ./etc/init.d
for i in 0 1 2 3 'S'; do
    mkdir ./etc/rc$i.d
    ln -s ./etc/init.d/cswlighttpd ./etc/rc$i.d/cswlighttpd
done
mkdir -p ./opt/csw/var/svc/manifest/network
cp $CURRENT/lighttpd.xml ./opt/csw/var/svc/manifest/network
mkdir -p ./opt/csw/lib/svc/method
cp $CURRENT/cswlighttpd ./opt/csw/lib/svc/method

# log/config/rootdir 
mkdir -p ./opt/csw/share/lighttpd-root
echo "Lighttpd works!" >>  ./opt/csw/share/lighttpd-root/index.html
chmod 755 ./opt/csw/share/lighttpd-root
chmod 755 ./opt/csw/share/lighttpd-root/index.html
mkdir -p ./opt/csw/var/lighttpd/

mkdir ./opt/csw/etc
cp $CURRENT/lighttpd.conf ./opt/csw/etc/lighttpd.conf.CSW
chmod 644 ./opt/csw/etc/lighttpd.conf.CSW

(
cat <<-EOF
d none  /opt/csw/var/lighttpd 0755 nobody nobody
d none  /opt/csw/share/lighttpd-root 0755 nobody nobody
f none  /opt/csw/share/lighttpd-root/index.html 0755 nobody nobody
f none  /opt/csw/etc/lighttpd.conf.CSW 0644 root bin
f smfno /etc/init.d/cswlighttpd=cswlighttpd 0755 root bin
l smfno /etc/rc0.d/K15cswlighttpd=/etc/init.d/cswlighttpd
l smfno /etc/rc1.d/K15cswlighttpd=/etc/init.d/cswlighttpd
l smfno /etc/rc2.d/K15cswlighttpd=/etc/init.d/cswlighttpd
l smfno /etc/rc3.d/S40cswlighttpd=/etc/init.d/cswlighttpd
l smfno /etc/rcS.d/K15cswlighttpd=/etc/init.d/cswlighttpd
d smfyes /opt/csw/var/svc 0755 root bin 
d smfyes /opt/csw/var/svc/manifest 0755 root bin
d smfyes /opt/csw/var/svc/manifest/network 0755 root bin
f smfyes /opt/csw/var/svc/manifest/network/lighttpd.xml=/lighttpd.xml 0644 root bin
d smfyes /opt/csw/lib/svc 0755 root bin
d smfyes /opt/csw/lib/svc/method 0755 root bin
f smfyes /opt/csw/lib/svc/method/cswlighttpd=cswlighttpd 0755 root bin
EOF
) >> ./lastpart

grep "^i" ./prototype > ./head
for i in checkinstall preremove postinstall i.smfno i.smfyes space;do 
   echo "i $i" >> ./head
done
grep -v "^i" ./prototype > realfiles
cat ./head ./realfiles ./lastpart > ./prototype
rm -f ./head ./lastpart ./realfiles

#cp $CURRENT/lighttpd.xml $HOME/pkgs/$PKG_NAME
#cp $CURRENT/cswlighttpd $HOME/pkgs/$PKG_NAME
#cp $CURRENT/index.html $HOME/build/$ROOT_TB/cswstage
cp $CURRENT/lighttpd.xml $HOME/build/$ROOT_TB/cswstage
cp $CURRENT/cswlighttpd $HOME/build/$ROOT_TB/cswstage
cp prototype $HOME/pkgs/$PKG_NAME
cd $HOME/pkgs/$PKG_NAME
rm -f *.pkg*
touch ./depend
#DPS=`createpkg -r $HOME/build/$ROOT_TB/cswstage 2>&1 | grep "^>" | grep -v SUNW | grep -v SPRO | sed 's/> //g'`
DPS="CSWexpat CSWfconfig CSWftype2 CSWgcc4g++rt CSWiconv CSWlibxft2 CSWlibxrender CSWxpm CSWzlib CSWbzip2 CSWosslrt CSWpcrert"

rm -f ./depend
for i in $DPS;do
    echo -e "P\t$i" >> ./depend
done
#echo "i depend" >> prototype
rm -f *.g

rm -f $HOME/pkgs/$PKG_NAME/*.gz
createpkg -r $HOME/build/$ROOT_TB/cswstage

mv *.pkg.gz $HOME/ready
gls -lach $HOME/ready
