# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = from-svn-repo
VERSION = 1.0
CATEGORIES = utils
GARTYPE = v2
DESCRIPTION = An example of a paa Subversion repository

VENDOR_URL = http://www.opencsw.org/manual/

SVN_REPO = http://usable-solaris.googlecode.com/svn/trunk/docs/
SVN_REV = HEAD $(notdir $(FILES))

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = cust# Otherwise there's a .git directory in $(WORKSRC)
NOGITPATCH = 1

# There are no architecture-specific files in this package.
ARCHALL_CSWfrom-svn-repo = 1

include gar/category.mk

# In this case, we're checking out into the $(prefix)/share directory, because
# this repository only contains documentation. You'll have to plan where you
# want to put the files.
post-extract-modulated:
	mkdir -p $(WORKSRC)$(prefix)/share
	svn export -r $(SVN_REV) $(SVN_REPO) $(WORKSRC)$(prefix)/share/usable-solaris
	@$(MAKECOOKIE)

# We're not doing any processing, or copying files into specific locations.
# Our installation is simply copying files from $(WORKSRC). Note the trailing
# slash -- it's necessary.
install-custom:
	rsync -a "$(WORKSRC)/" "$(DESTDIR)"
	@$(MAKECOOKIE)
