# Squid 3
# $Id$
#
NAME = squid
VERSION = 3.5.59]\).*\.[0-9]*/\1/')
GARTYPE = v2

DESCRIPTION = High performance Web proxy cache
define BLURB
  Squid is a high performance Web proxy cache that can be arranged
  hierarchically for an improvement in response times and a reduction in
  bandwith usage. Squid runs on all popular Unix and WindowV1 = $(shell echo $(VERSION) | cut -d. -f1)
V12 = $(shell echo $(VERSION) | cut -d. -f1,2)
MASTER_SITES = http://www.squid-cache.org/Versions/v$(V1)/$(V12)/
DISTFILES += $(DISTNAME).tar.bz2

# ssl_crtd fails to build on OpenSolaris/OpenIndiana/Solaris 11
# From http://bugs.squid-cache.org/show_bug.cgi?id=3664
#PATCHFILES += bug3664.patch

# configure doesnt detect IPFilter 5.1.2 system headers
# From http://bugs.squid-cache.org/show_bug.cgi?id=3754
#PATCHFILES += solaris10_fix_bug3754_mk3.patch

# Squid 3.4.5 crashes when adaptation_access is used
# From http://bugs.squid-cache.org/show_bug.cgi?id=4057
#PATCHFILES += bug4057.patch

PACKAGES = CSWsquid
RUNTIME_DEP_PKGS_CSWsquid += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsquid += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsquid += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWsquid += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWsquid += CSWperl
RUNTIME_DEP_PKGS_CSWsquid += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsquid += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWsquid += CSWlibssl1-0-0
#RUNTIME_DEP_PKGS_CSWsquid += CSWbdb48
RUNTIME_DEP_PKGS_CSWsquid += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsquid += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWsquid += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWsquid += CSWlibnettle4
RUNTIME_DEP_PKGS_CSWsquid += CSWlibgnutls28

# Linker anomaly
CHECKPKG_OVERRIDES_CSWsquid += surplus-dependency|CSWlibintl8

PACKAGING_PLATFORMS =  solaris10-sparc solaris10-i386

INITSMF += /etc/opt/csw/init.d/csw$(NAME)
PRESERVECONF += /etc/opt/csw/$(NAME)/cachemgr.conf
PRESERVECONF += /etc/opt/csw/$(NAME)/squid.conf
PRESERVECONF += /etc/opt/csw/$(NAME)/mime.conf
PRESERVECONF += /etc/opt/csw/$(NAME)/msntauthopt/csPRESERVECONF += /etc/opt/csw/$(NAME)/errorpage.csssw/$(NAME)/mime.conf

MIGRATE_SOURCE_DIR = /opt/csw/etc
MIGRATE_DEST_DIR = /etc/opt/csw/$(NAME)
MIGRATE_FILES  = cachemgr.conf
MIGRATE_FILES += mime.conf
MIGRATE_F# ./configure '--prefix=/usr/local/squid' '--enable-translation' '--enable-external-acl-helpers=file_userip' '--enable-icap-client' '--enable-ipf-transparent' '--enable-storeio=diskd' '--enable-removal-policies=lru,heap' '--enable-devpoll' '--disable-wccp' '--enable-wccpv2' '--enable-http-violations' '--enable-follow-x-forwarded-for' '--enable-arp-acl' '--enable-htcp' '--enable-cache-digests' '--with-dl' '--enable-auth-negotiate=none' '--disable-auth-digest' '--disable-auth-ntlm' '--enable-auth-basic' '--enable-storeid-rewrite-helpers=file' '--enable-log-daemon-helpers=file' '--enable-ssl' '--enable-ssl-crtd' '--enable-zph-qos' '--with-filedescriptors=131072' '--disable-snmp' '--enable-inline' '--with-build-environment=POSIX_V6_LP64_OFF64' 'CFLAGS=-O3 -m64 -fPIE -fstack-protector -mtune=core2 --param=ssp-buffer-size=4 -pipe' 'CXXFLAGS=-O3 -m64 -fPIE -fstack-protector -mtune=core2 --param=ssp-buffer-size=4 -pipe' 'CPPFLAGS=-I/opt/csw/include' 'LDFLAGS=-fPIE -pie -Wl,-z,now' --enable-build-info="Intercept/WCCPv2/SSL/CRTD/DISKD/64/GCC Production"_FCONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/$(NAME)onfdir=${sysconfdir}
CONFIGURE_ARGS += --datadir=$(datadir)/$(NAME)
CONFIGURE_ARGS += --docdir=$(datadir)/$(NAME)
CONFIGURE_ARGS += --localstatedir=/var/$(prefix)/$(NAME)
CONFIGURE_ARGS += --libexecdir=$(prefix)/libexec/$(NAME)
CONFIGURE_ARGS #+= --enable-arp-acl
CONFIGURE_ARGS += --enable-auth=basic,ntlm,digest,negotiate
CONFIGUauthtlm,digest,negotiate
CONFIGURE_ARGS += --enable-basic-auth-helpers=LDAP,SMB,YP,PAM,SASL,NCSA
CONFIGURE_ARGS += --enable-cache-digests
CONFIGURE_ARGS += --enable-carp
CONFIGURE_ARGS += --enable-delay-pools
CONFIGUexternal-acl-helpers=file_userip--enable-delay-pools
CONFIGURE_ARGS += --enable-forw-via-db
CONFIGURE_ARGS += --enable-htcp
CONFIGUhttp-violations
CONFIGURE_ARGS += --enable-follow-x-forwarded-for
CONFIGURE_ARGS += --enable-inlineRGS += --enable-htcp
CONFIGURE_ARGS += --enable-large-cache-files
CONFIGURE_ARGS += --enable-referer-log
CONFIGURE_ARGS += --enable-remova# Use devpoll in favor of select as it is much faster
CONFIGURE_ARGS += --enable-devpollS += --enable-select
CONFIGURE_ARGS += --enable-snmp
CONFIGURE_ARGS += --enable-ssl
CONFIGUssl-crtdARGS += --enable-ssl
CONFIGURE_ARGS += --enable-useragent-log
CONFIGURE_ARGS += --enable-ipf-transparent
CONFIGURE_ARGS += --enable-icap-client
enable-zph-qos--enable-icap-client
CONFIGURE_ARGS += --disable-ident-lookups
CONFIGURE_ARGS += --disable-icmp
CONFIGURE_ARGS += --with-dl
CONFIGURE_ARGS += --with-large-files
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-dCONFIGURE_ARGS += --with-filedescriptors=131072dCONFIGURE_ARGS += --enable-aio
CONFIGURE_ARGS += --enable-storeio=ufs,diskddCONFIGURE_ARGS += --enable-storeid-rewrite-helpers=file
CONFIGURE_ARGS += --enable-log-daemon-helpers=filed# These are needed for Cisco integration, as requested by email
CONFIGURE_ARGS += --enable-wccp
CONFIGURE_ARGS += --enable-wccpv2d
# Native instructions need to be disabled for zones as reported in #5221
# This is described in detail in
#   http://wiki.squid-cache.org/KnowledgeBase/IllegalInstructionError
CONFIGURE_ARGS += --disable-arch-nativedefault-user=$(NAME)

# Allowed values (see configure --help):
#   POSIX_V6_ILP32_OFF32   32 bits
#   POSIX_V6_ILP32_OFFBIG  32 bits with large file support
#   POSIX_V6_LP64_OFF64    64 bits
#   POSIX_V6_LPBIG_OFFBIG  large pointers and files
#   XBS5_ILP32_OFF32       32 bits (legacy)
#   XBS5_ILP32_OFFBIG      32 bits with large file support (legacy)
#   XBS5_LP64_OFF64        64 bits (legacy)
#   XBS5_LPBIG_OFFBIG      large pointers and files (legacy)
#   default                The default for your OS

BUILD_ENVIRONMENT-32 = POSIX_V6_ILP32_OFFBIG
BUILD_ENVIRONMENT-64 = POSIX_V6_LPBIG_OFFBIG

CONFIGURE_ARGS += --with-build-environment=$(BUILD_ENVIRONMEEXTRA_CPPFLAGS += -DDEFAULT_SQUID_CONF=\\\"$(sysconfdir)/$(NAME)/squid.conf\\\"

# /opt/csw/bdb48/include/db_185.h needs slightly different type names than from sys/types.h
EXTRA_CPPFLAGS += -Du_int32_t=uint32_t -Du_int16_t=uint16_t

# Expose deprecated krb5 API as krb5_get_in_tkt_with_keytab is used in helpers/external_acl/kerberos_ldap_group/support_krb5.cc
# Add #defines.patch

# Use patch until this is fixed:
#   http://bugs.squid-cache.4025
EXTRA_CPPFLAGS += -DKRB5_DEPRECATED=1
CONFIGURE_ARGS += --disable-strict-error-checkingME# configure tests with 'id -u' and expects a uidnumber
CONFIGURE_ENV_PATH = /usr/xpg4/bin:$(PATH)MENT-$(MEMORYMODEL))

GARCOMPILER = GNU

EXTRA_LIB += $(prefix)/bdb48/lib
EXTRA_INC += $(prefix)/bdb48/include

# The testsuite requires cppuLECONF += mime.conf
USERGROUP = /etc/opt/csw/pkg/CSW$(NAME)/cswusergroup

PROTOTYPE_MODIFIERS      = varuser
PROTOTYPE_FILES_varuser  = \/var\/opt\/csw\/$(NAME)\/cache
PROTOTYPE_FILES_varuser += \/var\/opt\/csw\/$(NAME)\/logs
PROTOTYPE_CLASS_varuser  = ugfiles
PROTOTYPE_USER_varuser   = $(NAME)
PROTOTYPE_GROUP_varuser  = $(NAME)

REINPLACE_USRLOCAL = $(mandir)/man8/squid_session.8
REINPLACE_WHEN_USRLREINPLACEMENTS += conf
REINPLACE_MATCH_conf = /usr/local/squid/etc/
REINPLACE_WITH_conf = $(sysconfdir)/$(NAME)/
REINPLACE_FILES_conf += helpers/basic_auth/MSNT/msntauth.conf.default

EXTRA_MERGE_EXCLUDE_FILES += .*\.default

include gar/category.mk.sh
#	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/logs
	ginstall -d $(DESTDIR)/var/opt/csw/$(NAME)/cache
	ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)
	ginstall -m 755 $(FILEDIR)/cswsquid3 $(DESTDIR)/etc/opt/csw/init.d/csw$(NAME)
	ginstall -m 644 $(FILEDIR)/CSWsquid3.cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSW$(NAME)/cswusergro