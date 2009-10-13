# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = loose-files
GARVERSION = 1.0
CATEGORIES = utils
DESCRIPTION = An example of a package created from loose files.
define BLURB
endef
SPKG_SOURCEURL =

PACKAGES = CSWloosefilesexa
CATALOGNAME = loose_files_example

# The directory where all the sources are kept. The slash at the end is
# necessary.
LOCAL_SRC = /usr/xpg4/

# The list of files to include, relative to LOCAL_SRC
FILES  = bin/grep
FILES += include/curses.h

MASTER_SITES = $(sort $(addprefix file://$(LOCAL_SRC),$(dir $(FILES))))
DISTFILES  = $(notdir $(FILES))

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk

install-custom:
	$(foreach F,$(FILES),ginstall \
		-d $(DESTDIR)$(prefix)/$(dir $F) \
		&& ginstall $(WORKDIR)/$(notdir $F) \
		$(DESTDIR)$(prefix)/$(dir $F);)
	@$(MAKECOOKIE)
