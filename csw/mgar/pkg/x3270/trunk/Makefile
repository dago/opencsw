# $Id$
NAME = x3270
BASEREL = 3.3
VERSION = $(BASEREL).12ga11
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = An IBM 3270 terminal emulator
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = suite3270-$(VERSION)-src.tgz

# Add patch until this bug is resolved:
#   https://sourceforge.net/tracker/?func=detail&aid=3151250&group_id=153338&atid=787364
PATCHFILES += 0002-Propagate-CFLAGS-to-building-of-version.o.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-src.tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://x3270.sourceforge.net/

LICENSE = c3270-$(BASEREL)/LICENSE

BUILD_DEP_PKGS += CSWtcl-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWlibreadline-dev
BUILD_DEP_PKGS += CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibncurses-dev

PACKAGES += CSWx3270
SPKG_DESC_CSWx3270 = An IBM 3270 terminal emulator
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWx3270 += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWx3270 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWx3270 += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWx3270 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWx3270 += CSWlibncursesw5

# These are just docs, override for now
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/tcl3270/html/Build.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/tcl3270/html/Resources.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/s3270/html/Build.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/s3270/html/s3270-man.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/s3270/html/Resources.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/pr3287/README
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/pr3287/html/Build.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/x3270/html/Build.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/x3270/html/FAQ.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/x3270/html/Resources.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/c3270/html/c3270-man.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/c3270/html/Resources.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/x3270/c3270/html/Build.html
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/c3270.1
CHECKPKG_OVERRIDES_CSWx3270 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/s3270.1

# wc3270 = windows console, we don't need that.
# wpr3270 = MinGW
# ws3270 = MinGW
# SUBSYSTEMS = c3270 pr3287 s3270 tcl3270 wc3270 wpr3287 ws3270 x3270
SUBSYSTEMS = c3270 pr3287 s3270 tcl3270 x3270

EXTRA_LINKER_FLAGS = -liconv

WORKSRC = $(WORKDIR)
PATCHDIR = $(WORKDIR)

# CONFIGURE_SCRIPTS = $(foreach S,$(SUBSYSTEMS),$(WORKDIR)/$S-$(BASEREL)/configure)
CONFIGURE_SCRIPTS = $(addprefix x3270-,$(SUBSYSTEMS))

sysconfdir = /etc/opt/csw
CONFIGURE_ARGS-tcl3270 = --with-tcl=8.4
CONFIGURE_ARGS-x3270 = --with-fontdir=$(sharedstatedir)/x3270
CONFIGURE_ARGS = $(DIRPATHS)

BUILD_SCRIPTS = $(foreach S,$(SUBSYSTEMS),$(WORKDIR)/$S-$(BASEREL)/Makefile)
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(BUILD_SCRIPTS)
INSTALL_ARGS = install.man

# Otherwise one manpage ends up in /usr/openwin/...
INSTALL_OVERRIDE_VARS = MANPATH BINDIR
INSTALL_OVERRIDE_VAR_MANPATH = $(mandir)
INSTALL_OVERRIDE_VAR_BINDIR = $(bindir)

MIGRATE_FILES = x3270/ibm_hosts
PRESERVECONF = $(addprefix $(sysconfdir)/,$(MIGRATE_FILES))

include gar/category.mk

configure-x3270-%:
	@echo " ==> Running configure for $*"
	cd $(WORKDIR)/$*-$(BASEREL) && $(CONFIGURE_ENV) ./configure $(CONFIGURE_ARGS) $(CONFIGURE_ARGS-$*)
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(libdir)/x3270
	ginstall $(WORKSRC)/x3270-$(BASEREL)/x3270_glue.expect $(DESTDIR)$(libdir)/x3270/x3270_glue.expect
	$(foreach S,$(SUBSYSTEMS),ginstall -d $(DESTDIR)$(docdir)/x3270/$S; cp -rp $(WORKSRC)/$S-$(BASEREL)/README $(WORKSRC)/$S-$(BASEREL)/html $(DESTDIR)$(docdir)/x3270/$S;)
	@$(MAKECOOKIE)
