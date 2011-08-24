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
DISTFILES += CSWtcpwrap.postmsg

PATCHFILES = patch-cflags.diff
PATCHFILES += man.patch
PATCHFILES += sharedlib.patch

WORKSRC = $(WORKDIR)/$(DISTNAME)

PACKAGES = CSWtcpwrap
CATALOGNAME = tcpwrappers
SPKG_DESC_CSWtcpwrap = $(DESCRIPTION)

SPKG_VERSION = $(BASEVERSION)

EXTRA_MODULATORS = EXTENDED
MODULATIONS_EXTENDED = on off

BUILD_ARGS = REAL_DAEMON_DIR=/usr/sbin
BUILD_ARGS += STYLE=-DPROCESS_OPTIONS
BUILD_ARGS += USER_CFLAGS="$(CFLAGS)"
BUILD_ARGS += LIBS="-lsocket -lnsl"

BUILD64 = 1

CONFIGURE_SCRIPTS =

BUILD_TARGET_EXTENDED_off = sunos5-shared
BUILD_TARGET_EXTENDED_on = sunos5-sharedext

BUILD_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

LIBNAME_EXTENDED-off = libwrap-std.so.0
LIBNAME_EXTENDED-on  = libwrap-ext.so.0

INSTALL_SCRIPTS = custom

MERGE_SCRIPTS_isa-default-extended-off = copy-all
 MERGE_SCRIPTS_isa-default-extended-on = copy-only
    MERGE_DIRS_isa-default-extended-on = $(libdir)

MERGE_SCRIPTS_isa-default64-extended-off = copy-relocated-only
   MERGE_DIRS_isa-default64-extended-off = $(libdir)
 MERGE_SCRIPTS_isa-default64-extended-on = copy-relocated-only
    MERGE_DIRS_isa-default64-extended-on = $(libdir)

MIGRATE_FILES = hosts.allow hosts.deny

ALTERNATIVES = std ext
ALTERNATIVE_std  = $(libdir)/libwrap.so.0 tcpwrappers $(libdir)/libwrap-std.so.0 200
ALTERNATIVE_std += $(libdir)/$(ISA_DEFAULT64)/libwrap.so.0 tcpwrappers64 $(libdir)/$(ISA_DEFAULT64)/libwrap-std.so.0
ALTERNATIVE_ext  = $(libdir)/libwrap.so.0 tcpwrappers $(libdir)/libwrap-ext.so.0 100
ALTERNATIVE_ext += $(libdir)/$(ISA_DEFAULT64)/libwrap.so.0 tcpwrappers64 $(libdir)/$(ISA_DEFAULT64)/libwrap-ext.so.0

POSTMSG = $(docdir)/$(CATALOGNAME)/CSWtcpwrap.postmsg

PACKAGES += CSWlibwrap0
CATALOGNAME_CSWlibwrap0 = libwrap0
PKGFILES_CSWlibwrap0 += $(call baseisadirs,$(libdir),libwrap\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibwrap0 += $(DESCRIPTION), libwrap.so.0
RUNTIME_DEP_PKGS_CSWtcpwrap += CSWlibwrap0

PACKAGES += CSWtcpwrap-dev
SPKG_DESC_CSWtcpwrap-dev = $(DESCRIPTION) development package
PKGFILES_CSWtcpwrap-dev += $(PKGFILES_DEVEL)
CATALOGNAME_CSWtcpwrap-dev = tcpwrappers_dev

# These binaries link against libwrap.so which will be linked by alternatives
# after package install. Until then they can obviously not link properly.
CHECKPKG_OVERRIDES  = symbol-not-found|tcpdmatch
CHECKPKG_OVERRIDES += symbol-not-found|tcpd
CHECKPKG_OVERRIDES += symbol-not-found|try-from
CHECKPKG_OVERRIDES += symbol-not-found|tcpdchk

include gar/category.mk

build-custom:
	$(MAKE) -C $(WORKSRC) $(BUILD_ARGS) $(BUILD_TARGET_EXTENDED_$(EXTENDED))
	@$(MAKECOOKIE)

install-custom:
	@echo " => Installing $(CATALOGNAME)"
	ginstall -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	cd $(WORKDIR) && ginstall -v -m 644 README $(DESTDIR)$(docdir)/$(CATALOGNAME)
	ginstall -d $(DESTDIR)$(libexecdir)
	cd $(WORKSRC) && ginstall -v -m 755 safe_finger tcpd tcpdchk tcpdmatch try-from $(DESTDIR)$(libexecdir)
	ginstall -d $(DESTDIR)$(includedir)
	cd $(WORKSRC) && ginstall -v -m 644 tcpd.h $(DESTDIR)$(includedir)
	ginstall -d $(DESTDIR)$(libdir)
	cd $(WORKSRC) && ginstall -v -m 644 libwrap.so.0 $(DESTDIR)$(libdir)/$(LIBNAME_EXTENDED-$(EXTENDED))
	ginstall -d $(DESTDIR)$(mandir)/man3
	cd $(WORKSRC) && ginstall -v -m 644 *.3 $(DESTDIR)$(mandir)/man3
	ginstall -d $(DESTDIR)$(mandir)/man5
	cd $(WORKSRC) && ginstall -v -m 644 *.5 $(DESTDIR)$(mandir)/man5
	ginstall -d $(DESTDIR)$(mandir)/man8
	cd $(WORKSRC) && ginstall -v -m 644 *.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)

post-merge:
	ginstall -d $(PKGROOT)$(dir $(POSTMSG))
	ginstall $(WORKDIR)/$(notdir $(POSTMSG)) $(PKGROOT)$(POSTMSG)
	ln -s libwrap.so.0 $(PKGROOT)$(libdir)/libwrap.so
	ln -s libwrap.so.0 $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libwrap.so
	@# As libwrap.so.0 is the SONAME to be bound against we must register it with the package
	@# to allow chkpkg to look up the pkgname for the library. This is rewritten by alternatives
	@# on installation and is solely to register the link path, the destination doesn't matter.
	ln -s /etc/opt/csw/alternatives/tcpwrappers $(PKGROOT)$(libdir)/libwrap.so.0
	ln -s /etc/opt/csw/alternatives/tcpwrappers64 $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libwrap.so.0
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

