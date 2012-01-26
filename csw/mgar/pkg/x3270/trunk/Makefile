# $Id$
NAME = x3270
VERSION = $(BASEREL).11ga6
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

# PATCHFILES += x3270-3.3.6_DBCS.patch
# PATCHFILES += c3270-3.3_ncurses.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-src.tar.gz

VENDOR_URL = http://x3270.sourceforge.net/

BASEREL = 3.3
# wc3270 = windows console, we don't need that.
# wpr3270 = MinGW
# ws3270 = MinGW
# SUBSYSTEMS = c3270 pr3287 s3270 tcl3270 wc3270 wpr3287 ws3270 x3270
SUBSYSTEMS = c3270 pr3287 s3270 tcl3270 x3270

LICENSE = c3270-$(BASEREL)/LICENSE

DEP_PKGS = CSWiconv CSWtcl CSWreadline CSWosslrt CSWncurses

EXTRA_LINKER_FLAGS = -liconv

WORKSRC = $(WORKDIR)
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
	#@$(MAKECOOKIE)
