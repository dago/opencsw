#!/bin/sh

# buildms.sh - script for easier build of MailScanner
# usage: buildms.sh [ source file ]
# 2006-05-12 Peter Bonivart
# 2006-05-15 First working version
# 2007-07-09 Lots added
# 2007-07-10 Added .CSW and lots more
# 2007-07-11 Added mods to MailScanner.conf, spam.assassin.prefs.conf and
#            virus.scanners.conf. Support REV=YYYY.MM.DD
# 2007-07-12 Added mods to check_mailscanner, syslog type
# 2007-07-16 Added mods to MailScanner.conf: clamd settings
# 2007-08-14 Added mod so symlink from /opt is not needed. Fixed so 4.62+ tar
#	     filename (includes build rev) is handled
# 2007-08-15 Added path mod to check_MailScanner.cron. Patch check_mailscanner
# 2007-08-21 Remove unnecessary files (other OS and so on). Added history file
#	     to package
# 2007-09-03 Remove snv-commit files that are left over
# 2007-09-13 Add changelog to package, removed patching of check_mailscanner
#            (not needed with 4.63.8)
# 2007-10-01 Changelog included in 4.64, moved README and COPYING to CSW doc
# 2008-01-03 Added wrapper script to /opt/csw/bin/MailScanner instead of
#            symlink so lint etc works. PERLIB added to rc-script. Dependency
#            to CSWpmio added
# 2008-01-09 Backed out changes from 2008-01-03. Fixed path to tnef-binary in
#            MailScanner.conf and added unrar and mailtools as dependencies
# 2008-04-09 Changed awk to CSW gawk in SA.pm. Always add REV=YYYY.MM.DD.
# 2008-06-19 Changed gtar path to /usr/sfw/bin (login changed to loginz),
#            added pm_converttnef, pm_podescapes, pm_podsimple and pm_testpod
#            as dependencies
# 2008-06-27 Removed displaying full license during install, instead show just a
#            short message referring to the license file
# 2008-07-03 Added SMF support
# 2008-09-04 Fixed path to sendmail in MailScanner.conf, symlink cswmailscanner
#            works regardless of SMF or not
# 2008-11-18 Fixed SA Install Prefix and Local State Dir in MailScanner.conf
# 2008-12-18 Changed copyright filename to LICENSE, gtar path
# 2009-01-13 Fixed path for ClamAV update monitoring
# 2009-01-21 Fixed path for SpamAssassin Site Rules Dir, fixed
#            update_spamassassin
# 2009-01-23 Fixed Sendmail service script
# 2009-01-24 Added etc/MailScanner file
# 2009-10-01 Run only on build servers, not on login server
# 2010-02-22 Copy package to experimental instead of testing, changed SA path
#            from /opt/csw/etc/spamassassin to /etc/opt/csw/spamassassin
# 2010-07-02 Lowercase license filename. Make conffiles 0400 to protect it
# 2010-07-03 Use /tmp/clamd.socket for ClamAV socket
# 2010-09-01 Fixed update_spamassassin.cron, switch to 5.9

# todo: 

# abort execution in case of error

set -e

BSVER=2.22
SLTYPE=udp

PATHPREFIX1=/home/bonivart
PATHPREFIX2=/home
PKGDIR=$PATHPREFIX1/pkgs/mailscanner
BUILDDIR=$PATHPREFIX1/build/mailscanner
SRCDIR=$PATHPREFIX2/src/mailscanner
TESTDIR=$PATHPREFIX2/experimental/bonivart
GTAR=/opt/csw/bin/gtar

# abort if not on build server

if [ `uname -n` = "login" ]; then
  echo "Run on build server. Exiting."
  exit 1
fi
 
# select source file

if [ "$1" ]; then
  if [ ! -s "$SRCDIR/$1" ]; then
    echo "-err-> No such source file: $1. Exiting."
    exit 1
  else
    src=$1
  fi
else
  echo "-> No source file given on command line. Select from:"
  echo
  ls -t $SRCDIR | grep '^MailScanner'
  echo
  echo "Enter source file: \c"
  read src
  if [ ! -s "$SRCDIR/$src" -o ! "$src" ]; then
    echo "-err-> No such source file: $src. Exiting."
    exit 1
  fi
fi

# log stuff

version=`echo $src | awk -F'-' '{print $3}'`
rev=`echo $src | awk -F'-' '{print $4}' | awk -F'.' '{print $1}'`
cswrev=`date +%Y.%m.%d`
timestamp=`date +%y%m%d-%H%M`
LOGDIR=$PKGDIR/$version-$timestamp
TARLOG1=$LOGDIR/tarlog1
TARLOG2=$LOGDIR/tarlog2
LOG=$LOGDIR/buildms.log
mkdir $LOGDIR

# copy current build script and misc other files to log dir

cp $PKGDIR/$0 $LOGDIR
cp $PKGDIR/depend $LOGDIR
cp $PKGDIR/pkginfo.stub $LOGDIR
cp $PKGDIR/postinstall $LOGDIR
#cp $PKGDIR/postremove $LOGDIR	# not used at the moment
#cp $PKGDIR/preinstall $LOGDIR	# not used at the moment
cp $PKGDIR/preremove $LOGDIR
cp $PKGDIR/prototype.stub $LOGDIR
cp $PKGDIR/README.CSW $LOGDIR
cp $PKGDIR/cswmailscanner $LOGDIR
cp $PKGDIR/cswmailscanner.sendmail $LOGDIR
cp $PKGDIR/history $LOGDIR
cp $PKGDIR/SA.pm.patch $LOGDIR
cp $PKGDIR/checkinstall $LOGDIR
cp $PKGDIR/i.smfno $LOGDIR
cp $PKGDIR/i.smfyes $LOGDIR
cp $PKGDIR/space $LOGDIR
cp $PKGDIR/mailscanner.xml $LOGDIR
cp $PKGDIR/mailscanner.sendmail.xml $LOGDIR
cp $PKGDIR/MailScanner $LOGDIR
echo "-> Build script version: $BSVER" | tee $LOG
echo "-> Builder: `/usr/ucb/whoami`" | tee $LOG
echo "-> Build host: `uname -n`" | tee -a $LOG
echo "-> Build time: `date +'%Y-%m-%d %H:%M'`" | tee -a $LOG
echo "-> Source file: $src" | tee -a $LOG
echo "-> Version: $version" | tee -a $LOG
echo "-> Revision: $rev" | tee -a $LOG
if [ "$cswrev" ]; then
  echo "-> CSW Revision: $cswrev" | tee -a $LOG
  cswrev=",REV=$cswrev"
fi
echo "-> Log directory: $LOGDIR" | tee -a $LOG

# unpack source file in build dir

cd $BUILDDIR
echo "-> Unpacking source file ..." | tee -a $LOG
if [ -d "$BUILDDIR/MailScanner-install-$version" ]; then
  echo "-err-> Directory already exists. Exiting." | tee -a $LOG
  exit 1
fi
$GTAR xvzf "$SRCDIR/$src" > $TARLOG1
echo "-> Unpacking MailScanner into MailScanner-install-$version/mailscanner ..." | tee -a $LOG
cd $BUILDDIR/MailScanner-install-$version
$GTAR xvzf $BUILDDIR/MailScanner-install-$version/perl-tar/MailScanner-$version-$rev.tar.gz > $TARLOG2
mv MailScanner-$version-$rev mailscanner

# replace /usr/bin/perl with /opt/csw/bin/perl

cd mailscanner
find . -type f | xargs grep -n '#!/usr/bin/perl' | grep :1: | awk -F':' '{print $1}' > $LOGDIR/perlpathfix
echo "-> Fixing perl path in `wc -l $LOGDIR/perlpathfix | awk '{print $1}'` files ..." | tee -a $LOG
for i in `cat $LOGDIR/perlpathfix`
do
  echo "---> Fixing perl path in $i ..." >> $LOG
  sed 's/^#!\/usr\/bin\/perl/#!\/opt\/csw\/bin\/perl/' $i > $i.tmp
  mv $i.tmp $i
done
cd ..

# fix MailScanner.conf

cd mailscanner/etc

echo "-> Modifying MailScanner.conf for use with CSW ..." | tee -a $LOG
sed 's/\/opt\/MailScanner/\/opt\/csw\/mailscanner/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^TNEF Expander = \/opt\/csw\/mailscanner\/bin\/tnef/TNEF Expander = \/opt\/csw\/bin\/tnef/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^Incoming Work User =/Incoming Work User = clamav/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^Incoming Work Permissions = 0600/Incoming Work Permissions = 0640/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

#sed 's/^Clamd Socket = \/tmp\/clamd/Clamd Socket = \/tmp\/clamd.socket/' MailScanner.conf > MailScanner.conf.tmp
#mv MailScanner.conf.tmp MailScanner.conf

sed 's/^Monitors for ClamAV Updates = \/usr\/local\/share\/clamav\/\*\.cld \/usr\/local\/share\/clamav\/\*\.cvd/Monitors for ClamAV Updates = \/var\/opt\/csw\/clamav\/db\/\*\.cld \/var\/opt\/csw\/clamav\/db\/\*\.cvd/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^Unrar Command = \/usr\/bin\/unrar/Unrar Command = \/opt\/csw\/bin\/unrar/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^Sendmail = \/usr\/lib\/sendmail/Sendmail = \/opt\/csw\/lib\/sendmail/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^Sendmail2 = \/usr\/lib\/sendmail/Sendmail2 = \/opt\/csw\/lib\/sendmail/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^SpamAssassin Install Prefix =/SpamAssassin Install Prefix = \/opt\/csw/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^SpamAssassin Local State Dir = # \/var\/lib\/spamassassin/SpamAssassin Local State Dir = # \/var\/opt\/csw\/spamassassin/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

sed 's/^SpamAssassin Site Rules Dir = \/etc\/mail\/spamassassin/SpamAssassin Site Rules Dir = \/etc\/opt\/csw\/spamassassin/' MailScanner.conf > MailScanner.conf.tmp
mv MailScanner.conf.tmp MailScanner.conf

cd ../..

# fix spam.assassin.prefs.conf

cd mailscanner/etc
echo "-> Modifying spam.assassin.prefs.conf for use with CSW ..." | tee -a $LOG
sed 's/^dcc_path \/usr\/local\/bin\/dccproc$/dcc_path \/opt\/csw\/bin\/dccproc/' spam.assassin.prefs.conf > spam.assassin.prefs.conf.tmp
mv spam.assassin.prefs.conf.tmp spam.assassin.prefs.conf
cd ../..

# fix virus.scanners.conf

cd mailscanner/etc
echo "-> Modifying virus.scanners.conf for use with CSW ..." | tee -a $LOG
sed '/^clamav/s/\/usr\/local/\/opt\/csw/;/^clamd/s/\/usr\/local/\/opt\/csw/' virus.scanners.conf > virus.scanners.conf.tmp
mv virus.scanners.conf.tmp virus.scanners.conf
cd ../..

# fix check_mailscanner

cd mailscanner/bin
echo "-> Modifying check_mailscanner for use with CSW ..." | tee -a $LOG
sed "s/^  echo -n \'Starting MailScanner...\'/  echo \'Starting MailScanner...\\\c\'/" check_mailscanner > check_mailscanner.tmp
mv check_mailscanner.tmp check_mailscanner
cd ../..

# fix update_spamassassin

cd mailscanner/bin
echo "-> Modifying update_spamassassin for use with CSW ..." | tee -a $LOG
# sed replace /usr with /opt/csw, replace /etc/init.d with /opt/csw/bin, replace /etc/mail with /opt/csw/etc, replace /etc/sysconfig with /opt/csw/mailscanner/etc, insert PATH, SA conf file
sed 's/\/usr/\/opt\/csw/;s/^\/etc\/init.d\/MailScanner/\/opt\/csw\/bin\/cswmailscanner/;s/\/etc\/mail/\/opt\/csw\/etc/;s/\/etc\/sysconfig/\/opt\/csw\/mailscanner\/etc/;s/^SAUPDATEARGS/PATH=\/opt\/csw\/bin:\/usr\/bin ; export PATH ; SAUPDATEARGS/;s/\/opt\/csw\/mailscanner\/etc\/update_spamassassin/\/opt\/csw\/mailscanner\/etc\/MailScanner/;s/\/opt\/csw\/etc\/spamassassin/\/etc\/opt\/csw\/spamassassin/' update_spamassassin > update_spamassassin.tmp
mv update_spamassassin.tmp update_spamassassin
cd ../..

# fix update_spamassassin.cron

cd mailscanner/bin/cron
echo "-> Modifying update_spamassassin.cron for use with CSW ..." | tee -a $LOG
sed 's/\/etc\/sysconfig\/update_spamassassin/\/opt\/csw\/mailscanner\/etc\/MailScanner/' update_spamassassin.cron > update_spamassassin.cron.tmp
mv update_spamassassin.cron.tmp update_spamassassin.cron
cd ../../..

# fix check_MailScanner.cron

cd mailscanner/bin/cron
echo "-> Modifying check_MailScanner.cron for use with CSW ..." | tee -a $LOG
sed 's/^LOCKFILE=\/var\/lock\/check_Mailscanner.lock/LOCKFILE=\/opt\/csw\/mailscanner\/var\/check_MailScanner.lock/;s/^MS_LOCKFILE=\/var\/lock\/subsys\/MailScanner.off/MS_LOCKFILE=\/opt\/csw\/mailscanner\/var\/MailScanner.off/' check_MailScanner.cron > check_MailScanner.cron.tmp
mv check_MailScanner.cron.tmp check_MailScanner.cron
cd ../../..

# fix clamav-wrapper

cd mailscanner/lib
echo "-> Modifying clamav-wrapper for use with CSW ..." | tee -a $LOG
# disable tgz and deb, enable unrar
sed 's/^ExtraScanOptions=\"\$ExtraScanOptions --tgz/#ExtraScanOptions=\"\$ExtraScanOptions --tgz/;s/^ExtraScanOptions=\"\$ExtraScanOptions --deb/#ExtraScanOptions=\"\$ExtraScanOptions --deb/;s/^#ExtraScanOptions=\"\$ExtraScanOptions --unrar=\/path\/to\/unrar\"/ExtraScanOptions=\"\$ExtraScanOptions --unrar=\/opt\/csw\/bin\/unrar"/' clamav-wrapper > clamav-wrapper.tmp
mv clamav-wrapper.tmp clamav-wrapper
cd ../..

# change syslog socket

cd mailscanner/lib
find . -type f | xargs grep "setlogsock('unix')" | awk -F':' '{print $1}' | sort | uniq > $LOGDIR/syslogsocketfix
echo "-> Fixing syslog socket type in `wc -l $LOGDIR/syslogsocketfix | awk '{print $1}'` files ..." | tee -a $LOG
for i in `cat $LOGDIR/syslogsocketfix`
do
  echo "---> Fixing syslog socket type in $i ..." >> $LOG
  sed "/Sys::Syslog::setlogsock/s/unix/$SLTYPE/" $i > $i.tmp
  mv $i.tmp $i
done
cd ../..

# change awk to gawk in SA.pm

cd mailscanner/lib/MailScanner
echo "-> Changing awk to gawk in SA.pm ..." | tee -a $LOG
patch SA.pm < $LOGDIR/SA.pm.patch > /dev/null 2>&1
cd ../../..

# change MailScanner path (/opt/MailScanner to /opt/csw/mailscanner)

cd mailscanner
find . -type f | egrep -v 'INSTALL.FreeBSD|INSTALL.OpenBSD' | xargs grep "/opt/MailScanner" | awk -F':' '{print $1}' | sort | uniq > $LOGDIR/mspathfix
echo "-> Fixing MailScanner path in `wc -l $LOGDIR/mspathfix | awk '{print $1}'` files ..." | tee -a $LOG
for i in `cat $LOGDIR/mspathfix`
do
  echo "---> Fixing MailScanner path in $i ..." >> $LOG
  sed 's/\/opt\/MailScanner/\/opt\/csw\/mailscanner/g' $i > $i.tmp
  mv $i.tmp $i
done
cd ..

# fix ownership/permissions

cd mailscanner
echo "-> Fixing permissions ..." | tee -a $LOG
chmod 644 COPYING INSTALL.FreeBSD INSTALL.OpenBSD MailScanner.conf.index.html README
find bin | xargs chmod 755
find etc -type f |xargs chmod 644
find lib/MailScanner -type f |xargs chmod 644
find var -type f |xargs chmod 644
find www -type f |xargs chmod 644
chmod 755 bin bin/cron etc etc/mcp etc/reports etc/reports/* etc/rules lib lib/* lib/MailScanner/CustomFunctions var www
cd ..

# remove bak files in reports

cd mailscanner/etc/reports
find . -type f -name "*.bak" > $LOGDIR/bakfiles
echo "-> Removing `wc -l $LOGDIR/bakfiles | awk '{print $1}'` .bak files in reports ..." | tee -a $LOG
for i in `cat $LOGDIR/bakfiles`
do
  echo "---> Removing $i ..." >> $LOG
  rm $i
done
cd ../../..

# remove unnecessary files

cd mailscanner
echo "-> Removing unnecessary files ..." | tee -a $LOG
for i in INSTALL.FreeBSD INSTALL.OpenBSD MailScanner.conf.index.html svn-commit.tmp bin/Sophos.install bin/Sophos.install.linux bin/tnef.solaris.x86 bin/check_mailscanner.tru64
do
  echo "---> Removing $i ..." >> $LOG
  rm -f $i
done
cd ..

# add files to etc dir

echo "-> Adding files to etc dir ..." | tee -a $LOG
cd mailscanner/etc
cp $LOGDIR/MailScanner .
cd ../..

# fix conf files, add .CSW

cd mailscanner/etc
find . -type f | egrep -v -i 'example|readme|.CSW$' > $LOGDIR/conffiles
echo "-> Adding .CSW to `wc -l $LOGDIR/conffiles | awk '{print $1}'` configurable files ..." | tee -a $LOG
for i in `cat $LOGDIR/conffiles`
do
  echo "---> Adding .CSW to $i ..." >> $LOG
  mv $i ${i}.CSW
done
cd ../..

# add CSW files to doc dir, also move MS doc files there

echo "-> Adding files to doc dir ..." | tee -a $LOG
mkdir -p share/doc/mailscanner
cd share/doc/mailscanner
cp $LOGDIR/conffiles .
cp $LOGDIR/README.CSW .
cp $LOGDIR/history .
cp $LOGDIR/cswmailscanner .
cp $LOGDIR/cswmailscanner.sendmail .
cp $LOGDIR/mailscanner.xml .
cp $LOGDIR/mailscanner.sendmail.xml .
mv ../../../mailscanner/README .
mv ../../../mailscanner/ChangeLog .
mv ../../../mailscanner/COPYING license
cd ../../..

# create prototype

echo "-> Creating prototype ..." | tee -a $LOG
find mailscanner | pkgproto | grep -v prototype.find > prototype.find
cat $LOGDIR/prototype.stub prototype.find > prototype.combined
sed 's/bonivart csw/root bin/' prototype.combined > prototype
rm prototype.find prototype.combined

# add pstamp

pstamp=`uname -n``date +%Y%m%d%H%M%S`

# fix pkginfo

echo "-> Creating pkginfo ..." | tee -a $LOG
cp $LOGDIR/pkginfo.stub pkginfo
echo "VERSION=$version.$rev$cswrev" >> pkginfo
echo "PSTAMP=$pstamp" >> pkginfo

# add symlinks to pkg build files

echo "-> Adding symlinks to package build files ..." | tee -a $LOG
cp $PKGDIR/copyright .
ln -s $LOGDIR/depend depend
ln -s $LOGDIR/postinstall postinstall
#ln -s $LOGDIR/postremove postremove	# not used at the moment
#ln -s $LOGDIR/preinstall preinstall	# not used at the moment
ln -s $LOGDIR/preremove preremove
ln -s $LOGDIR/checkinstall checkinstall
ln -s $LOGDIR/i.smfyes i.smfyes
ln -s $LOGDIR/i.smfno i.smfno
ln -s $LOGDIR/space space

# pkgmk

echo "-> Making package ..." | tee -a $LOG
pkgmk -r `pwd` 2>> $LOG

# pkgtrans

echo "-> Translating package ..." | tee -a $LOG
cd /var/spool/pkg
pkg=mailscanner-$version.$rev$cswrev-SunOS5.9-all-CSW.pkg
pkgtrans -s `pwd` $LOGDIR/$pkg CSWmailscanner 2>> $LOG

# gzip

echo "-> Compressing package ..." | tee -a $LOG
cd $LOGDIR
gzip $pkg

# copy to /home/experimental/bonivart

echo "-> Copying package to /home/experimental/bonivart ..." | tee -a $LOG
cp $pkg.gz $TESTDIR/

# cleaning up

echo "-> Cleaning up spool dir ..." | tee -a $LOG
rm -rf /var/spool/pkg/CSWmailscanner
echo "-> Cleaning up build dir ..." | tee -a $LOG
cd $BUILDDIR/MailScanner-install-$version
rm -rf perl-tar CheckModuleVersion install.*

# copy pkginfo and prototype to pkg dir

echo "-> Copying pkginfo and prototype to log dir ..." | tee -a $LOG
cp $BUILDDIR/MailScanner-install-$version/pkginfo $LOGDIR
cp $BUILDDIR/MailScanner-install-$version/prototype $LOGDIR

# exiting

echo "-> Exiting build script ..." | tee -a $LOG
exit 0
