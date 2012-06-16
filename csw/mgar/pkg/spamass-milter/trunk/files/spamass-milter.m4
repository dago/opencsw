divert(-1)
dnl Sendmail feature for simple integration of spamass-milter
dnl
dnl Part of CSWspamass-milter.
dnl
dnl
dnl Use it like this in your sendmail.mc file:
dnl
dnl  FEATURE(`spamass-milter')dnl
dnl
dnl This will add the necessary configuration to use spamass-milter. It
dnl expects the spamass-milter socket to be /var/run/spamass.sock.
dnl
dnl If your spamass-milter socket is not at the default location, add
dnl something like
dnl
dnl  FEATURE(`spamass-milter', `<pathtosocket>')dnl
dnl
dnl to your sendmail.mc file. <pathtosocket> is the absolute path to the
dnl spamass-milter socket.
dnl
dnl In any case, the filter will be called `spamass-milter'.
dnl
dnl Direct comments and/or suggestions to raos@opencsw.org.
divert(0)
VERSIONID(`$Id')dnl
ifdef(`_ARG_',dnl
	define(`__SPAMASS_SOCK__',defn(`_ARG_')),dnl
	define(`__SPAMASS_SOCK__',`/var/run/spamass.sock'))dnl
INPUT_MAIL_FILTER(`spamass-milter', `S=local:'__SPAMASS_SOCK__`, F=, T=C:15m;S:4m;R:4m;E:10m')
define(`confMILTER_MACROS_CONNECT',`t, b, j, _, {daemon_name}, {if_name}, {if_addr}')dnl
define(`confMILTER_MACROS_HELO',`s, {tls_version}, {cipher}, {cipher_bits}, {cert_subject}, {cert_issuer}')dnl
define(`confMILTER_MACROS_ENVRCPT',`r, v, Z')dnl
