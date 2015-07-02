NAME = rsyslog
VERSION = 8.11.0
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Enhanced multi-threaded syslogd with a focus on security and reliability
define BLURB
  Enhanced multi-threaded syslogd with a focus on security and reliability
endef

MAwww.rsyslog.com/files/download/rsyslog/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswrsyslogd.xml
DISTFILES += rsyslog.conf

# Use patch from
#   0001-Forward-port-patch-from-pkgsrc.patch
# until this is fixed:
#   https://github.com/rsyslog/rsyslog/issues/417
PATCHFILES += 0001-Forward-port-patch-from-pkgsrc.patch

BUILD_DEP_PKGS += CSWlibestr-dev
BUILD_DEP_PKGS += CSWlibjson-c-dev
BUILD_DEP_PKGS += CSWlibrelp-dev
BUILD_DEP_PKGS += CSWliblogging-dev

RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibz1
RUNTIME_DEP_PKGS_CSWrsyslog += CSWliblogging-stdlog0
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibuuid1
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibestr0
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibgcrypt20
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibjson-c3
RUNTIME_DEP_PKGS_CSWrsyslog += CSWliblognorm2
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibdbi1
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibnet1
RUNTIME_DEP_PKGS_CSWrsyslog += CSWliblogging-rfc3195-0
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibrelp0
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibgnutls28

# This is the SMF DTD
CHECKPKG_OVERRIDES_CSWrsyslog += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswrsyslogd.xml

GARCOMPILER = GNU

# We need libnet. See for details
#   http://wiki.opencsw.org/project-libnet
EXTRA_LDFLAGS = -L$(libdir)/libnet-new

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-imsolaris

CONFIGURE_ARGS += --enable-imfile
CONFIGURE_ARGS += --enable-impstats

# imptcp requires epoll which Solaris does not have
# CONFIGURE_ARGS += --enable-imptcp

CONFIGURE_ARGS += --enable-libdbi
CONFIGURE_ARGS += --enable-elasticsearch
CONFIGURE_ARGS += --enable-gnutls
CONFIGURE_ARGS += --enable-mail
CONFIGURE_ARGS += --enable-mmnormalize
CONFIGURE_ARGS += --enable-mmjsonparse
CONFIGURE_ARGS += --enable-mmaudit
CONFIGURE_ARGS += --enable-mmanon
CONFIGURE_ARGS += --enable-mmutf8fix
CONFIGURE_ARGS += --enable-mmcount
CONFIGURE_ARGS += --enable-mmsequence
CONFIGURE_ARGS += --enable-mmfields
CONFIGURE_ARGS += --enable-mmpstrucdata
CONFIGURE_ARGS += --enable-mmrfc5424addhmac

CONFIGURE_ARGS += --enable-relp
CONFIGURE_ARGS += --enable-rfc3195
CONFIGURE_ARGS += --enable-omprog
CONFIGURE_ARGS += --enable-omudpspoof
CONFIGURE_ARGS += --enable-omstdout

# This is SystemD Journal, we don't have that on Solaris
# CONFIGURE_ARGS += --enable-omjournal

CONFIGURE_ARGS += --enable-pmlastmsg
CONFIGURE_ARGS += --enable-pmcisconames
CONFIGURE_ARGS += --enable-pmciscoios
CONFIGURE_ARGS += --enable-pmsnare
CONFIGURE_ARGS += --enable-omruleset
CONFIGURE_ARGS += --enable-omuxsock
CONFIGURE_ARGS += --enable-mmsnmptrapd

# CONFIGURE_ARGS += --enable-omhdfs
# CONFIGURE_ARGS += --enable-omkafka
# CONFIGURE_ARGS += --enable-ommongodb
# CONFIGURE_ARGS += --enable-imzmq3
# CONFIGURE_ARGS += --enable-imczmq
# CONFIGURE_ARGS += --enable-omzmq3
# CONFIGURE_ARGS += --enable-omczmq
# CONFIGURE_ARGS += --enable-omrabbitmq
# CONFIGURE_ARGS += --enable-omhiredis
# CONFIGURE_ARGS += --enable-omhttpfs
CONFIGURE_ARGS += --enable-generate-man-pages

EXTRA_CPPFLAGS += -D_PATH_LOGCONF=\\\"$(sysconfdir)/rsyslog.conf\\\"

PRESERVECONF += $(sysconfdir)/rsyslog.conf

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswrsyslogd.xml
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

post-install-modulated:
	gated:
	/opt/csw/gnu/install -D -m 644 $(WORKDIR)/rsyslog.conf $(DESTDIR)/etc/opginstall -D -m 0644 $(WORKDIR)/cswrsyslogd.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswrsyslogd.xml
	@$(MAKECOOKIE)
