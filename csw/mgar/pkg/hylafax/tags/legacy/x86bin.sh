#!/bin/sh
#
# so we don't have to do the whole convoluted install again we take care of the
# I386 binaries here.
#
# execute at the source root
#
STAGE=$PWD/cswstage

BINS="/opt/csw/bin/faxalter /opt/csw/bin/faxcover /opt/csw/bin/faxmail /opt/csw/bin/faxrm /opt/csw/bin/faxstat /opt/csw/bin/sendfax /opt/csw/bin/sendpage"

SBINS="/opt/csw/sbin/textfmt /opt/csw/sbin/faxmsg /opt/csw/sbin/faxadduser /opt/csw/sbin/faxconfig /opt/csw/sbin/faxdeluser /opt/csw/sbin/faxmodem /opt/csw/sbin/faxstate /opt/csw/sbin/faxwatch /opt/csw/sbin/faxinfo /opt/csw/sbin/tiffcheck /opt/csw/sbin/dialtest /opt/csw/sbin/typetest /opt/csw/sbin/faxq /opt/csw/sbin/faxqclean /opt/csw/sbin/faxgetty /opt/csw/sbin/faxsend /opt/csw/sbin/pagesend /opt/csw/sbin/tsitest /opt/csw/sbin/tagtest /opt/csw/sbin/cqtest /opt/csw/sbin/choptest /opt/csw/sbin/hfaxd /opt/csw/sbin/lockname /opt/csw/sbin/ondelay"

HLINKS="/opt/csw/sbin/faxabort /opt/csw/sbin/faxanswer /opt/csw/sbin/faxquit /opt/csw/sbin/faxlock"


APX="/opt/csw/share/hylafax/cgi-bin/man2html /opt/csw/share/hylafax/cgi-bin/unquote"

for ii in $BINS $SBINS $APX
do
name=`basename $ii`
x86=`find . -type f -name $name |grep -v cswstage`
cp -f $x86 $STAGE/$ii
strip $STAGE/$ii
done

for ii in $HLINKS
do
name=`basename $ii`
cd $STAGE/opt/csw/sbin/
[ -f $name ] && rm $name
ln faxmsg $name
done
