# $Id$

NAME = syslog-ng
VERSION = 3.2.5
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A powerful syslogd replacement
define BLURB
  Syslog New Generation is a powerful replacement for the standard syslogd. It
  can filter messages based on content using regular expressions and forward
  logs using TCP.
endef

MASTER_SITES = http://www.balabit.com/downloads/files/$(NAME)/open-source-edition/$(VERSION)/source/
DISTFILES  = $(NAME)_$(VERSION).tar.gz
DISTFILES += $(NAME).conf.CSW
DISTFILES += cswsyslog_ng
DISTFILES += CSWsyslog-ng.preinstall
DISTFILES += CSWsyslog-ng.postremove
DISTFILES += CSWsyslog-ng.cswreleasenotes

SPKG_SOURCEURL = http://www.balabit.com/network-security/syslog-ng/opensource-logging-system/
INITSMF = /etc/opt/csw/init\.d/cswsyslog_ng
SAMPLECONF = /etc/opt/csw/syslog-ng\.conf\.CSW


# shared /opt/csw support:
localstatedir = /var/opt/csw
sysconfdir = /etc/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic-linking
CONFIGURE_ARGS += --enable-spoof-source=no
CONFIGURE_ARGS += --enable-tcp-wrapper
CONFIGURE_ARGS += --enable-ssl

GARCOMPILER = GNU
TEST_SCRIPTS =

# The configure script finds -lwrap but doesn't actually use it.
# We need to be more pushy.
EXTRA_LDFLAGS = -L/opt/csw/lib -lwrap -lsocket

BUILD_DEP_PKGS  = $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWgcc4core
BUILD_DEP_PKGS += CSWggettext
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWpkgconfig

PACKAGES = CSWsyslog-ng
SPKG_DESC_CSWsyslog-ng = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWglib2
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibdbi1
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibevtlog0
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibwrap1

OBSOLETED_BY_CSWsyslog-ng = CSWsyslogng

# It it were split, it'd look like this:
# PACKAGES += CSWlibsyslog-ng0
# CATALOGNAME_CSWlibsyslog-ng0 = libsyslog_ng0
# PKGFILES_CSWlibsyslog-ng0 += $(call baseisadirs,$(libdir),libsyslog-ng\.so\.0\.0\.0)
# PKGFILES_CSWlibsyslog-ng0 += $(call baseisadirs,$(libdir),libsyslog-ng\.so\.0(\.\d+)*)
# SPKG_DESC_CSWlibsyslog-ng0 += $(DESCRIPTION), libsyslog-ng.so.0
# RUNTIME_DEP_PKGS_CSWlibsyslog-ng0 += CSWlibevtlog0
# RUNTIME_DEP_PKGS_CSWlibsyslog-ng0 += CSWlibintl8
# RUNTIME_DEP_PKGS_CSWlibsyslog-ng0 += CSWlibwrap1
# RUNTIME_DEP_PKGS_CSWlibsyslog-ng0 += CSWlibgnutls26
# RUNTIME_DEP_PKGS_CSWlibsyslog-ng0 += CSWlibgcc-s1
# RUNTIME_DEP_PKGS_CSWlibsyslog-ng0 += CSWlibpcre1
# RUNTIME_DEP_PKGS_CSWlibsyslog-ng0 += CSWglib2
# 
# PACKAGES += CSWsyslog-ng-dev
# CATALOGNAME_CSWsyslog-ng-dev = syslog_ng_dev
# SPKG_DESC_CSWsyslog-ng-dev += $(DESCRIPTION), development files
# PKGFILES_CSWsyslog-ng-dev += /opt/csw/lib/libsyslog-ng.so
# RUNTIME_DEP_PKGS_CSWsyslog-ng-dev += CSWlibsyslog-ng0

# A reference to /usr/share/lib/zoneinfo
CHECKPKG_OVERRIDES_CSWsyslog-ng += file-with-bad-content|/usr/share|root/opt/csw/lib/libsyslog-ng.so.0.0.0

# Not splitting the syslog-ng libraries.  There are no known packages linking
# to syslog's shared objects.
CHECKPKG_OVERRIDES_CSWsyslog-ng += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWsyslog-ng += shared-lib-pkgname-mismatch

# Missing TLS symbols
EXTRA_LINKER_FLAGS = -lgnutls

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw
	ginstall -m 444 $(WORKDIR)/$(NAME).conf.CSW \
		$(DESTDIR)/etc/opt/csw/$(NAME).conf.CSW
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswsyslog_ng \
		$(DESTDIR)/etc/opt/csw/init.d/cswsyslog_ng
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)/run
	@$(MAKECOOKIE)

include gar/category.mk
