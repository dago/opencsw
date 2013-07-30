# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = dmenu
VERSION = 4.5
GARTYPE = v2

DESCRIPTION = Dynamic menu for X, originally designed for dwm

MASTER_SITES = http://dl.suckless.org/tools/
DISTFILES  = $(DISTNAME).tar.gz
VENDOR_URL = http://tools.suckless.org/dmenu/

PATCHFILES += 0001-Assorted-changes-to-make-it-compile.patch

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = dmenu
INSTALL_SCRIPTS = dmenu
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

GARCOMPILER = GNU

include gar/category.mk


build-dmenu:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) gmake
	$(MAKECOOKIE)

install-dmenu:
	cd $(WORKSRC) &&  /usr/bin/env -i $(INSTALL_ENV) gmake install
	$(MAKECOOKIE)

