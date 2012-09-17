NAME = rsyslog
VERSION = 5.8.13
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Enhanced multi-threaded syslogd with a focus on security and reliability
define BLURB
  Enhanced multi-threaded syslogd with a focus on security and reliability
endef

MASTER_SITES = http://rsyslog.com/files/download/rsyslog/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES  += rsyslog.init
DISTFILES  += rsyslog.default
DISTFILES  += rsyslog.conf

RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibz1

GARCOMPILER = GNU

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-imsolaris
EXTRA_CPPFLAGS+= -D_PATH_LOGCONF=\\\"$(sysconfdir)/rsyslog.conf\\\"

CHECKPKG_OVERRIDES_CSWrsyslog += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/rsyslogd.8

INITSMF = /etc/opt/csw/init.d/cswrsyslog

post-install-modulated:
	/opt/csw/gnu/install -D -m 644 $(WORKDIR)/rsyslog.conf $(DESTDIR)/etc/opt/csw/rsyslog.conf
	/opt/csw/gnu/install -D -m 644 $(WORKDIR)/rsyslog.default $(DESTDIR)/etc/opt/csw/default/rsyslog
	/opt/csw/gnu/install -D -m 755 $(WORKDIR)/rsyslog.init $(DESTDIR)/etc/opt/csw/init.d/cswrsyslog

include gar/category.mk
