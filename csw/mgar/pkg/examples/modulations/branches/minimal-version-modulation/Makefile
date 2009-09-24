# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

# The resulting prototype should look like this:
#
# f none /opt/csw/share/example-1.0.txt 0644 root bin
# f none /opt/csw/share/example-1.1.txt 0644 root bin
# f none /opt/csw/share/example-2.0.txt 0644 root bin
# i depend=CSWmodulatedpkg.depend
# i pkginfo=CSWmodulatedpkg.pkginfo

GARNAME = modulatedpkg
GARVERSION = 2.0
CATEGORIES = utils
DESCRIPTION = An example of a modulated package
define BLURB
endef
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = example
TEST_SCRIPTS =

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.0 1.1 2.0
MERGE_SCRIPTS_isa-sparcv8-garversion-1.0 = copy-all
MERGE_SCRIPTS_isa-sparcv8-garversion-1.1 = copy-all
MERGE_SCRIPTS_isa-sparcv8-garversion-2.0 = copy-all

# A really simple installator, creating different files for each GARVERSION.
install-example:
	ginstall -d -m 755 $(DESTDIR)$(datadir)
	echo "This file belongs to the $(GARNAME)-$(GARVERSION)." \
		> $(DESTDIR)$(datadir)/example-$(GARVERSION).txt
	@$(MAKECOOKIE)

include gar/category.mk
