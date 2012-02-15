VERSIONID(`$Id: sendmail.mc,v 1.1 2012/02/15 15:19:30 bonivart Exp $')
OSTYPE(`solaris9csw')
DOMAIN(`generic')
define(`SMART_HOST',`smarthost.mydomain.com')
define(`STATUS_FILE',`/etc/opt/csw/mail/statistics')
define(`MAIL_SETTINGS_DIR',`/etc/opt/csw/mail/')
FEATURE(`mailertable', `hash -o /etc/opt/csw/mail/mailertable')
FEATURE(`genericstable', `hash -o /etc/opt/csw/mail/genericstable')
FEATURE(`access_db', `hash -T<TMPF> /etc/opt/csw/mail/access')
FEATURE(`virtusertable', `hash /etc/opt/csw/mail/virtusertable')
dnl Enable if you have installed CSWspamass-milter
dnl FEATURE(`spamass-milter')dnl
dnl Enable if you have installed CSWmiltergreylist
dnl Copy /opt/csw/share/doc/miltergreylist/milter-greylist.m4
dnl to /opt/csw/share/sendmail/cf/feature/milter-greylist.m4
dnl FEATURE(`milter-greylist')
MASQUERADE_AS(`mydomain.com')
MASQUERADE_DOMAIN(`mydomain.com')
FEATURE(`masquerade_entire_domain')
FEATURE(`masquerade_envelope')
define(`confSMTP_LOGIN_MSG', `$j server ready at $b')
define(`confTO_IDENT', `0')
define(`confBIND_OPTS', `WorkAroundBrokenAAAA')
MAILER(`local')dnl
MAILER(`smtp')dnl
