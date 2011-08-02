# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = bwidget
PACKAGES = CSWtclbwidget
CATALOGNAME_CSWtclbwidget = tcl-bwidget
VERSION = 1.9.5
GARTYPE = v2
CATEGORIES = lang
ARCHALL_CSWtclbwidget = 1
DESCRIPTION = The BWidget Toolkit is a high-level widget set for Tcl/Tk
RUNTIME_DEP_PKGS_CSWiwidgets = CSWtcl CSWtclitcl CSWtclitk

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_SCRIPTS = 

BUILD_SCRIPTS =

INSTALL_SCRIPTS = custom

TEST_SCRIPTS = 

TEST_TARGET = 

install-custom:
	( TCL_INSTDIR=$(DESTDIR)$(libdir)/tcl`echo 'puts $$tcl_version' | $(bindir)/tclsh`/$(NAME)$(VERSION) ;\
	mkdir -p -m 755 $$TCL_INSTDIR ;\
	cp -pr $(WORKSRC)/* $$TCL_INSTDIR )
	$(MAKECOOKIE)

include gar/category.mk
