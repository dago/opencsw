# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = iwidgets
PACKAGES = CSWtcliwidgets
CATALOGNAME_CSWtcliwidgets = tcl-iwidgets
VERSION = 4.0.1
GARTYPE = v2
CATEGORIES = lang
ARCHALL_CSWtcliwidgets = 1
DISTNAME = $(NAME)$(VERSION)
RUNTIME_DEP_PKGS_CSWiwidgets = CSWtcl CSWtclitcl CSWtclitk

DESCRIPTION = [incr Widgets] is a library of reusable mega-widgets for Tcl/Tk

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

# This package needs the source code of Itcl and Itk to build.
# Unpack these two /opt/csw/src/itcl and /opt/csw/src/itk.
# It also requires the files /opt/csw/src/config/mkinstalldirs
# and /opt/csw/src/config/installFile.tcl to be present.
# (location is specified using --with-itcl)
CONFIGURE_ARGS = $(DIRPATHS) --with-itcl=/opt/csw/src

BUILD_SCRIPTS =

INSTALL_SCRIPTS = custom

TEST_SCRIPTS = 

TEST_TARGET = 

install-custom:
	gmake -C $(WORKSRC) INSTALL_ROOT=$(DESTDIR) install
	$(MAKECOOKIE)

include gar/category.mk
