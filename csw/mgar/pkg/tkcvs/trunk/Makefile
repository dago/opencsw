GARNAME = tkcvs
GARVERSION = 8.2
CATEGORIES = apps

DESCRIPTION = A graphical front-end to CVS and Subversion
define BLURB
  TkCVS is a Tcl/Tk based graphical interface to the CVS and Subversion
  version control systems. TkCVS shows the status of files in the
  current working directory, and has tools for tagging, merging,
  importing, exporting, checking in/out, and other typical operations.
endef

MASTER_SITES = http://www.twobarleycorns.net/
DISTNAME = $(GARNAME)_$(subst .,_,$(GARVERSION))
DISTFILES  = $(GARNAME)_$(subst .,_,$(GARVERSION)).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)_(\d+(?:_\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

LICENSE = COPYING
ARCHALL = 1
REQUIRED_PKGS = CSWtcl CSWtk CSWtkdiff

include gar/category.mk

TCL_FILES = $(filter-out %/tkcvs.tcl,$(wildcard $(WORKSRC)/tkcvs/*.tcl))
IMAGE_FILES = $(wildcard $(WORKSRC)/tkcvs/bitmaps/*.gif $(WORKSRC)/tkcvs/bitmaps/*.xbm)

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@ginstall -D $(WORKSRC)/tkcvs/tkcvs.tcl $(DESTDIR)$(prefix)/bin/tkcvs
	@ginstall -D $(WORKSRC)/tkcvs/tkcvs.1 $(DESTDIR)$(prefix)/share/man/man1/tkcvs.1
	@ginstall -d $(DESTDIR)$(prefix)/lib/tkcvs/bitmaps
	@ginstall -m 644 $(TCL_FILES) $(DESTDIR)$(prefix)/lib/tkcvs
	@ginstall -m 644 $(IMAGE_FILES) $(DESTDIR)$(prefix)/lib/tkcvs/bitmaps
	@$(MAKECOOKIE)
