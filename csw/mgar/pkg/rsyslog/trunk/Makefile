NAME = rsyslog
VERSION = 5.8.6
CATEGORIES = server

DESCRIPTION = Enhanced multi-threaded syslogd with a focus on security and reliability
define BLURB
  Enhanced multi-threaded syslogd with a focus on security and reliability
endef

MASTER_SITES = http://rsyslog.com/files/download/rsyslog/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWrsyslog += CSWlibz1

GARCOMPILER = GNU

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-imsolaris

CHECKPKG_OVERRIDES_CSWrsyslog += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/rsyslogd.8

include gar/category.mk
