NAME = tcl8.4
VERSION = 8.4.19
CATEGORIES = lang

DESCRIPTION = Tcl programming language v8.4
define BLURB
endef

SF_PROJ = tcl
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(SF_PROJ)$(VERSION)
DISTFILES  = $(DISTNAME)-src.tar.gz

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10894
UPSTREAM_USE_SF = 1

VENDOR_URL = http://www.tcl.tk/
LICENSE = license.terms

REN_LIBTCL  = libtcl8.4.so
REN_TCLSH   = tclsh8.4

PATCHDIR = $(WORKDIR)/$(DISTNAME)
PATCHFILES  = soname.diff
PATCHFILES += tcl-dtrace.patch

PACKAGES  = CSWtcl
PACKAGES += CSWtcl8-4
PACKAGES += CSWlibtcl8-4-0
PACKAGES += CSWtcl8-4-dev

ALTERNATIVES_PRIO = 840

RUNTIME_DEP_PKGS_CSWtcl         = CSWtcl8-4
RUNTIME_DEP_PKGS_CSWtcl8-4      = CSWlibtcl8-4-0
RUNTIME_DEP_PKGS_CSWtcl8-4-dev  = CSWlibtcl8-4-0

SPKG_DESC_CSWtcl          = $(DESCRIPTION), backwards compatibility package
SPKG_DESC_CSWtcl8-4       = $(DESCRIPTION)
SPKG_DESC_CSWlibtcl8-4-0  = $(DESCRIPTION), libraries
SPKG_DESC_CSWtcl8-4-dev   = $(DESCRIPTION), development files

# Make sure CSWtcl remains empty, it's just for backwards compatibility:
PKGFILES_CSWtcl8-4        =
PKGFILES_CSWlibtcl8-4-0   = $(call pkgfiles_lib,libtcl8.4.so.0)
PKGFILES_CSWtcl8-4-dev    = $(PKGFILES_DEVEL)
# catchall, so nothing here.
# PKGFILES_CSWtcl8-4


ALTERNATIVES_CSWtcl8-4 += tcl8_4
ALTERNATIVE_tcl8_4     += $(bindir)/tclsh $(ALTERNATIVES_PRIO)
ALTERNATIVE_tcl8_4     += $(libdir)/tclConfig.sh $(ALTERNATIVES_PRIO)

CHECKPKG_OVERRIDES_CSWtcl += surplus-dependency|CSWtcl8-4k

BUILD64 = 1

INCLUDE_FLAGS =

WORKSRC = $(WORKDIR)/$(DISTNAME)/unix

includedir = $(prefix)/include/$(NAME)
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-dtrace

INSTALL_ARGS = install install-private-headers

# tk need the static tclstub library for some reason
MERGE_EXCLUDE_STATICLIBS =

TEST_TARGET = test

include gar/category.mk

# CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

pre-configure-modulated:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; cp -p ../license.terms .; $(prefix)/bin/autoreconf -if )
	@$(MAKECOOKIE)

pre-test-modulated:
	@# Need to manually create symlink to latest version
	@echo Creating symlinks for libtcl8.5.so
	@(cd $(WORKSRC) ; \
		mv $(REN_LIBTCL) $(REN_LIBTCL).0 ; \
		ln -sf $(REN_LIBTCL).0 $(REN_LIBTCL) )
	@$(MAKECOOKIE)

post-install-modulated:
	@# Need to manually create symlink to latest version - it will be handled by alternatives
	@echo Creating tclsh link
	@ln -s $(REN_TCLSH) $(INSTALLISADIR)/$(bindir)/tclsh
	@perl -pi -e "s|/usr/local|$(prefix)|g" $(INSTALLISADIR)/$(libdir)/tclConfig.sh
	@perl -pi -e "s|/usr/local|$(prefix)|g" $(INSTALLISADIR)/$(prefix)/share/man/man1/tclsh.1
	@$(MAKECOOKIE)

