#!/bin/sh
# 2007-12-09  Initial version created from the old CSWsendmail preremove script
#
# Remove the symlinks for using CSWsendmail and return filesystem to
# using Sun's sendmail.

# Remove the symlinks to CSW files
    echo "Removing the symlinks to CSW files."
# /usr/bin/newaliases or /usr/sbin/newaliases
    if /bin/test -L /usr/bin/newaliases ; then rm -f /usr/bin/newaliases ; fi
    if /bin/test -L /usr/sbin/newaliases ; then rm -f /usr/sbin/newaliases ; fi
# /usr/bin/mailq.  mailq is either a symlink or a file, depending
#   on the version of Solaris
    if /bin/test -L /usr/bin/mailq ; then rm -f /usr/bin/mailq ; fi
# /usr/bin/vacation
    if /bin/test -L /usr/bin/vacation  ; then rm -f /usr/bin/vacation ; fi
# /usr/bin/mailstats
    if /bin/test -L /usr/bin/mailstats ; then rm -f /usr/bin/mailstats ; fi
# /usr/sbin/makemap
    if /bin/test -L /usr/sbin/makemap ; then rm -f /usr/sbin/makemap ; fi
# /usr/bin/praliases
    if /bin/test -L /usr/bin/praliases ; then rm -f /usr/bin/praliases ; fi
# /usr/lib/smrsh
    if /bin/test -L /usr/lib/smrsh ; then rm -f /usr/lib/smrsh ; fi
# /usr/lib/mail.local
    if /bin/test -L /usr/lib/mail.local ; then rm -f /usr/lib/mail.local ; fi
# /usr/lib/sendmail
    if /bin/test -L /usr/lib/sendmail ; then rm -f /usr/lib/sendmail ; fi
#
    echo "Symlinks to CSW files removed."
#
# Return to Sun files
# /usr/bin/newaliases or /usr/sbin/newaliases
    if /bin/test -L /usr/bin/newaliases.OFF ; then 
        mv -f /usr/bin/newaliases.OFF /usr/bin/newaliases
    fi
    if /bin/test -L /usr/sbin/newaliases.OFF ; then 
        mv -f /usr/sbin/newaliases.OFF /usr/sbin/newaliases
    fi
    if /bin/test -L /usr/bin/mailq.OFF || /bin/test -f /usr/bin/mailq.OFF ; then
        mv -f /usr/bin/mailq.OFF /usr/bin/mailq
    fi
# /usr/bin/vacation
    if /bin/test -f /usr/bin/vacation.OFF ; then
        mv -f /usr/bin/vacation.OFF /usr/bin/vacation
    fi
# /usr/bin/mailstats
    if /bin/test -f /usr/bin/mailstats.OFF ; then
        mv -f /usr/bin/mailstats.OFF /usr/bin/mailstats
    fi
# /usr/sbin/makemap
    if /bin/test -f /usr/sbin/makemap.OFF ; then
        mv -f /usr/sbin/makemap.OFF /usr/sbin/makemap
    fi
# /usr/bin/praliases
    if /bin/test -f /usr/bin/praliases.OFF ; then
        mv -f /usr/bin/praliases.OFF /usr/bin/praliases
    fi
# /usr/lib/smrsh
    if /bin/test -f /usr/lib/smrsh.OFF ; then
        mv -f /usr/lib/smrsh.OFF /usr/lib/smrsh
    fi
# /usr/lib/mail.local
    if /bin/test -f /usr/lib/mail.local.OFF ; then
        mv -f /usr/lib/mail.local.OFF /usr/lib/mail.local
    fi
# /usr/lib/sendmail
    if /bin/test -f /usr/lib/sendmail.OFF ; then
        mv -f /usr/lib/sendmail.OFF /usr/lib/sendmail
    fi
# /etc/mail/sendmail.cf
    if /bin/test -f /etc/mail/sendmail.cf.OFF ; then
        mv -f /etc/mail/sendmail.cf.OFF /etc/mail/sendmail.cf
    fi
    echo "Sun sendmail files restored."
