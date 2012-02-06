divert(-1)
# Sendmail feature for simple integration of spamass-milter
#
# Part of CSWspamass-milter.
#

divert(0)
VERSIONID(`$Id')dnl
divert(-1)

ifdef(`_ARG_',dnl
	define(`__SPAMASS_SOCK__',defn(`_ARG_')),dnl
	define(`__SPAMASS_SOCK__',`/var/run/spamass.sock'))dnl
INPUT_MAIL_FILTER(`spamass-milter', `S=local:'__SPAMASS_SOCK__`, F=, T=C:15m;S:4m;R:4m;E:10m')
define(`confMILTER_MACROS_CONNECT',`t, b, j, _, {daemon_name}, {if_name}, {if_addr}')dnl
define(`confMILTER_MACROS_HELO',`s, {tls_version}, {cipher}, {cipher_bits}, {cert_subject}, {cert_issuer}')dnl
define(`confMILTER_MACROS_ENVRCPT',`r, v, Z')dnl
