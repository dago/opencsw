GARNAME = tcp_wrappers
BASEVERSION = 7.6
RELEASE = ipv6.4
GARVERSION = $(BASEVERSION)-$(RELEASE)
CATEGORIES = lib

DESCRIPTION = Socket wrappers for pre-screening tcp connections (ipv6.4 patched)
define BLURB
  Socket Wrappers is an improved version of tcp_wrappers by Wietse Venema.
endef

MASTER_SITES = http://ftp.porcupine.org/pub/security/
DISTNAME = $(GARNAME)_$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz
DISTFILES += COPYING
DISTFILES += README

PATCHFILES = patch-cflags.diff
PATCHFILES += man.patch
PATCHFILES += sharedlib.patch

WORKSRC = $(WORKDIR)/$(DISTNAME)

PACKAGES = CSWtcpwrap
CATALOGNAME = tcpwrappers

SPKG_VERSION = $(BASEVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)_(\d+(?:\.\d+)*).tar.gz

EXTRA_MODULATORS = EXTENDED
MODULATIONS_EXTENDED = on off

BUILD_ARGS = REAL_DAEMON_DIR=/usr/sbin
BUILD_ARGS += STYLE=-DPROCESS_OPTIONS
BUILD_ARGS += USER_CFLAGS="$(CFLAGS)"

BUILD64 = 1

CONFIGURE_SCRIPTS =

BUILD_TARGET_EXTENDED_off = sunos5-shared
BUILD_TARGET_EXTENDED_on = sunos5-sharedext

BUILD_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

LIBNAME_EXTENDED-off = libwrap-std.so.1
LIBNAME_EXTENDED-on  = libwrap-ext.so.1

INSTALL_SCRIPTS = custom

MERGE_SCRIPTS_isa-sparcv8-extended-off = copy-all
 MERGE_SCRIPTS_isa-sparcv8-extended-on = copy-relocated-only
    MERGE_DIRS_isa-sparcv8-extended-on = $(libdir)

MERGE_SCRIPTS_isa-sparcv9-extended-off = copy-relocated-only
   MERGE_DIRS_isa-sparcv9-extended-off = $(libdir)
 MERGE_SCRIPTS_isa-sparcv9-extended-on = copy-relocated-only
    MERGE_DIRS_isa-sparcv9-extended-on = $(libdir)

   MERGE_SCRIPTS_isa-i386-extended-off = copy-all
    MERGE_SCRIPTS_isa-i386-extended-on = copy-relocated-only
       MERGE_DIRS_isa-i386-extended-on = $(libdir)

  MERGE_SCRIPTS_isa-amd64-extended-off = copy-relocated-only
     MERGE_DIRS_isa-amd64-extended-off = $(libdir)
   MERGE_SCRIPTS_isa-amd64-extended-on = copy-relocated-only
      MERGE_DIRS_isa-amd64-extended-on = $(libdir)

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
	cd $(WORKSRC) && ginstall -v -m 644 libwrap.so.1 $(DESTDIR)$(libdir)/$(LIBNAME_EXTENDED-$(EXTENDED))
	ginstall -d $(DESTDIR)$(mandir)/man3
	cd $(WORKSRC) && ginstall -v -m 644 *.3 $(DESTDIR)$(mandir)/man3
	ginstall -d $(DESTDIR)$(mandir)/man5
	cd $(WORKSRC) && ginstall -v -m 644 *.5 $(DESTDIR)$(mandir)/man5
	ginstall -d $(DESTDIR)$(mandir)/man8
	cd $(WORKSRC) && ginstall -v -m 644 *.8 $(DESTDIR)$(mandir)/man8
	@$(MAKECOOKIE)

post-merge:
	ln -s libwrap-std.so.1 $(PKGROOT)$(libdir)/libwrap.so.1
	ln -s libwrap.so.1 $(PKGROOT)$(libdir)/libwrap.so
	ln -s libwrap-std.so.1 $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libwrap.so.1
	ln -s libwrap.so.1 $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libwrap.so
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

