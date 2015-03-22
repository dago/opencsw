# $Id$

NAME = syslog-ng
VERSION = 3.6.2
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A powerful syslogd replacement
define BLURB
  Syslog New Generation is a powerful replacement for the standard syslogd. It
  can filter messages based on content using regular expressions and forward
  logs using TCP.
endef

MASTER_SITES = http://www.balabit.com/downloads/files/$(NAME)/open-source-edition/$(VERSION+/source/
DISTFILES  = $(NAME)_$(VERSION).tar.gz
DISTFILES += $(NAME).conf.CSW
DISTFILES += cswsyslog_ng
DISTFILES += CSWsyslog-ng.preinstall
DISTFILES += CSWsyslog-ng.postremove
DISTFILES += CSWsyslog-# Solaris <11 does not contain ntohll, htonll and asprintf
PATCHFILES += 0001-Added-definition-for-htonll-and-ntohll.patch
PATCHFILES += 0002-Add-asprintf.patch

VENDOR_URL = http://www.balabit.com/network-security/syslog-ng/opensource-logging-system/

INITSMF += /etc/opt/csw/init\.d/cswsyslog_ng
PRESERVECONF += $(sysconfdir)/syslog-ng\.conf
PRESERVECONF += $(sysconfdir)/scl\.confsyslog-ng\.conf\.CSW

# Syslog links against glib2, which is packaged in different packages on
# Solaris 9 and Solaris 10. Therefore, we need to build separately on 9 and
# 10, and declare diff# Don't build for Solaris 9f# PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS ACKAGING_PLATFORMS += solaris10-sp# Need XPG4v2 for struct msghdr
EXTRA_CFLAGS += -D_XOPEN_SOURCE=1 -D_XOPEN_SOURCE_EXTENDED=1 -D__EXTENSIONS__
# ...and -XPG6 to allow C99 with the flags above
EXTRA_CFLAGS += -std=gnu99 -D_XPG6
# We need id -u
CONFIGURE_ENV_PATH = /usr/xpg4/bin:$(PATH) spdir = /etc/opt/csw

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-dynamic-linking
CONFIGURE_ARGS += --enable-spoof-source=no
CONFIGURE_ARGS += --enable-tcp-wrapper
CONFIGURE_ARBUILD_ARGS += V=1RGS += --enable-ssl

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
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibdbi1
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibevtlog0
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibpcre1
RUNTIME_DEP_PKGS_CSssl1-0-0og-ng += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWsysloRUNTIME_DEP_PKGS_CSWsyslog-ng += CSWlibintl8

# This is correct, zoneinfo is searched at
#   /usr/share/zoneinfo/
#   /usr/share/lib/zoneinfo/r/share/lib/zoneinfo
CHECKPKG_OVERRIDES_CSWsyslog-ng += file-with-bad-content|/usr/share|root/opt/-3.6.so.0.0.0

# This is optional
CHECKPKG_OVERRIDES_CSWsyslog-ng += missing-dependency|CSWperlog-ng += CSWlibwrap1

# Specifying different dependencies for 5.9 and 5.10.
RUNTIME_DEP_PKGS_CSWsyslog-ng_5.10 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWsyslog-ng_5.10 += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWsyslgthread.10 +=
RUNTIME_DEP_PKGS_CSWsyslog-ng_5.9 += CSWglib2.9 += CSWlibssl0-9-8

RUNTIME_DEP_PKGS_CSWsyslog-ng += $(RUNTIME_DEP_PKGS_CSWsysl# Stub package refers to an older version, we don't need it
# OBSOLETED_BY_CSWsyslog-ng = CSWsyslogng
# og-ng = CSWsyslogng
CATALOGNAME_CSWsyslogng = syslog_ng_stub

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
# RUNTIME_DEP_PKGS_CSWsyslog-ng-dev += slog-ng.so.0.0.0

# Not splitting the syslog-ng libraries.  There are no known packages linking
# to syslog's shared objects.
CHECKPKG_OVERRIDES_CSWsyslog-ng += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWsyslog-ng += shared-l#  Needed on Sparc only
CHECKPKG_OVERRIDES_CSWsyslog-ng += surplus-dependency|CSWlibintl8KEinclude gar/category.mkKER_FLAGS = -lgnutls

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw
	ginstall -m 444 $(WORKDIR)/$(NAME).conf.CSW \
		$(DESTDIR)/etc/opt/csw/$(NAME).conf.CSW
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswsyslog_ng \
		$(DESTDIR)/etc/opt/csw/init.d/cswsyslog_ng
	ginstall -m 755 -d $(DESTDIR)$(localstatedir)/