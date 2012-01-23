# $Id$
#
# files/README describes that there are two versions of hosts.{allow,deny}
# syntaxes.

NAME = tcp_wrappers
BASEVERSION = 7.6
RELEASE = ipv6.4
VERSION = $(BASEVERSION)-$(RELEASE)
CATEGORIES = lib

DESCRIPTION = Socket wrappers for pre-screening tcp connections (ipv6.4 patched)
define BLURB
  Socket Wrappers is an improved version of tcp_wrappers by Wietse Venema.
endef

MASTER_SITES = http://ftp.porcupine.org/pub/security/
DISTNAME = $(NAME)_$(VERSION)
DISTFILES = $(DISTNAME).tar.gz
DISTFILES += COPYING
DISTFILES += README

PATCHFILES = patch-cflags.diff
PATCHFILES += sharedlib.patch

PACKAGES += CSWtcpwrapper
SPKG_DESC_CSWtcpwrapper = Wrapper around common tools using libwrap.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWtcpwrapper += CSWlibwrap1
OBSOLETED_BY_CSWtcpwrapper += CSWtcpwrap
CATALOGNAME_CSWtcpwrap = tcpwrappers_stub

PACKAGES += CSWlibwrap1
SPKG_DESC_CSWlibwrap1 = Socket wrappers for pre-screening tcp connections (ipv6.4 patched), libwrap.so.1
PKGFILES_CSWlibwrap1 += $(call pkgfiles_lib,libwrap.so.1)
PKGFILES_CSWlibwrap1 += $(mandir)/man5/.*
SPKG_DESC_CSWtcpwrap = $(DESCRIPTION)

PACKAGES += CSWlibwrap-dev
SPKG_DESC_CSWlibwrap-dev = Development files for libwrap.so.1
PKGFILES_CSWlibwrap-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibwrap-dev += CSWlibwrap1

BUILD_ARGS = REAL_DAEMON_DIR=/usr/sbin
BUILD_ARGS += STYLE=-DPROCESS_OPTIONS
BUILD_ARGS += USER_CFLAGS="$(CFLAGS)"
BUILD_ARGS += LIBS="-lsocket -lnsl"

# EXTENDED = off
EXTENDED = on

BUILD64_LIBS_ONLY = 1
NOISALIST = 1

CONFIGURE_SCRIPTS =

BUILD_TARGET_EXTENDED_off = sunos5-shared
BUILD_TARGET_EXTENDED_on = sunos5-sharedext

BUILD_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

MIGRATE_FILES_CSWlibwrap1 = hosts.allow hosts.deny

# This is an example to /usr/local/lib/ntalkd
CHECKPKG_OVERRIDES_CSWtcpwrapper += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/tcpd.8

include gar/category.mk

SPKG_VERSION = $(subst -,_,$(VERSION))

post-extract-modulated:
	-cd $(WORKSRC) && perl -pi -e 's,/etc/hosts\.,$(sysconfdir)/hosts.,g' \
		hosts_access.3 \
		hosts_access.5 \
		tcpd.8 \
		tcpdchk.8 \
		tcpdmatch.8
	@$(MAKECOOKIE)

build-custom:
	$(BUILD_ENV) $(MAKE) -C $(WORKSRC) $(BUILD_ARGS) $(BUILD_TARGET_EXTENDED_$(EXTENDED))
	@$(MAKECOOKIE)

install-custom:
	@echo " => Installing tcpwrapper"
	ginstall -d $(DESTDIR)$(docdir)/tcpwrapper"
	cd $(WORKDIR) && ginstall -v -m 644 README $(DESTDIR)$(docdir)/tcpwrapper/README
	ginstall -d $(DESTDIR)$(libexecdir)
	cd $(WORKSRC) && ginstall -v -m 755 safe_finger tcpd tcpdchk tcpdmatch try-from $(DESTDIR)$(libexecdir)
	ginstall -d $(DESTDIR)$(includedir)
	cd $(WORKSRC) && ginstall -v -m 644 tcpd.h $(DESTDIR)$(includedir)
	ginstall -d $(DESTDIR)$(libdir)
	cd $(WORKSRC) && ginstall -v -m 644 libwrap.so.1 $(DESTDIR)$(libdir)/libwrap.so.1
	gln -s libwrap.so.1 $(DESTDIR)$(libdir)/libwrap.so
	ginstall -d $(DESTDIR)$(mandir)/man3
	cd $(WORKSRC) && ginstall -v -m 644 *.3 $(DESTDIR)$(mandir)/man3
	ginstall -d $(DESTDIR)$(mandir)/man5
	cd $(WORKSRC) && ginstall -v -m 644 *.5 $(DESTDIR)$(mandir)/man5
	ginstall -d $(DESTDIR)$(mandir)/man8
	cd $(WORKSRC) && ginstall -v -m 644 *.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)

