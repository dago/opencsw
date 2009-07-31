#!/bin/sh
# 2007-12-09 Initial version created from old CSWsendmail Postinstall script
#

# Make backup of Sun sendmail files
# /usr/sbin/newaliases or /usr/bin/newaliases
    if /bin/test ! -L /usr/sbin/newaliases.OFF && /bin/test -L /usr/sbin/newaliases ; then
        echo "Moving /usr/sbin/newaliases to newaliases.OFF"
        mv /usr/sbin/newaliases /usr/sbin/newaliases.OFF
    fi
    if /bin/test ! -L /usr/bin/newaliases.OFF && /bin/test -L /usr/bin/newaliases ; then
        echo "Moving /usr/bin/newaliases to newaliases.OFF"
        mv /usr/bin/newaliases /usr/bin/newaliases.OFF
    fi
# /usr/bin/mailq. In Solaris 8, mailq is a file.  In Solaris 9,
#    mailq is a symlink.  In CSW sendmail, mailq is symlink.
    if /bin/test ! -f /usr/bin/mailq.OFF && /bin/test -f /usr/bin/mailq ; then
        echo "Moving /usr/bin/mailq to mailq.OFF"
        mv /usr/bin/mailq /usr/bin/mailq.OFF
    fi
    if /bin/test ! -L /usr/bin/mailq.OFF && /bin/test -L /usr/bin/mailq ; then
        echo "Moving /usr/bin/mailq to mailq.OFF"
        mv /usr/bin/mailq /usr/bin/mailq.OFF
    fi
# /usr/bin/vacation
    if /bin/test ! -f /usr/bin/vacation.OFF && /bin/test -f /usr/bin/vacation ; then
        echo "Moving /usr/bin/vacation to vacation.OFF"
        mv /usr/bin/vacation /usr/bin/vacation.OFF
    fi
# /usr/bin/mailstats
    if /bin/test ! -f /usr/bin/mailstats.OFF && /bin/test -f /usr/bin/mailstats ; then
        echo "Moving /usr/bin/mailstats to mailstats.OFF"
        mv /usr/bin/mailstats /usr/bin/mailstats.OFF
    fi
# /usr/sbin/makemap
    if /bin/test ! -f /usr/sbin/makemap.OFF && /bin/test -f /usr/sbin/makemap ; then
        echo "Moving /usr/sbin/makemap to makemap.OFF"
        mv /usr/sbin/makemap /usr/sbin/makemap.OFF
    fi
# /usr/bin/praliases
    if /bin/test ! -f /usr/bin/praliases.OFF && /bin/test -f /usr/bin/praliases ; then
        echo "Moving /usr/bin/praliases to praliases.OFF"
        mv /usr/bin/praliases /usr/bin/praliases.OFF
    fi
# /usr/lib/smrsh
    if /bin/test ! -f /usr/lib/smrsh.OFF && /bin/test -f /usr/lib/smrsh ; then
        echo "Moving /usr/lib/smrsh to smrsh.OFF"
        mv /usr/lib/smrsh /usr/lib/smrsh.OFF
    fi
# /usr/lib/mail.local
    if /bin/test ! -f /usr/lib/mail.local.OFF && /bin/test -f /usr/lib/mail.local ; then
        echo "Moving /usr/lib/mail.local to mail.local.OFF"
        mv /usr/lib/mail.local /usr/lib/mail.local.OFF
    fi
# /etc/mail/sendmail.cf
    if /bin/test ! -f /etc/mail/sendmail.cf.OFF && /bin/test -f /etc/mail/sendmail.cf ; then
        echo "Moving /etc/mail/sendmail.cf to sendmail.cf.OFF"
        mv /etc/mail/sendmail.cf /etc/mail/sendmail.cf.OFF
    fi
# /usr/lib/sendmail
    if /bin/test ! -f /usr/lib/sendmail.OFF && /bin/test -f /usr/lib/sendmail ; then
        echo "Moving /usr/lib/sendmail to sendmail.OFF"
        mv /usr/lib/sendmail /usr/lib/sendmail.OFF
    fi
#
    echo "Making symbolic links in /usr for CSWsendmail files."
    if /bin/test -L /usr/bin/newaliases.OFF ; then
        echo "Making symlink /usr/bin/newaliases"
        ln -s /opt/csw/lib/sendmail /usr/bin/newaliases
    fi
    if /bin/test -L /usr/sbin/newaliases.OFF ; then
        echo "Making symlink /usr/sbin/newaliases"
        ln -s /opt/csw/lib/sendmail /usr/sbin/newaliases
    fi
    if /bin/test ! -L /usr/bin/mailq ; then
        echo "Making symlink /usr/bin/mailq"
        ln -s /opt/csw/lib/sendmail /usr/bin/mailq
    fi
    if /bin/test ! -L /usr/bin/vacation ; then
        echo "Making symlink /usr/bin/vacation"
        ln -s /opt/csw/bin/vacation /usr/bin/vacation
    fi
    if /bin/test ! -L /usr/bin/mailstats ; then
        echo "Making symlink /usr/bin/mailstats"
        ln -s /opt/csw/sbin/mailstats /usr/bin/mailstats
    fi
    if /bin/test ! -L /usr/sbin/makemap ; then
        echo "Making symlink /usr/sbin/makemap"
        ln -s /opt/csw/sbin/makemap /usr/sbin/makemap
    fi
    if /bin/test ! -L /usr/bin/praliases ; then
        echo "Making symlink /usr/bin/praliases"
        ln -s /opt/csw/sbin/praliases /usr/bin/praliases
    fi
    if /bin/test ! -L /usr/lib/smrsh ; then
        echo "Making symlink /usr/lib/smrsh"
        ln -s /opt/csw/lib/smrsh /usr/lib/smrsh
    fi
    if /bin/test ! -L /usr/lib/mail.local ; then
        echo "Making symlink /usr/lib/mail.local"
        ln -s /opt/csw/lib/mail.local /usr/lib/mail.local
    fi
    if /bin/test ! -L /usr/lib/sendmail ; then
        echo "Making symlink /usr/lib/sendmail"
        ln -s /opt/csw/lib/sendmail /usr/lib/sendmail
    fi
