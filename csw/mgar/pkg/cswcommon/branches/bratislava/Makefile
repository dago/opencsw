# $Id$

NAME = cswcommon
VERSION = 1.6
GARTYPE = v2

DESCRIPTION = Installs base CSW filesystem directories, symlinks and files
define BLURB
endef

#MASTER_SITES = http://mirror.opencsw.org/opencsw/current/$(shell uname -p)/5.8
# MASTER_SITES = http://mirror.opencsw.org/opencsw/current/sparc/5.8/
# DISTFILES  = common-1.5,REV=2010.12.11-SunOS5.8-sparc-CSW.pkg

PACKAGES = CSWcommon

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWcommon += disallowed-path

include gar/category.mk

install-custom:
	$(FILEDIR)/build_common.sh $(GARCH) $(DESTDIR)
	@$(MAKECOOKIE)
