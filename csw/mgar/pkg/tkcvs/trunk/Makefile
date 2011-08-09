NAME = tkcvs
VERSION = 8.2.2
CATEGORIES = apps

DESCRIPTION = A graphical front-end to CVS and Subversion
define BLURB
  TkCVS is a Tcl/Tk based graphical interface to the CVS and Subversion
  version control systems. TkCVS shows the status of files in the
  current working directory, and has tools for tagging, merging,
  importing, exporting, checking in/out, and other typical operations.
endef

MASTER_SITES = http://www.twobarleycorns.net/
DISTNAME = $(NAME)_$(subst .,_,$(VERSION))
DISTFILES  = $(NAME)_$(subst .,_,$(VERSION)).tar.gz

UPSTREAM_MASTER_SITES = $(MASTER_SITES)/tkcvs.html
UFILES_REGEX = $(NAME)_(\d+(?:_\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

LICENSE = COPYING
ARCHALL = 1
RUNTIME_DEP_PKGS = CSWtcl CSWtk CSWtkdiff

CHECKPKG_OVERRIDES_CSWtkcvs += surplus-dependency|CSWtcl
CHECKPKG_OVERRIDES_CSWtkcvs += surplus-dependency|CSWtkdiff
CHECKPKG_OVERRIDES_CSWtkcvs += surplus-dependency|CSWtk

include gar/category.mk

TCL_FILES = $(filter-out %/tkcvs.tcl,$(wildcard $(WORKSRC)/tkcvs/*.tcl))
IMAGE_FILES = $(wildcard $(WORKSRC)/tkcvs/bitmaps/*.gif $(WORKSRC)/tkcvs/bitmaps/*.xbm)

install-custom:
	@echo " ==> Installing $(NAME)"
	@ginstall -D $(WORKSRC)/tkcvs/tkcvs.tcl $(DESTDIR)$(prefix)/bin/tkcvs
	perl -i -plne "s{^exec wish}{exec ${bindir}/wish}g" $(DESTDIR)$(prefix)/bin/tkcvs
	@ginstall -D $(WORKSRC)/tkcvs/tkcvs.1 $(DESTDIR)$(prefix)/share/man/man1/tkcvs.1
	@ginstall -d $(DESTDIR)$(prefix)/lib/tkcvs/bitmaps
	@ginstall -m 644 $(TCL_FILES) $(WORKSRC)/tkcvs/tclIndex $(DESTDIR)$(prefix)/lib/tkcvs
	@ginstall -m 644 $(IMAGE_FILES) $(DESTDIR)$(prefix)/lib/tkcvs/bitmaps
	@$(MAKECOOKIE)
