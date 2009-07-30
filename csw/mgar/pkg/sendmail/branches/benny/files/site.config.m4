dnl adapted site.config.m4 from the REV=2007.12.17 build

dnl ### we are using SUN Studio and OpenCSW
define(`confCC', `%OCSWCC%')
APPENDDEF(`confCCOPTS', `%CFLAGS%')
define(`confEBINDIR',`/opt/csw/lib')
define(`confMANROOT',`/usr/csw/share/man')
define(`confMANROOTMAN',`/usr/csw/share/man')
define(`confMBINDIR',`/opt/csw/bin')
define(`confSBINDIR',`/opt/csw/sbin')
define(`confUBINDIR',`/opt/csw/bin')
define(`confNO_STATISTICS_INSTALL',`True')
define(`confHFDIR', `/opt/csw/share/mail')

dnl ### add OpenCSW lib and include directories
APPENDDEF(`confLIBDIRS', `-L/opt/csw/lib -R/opt/csw/lib')
APPENDDEF(`confINCDIRS', `-I/opt/csw/include')
APPENDDEF(`conf_sendmail_ENVDEF', `-I/opt/csw/include')
dnl we should not need this..
dnl APPENDDEF(`confLIBDIRS', `-L/opt/csw/bdb44/lib -R/opt/csw/bdb44/lib')
dnl APPENDDEF(`confINCDIRS', `-I/opt/csw/bdb44/include')

dnl ### add NIS/NIS+ support
APPENDDEF(`confENVDEF', `-DNIS')
APPENDDEF(`confENVDEF', `-DNISPLUS')

dnl ### add LDAP support
APPENDDEF(`conf_libsm_ENVDEF', `-DLDAPMAP')
APPENDDEF(`conf_sendmail_ENVDEF', `-DLDAPMAP')

dnl ### add SASL support
APPENDDEF(`conf_sendmail_ENVDEF', `-DSASL=2')
APPENDDEF(`conf_sendmail_ENVDEF', `-D_FFR_TLS_1')
APPENDDEF(`conf_sendmail_LIBS', `-lsasl2')

dnl ### add STARTTLS support
APPENDDEF(`confENVDEF',`-DSTARTTLS')
APPENDDEF(`confLIBS', `-lssl -lcrypto')

dnl ### add because they were already compiled in
APPENDDEF(`confENVDEF', `-DSOCKETMAP')
APPENDDEF(`conf_sendmail_ENVDEF', `-DTCPWRAPPERS')
APPENDDEF(`conf_sendmail_LIBS', `-lwrap')"
APPENDDEF(`conf_sendmail_ENVDEF', `-DNETINET6')
APPENDDEF(`conf_libmilter_ENVDEF', `-DNETINET6')
APPENDDEF(`conf_libsm_ENVDEF', `-I/opt/csw/include')
APPENDDEF(`conf_libsm_ENVDEF', `-DLDAPMAP')
APPENDDEF(`conf_libsm_LIBS', `-lldap')
APPENDDEF(`conf_libsm_LIBS', `-llber')
APPENDDEF(`conf_sendmail_ENVDEF', `-DLDAPMAP')
APPENDDEF(`conf_sendmail_LIBS', `-lldap')
APPENDDEF(`conf_sendmail_LIBS', `-llber')
APPENDDEF(`conf_editmap_LIBS', `-lldap')
APPENDDEF(`conf_editmap_LIBS', `-llber')
APPENDDEF(`conf_mail_local_LIBS', `-lldap')
APPENDDEF(`conf_mail_local_LIBS', `-llber')
APPENDDEF(`conf_mailstats_LIBS', `-lldap')
APPENDDEF(`conf_mailstats_LIBS', `-llber')
APPENDDEF(`conf_makemap_LIBS', `-lldap')
APPENDDEF(`conf_makemap_LIBS', `-llber')
APPENDDEF(`conf_praliases_LIBS', `-lldap')
APPENDDEF(`conf_praliases_LIBS', `-llber')
APPENDDEF(`conf_rmail_LIBS', `-lldap')
APPENDDEF(`conf_smrsh_LIBS', `-lldap')
APPENDDEF(`conf_smrsh_LIBS', `-llber')
APPENDDEF(`conf_vacation_LIBS', `-lldap')
APPENDDEF(`conf_vacation_LIBS', `-llber')
APPENDDEF(`conf_libmilter_ENVDEF', `-DMILTER')
APPENDDEF(`conf_sendmail_ENVDEF', `-DMILTER')
APPENDDEF(`conf_sendmail_ENVDEF', `-D_FFR_TLS_1')
APPENDDEF(`conf_libmilter_ENVDEF', `-DSM_CONF_POLL=1')
APPENDDEF(`conf_libmilter_ENVDEF', `-D_FFR_WORKERS_POOL=1')
