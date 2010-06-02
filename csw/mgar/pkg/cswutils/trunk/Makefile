# $Id$

GARNAME = cswutils
GARVERSION = 1.14.6
CATEGORIES = utils

DESCRIPTION = Utilities for CSW maintainers
define BLURB
endef

SVNROOT = http://opencsw.svn.sourceforge.net/svnroot/opencsw/utilities/
SVN_REV = 133

MASTER_SITES =
SVN_FILES = compare_pkgs.py
DISTFILES = COPYING
DISTFILES += checkpkg checkpkg.8
DISTFILES += cpan2pkg
DISTFILES += createpkg createpkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += $(foreach F,$(SVN_FILES),$(F)-r$(SVN_REV))
DISTFILES += opencsw.py checkpkg.py submitpkg


RUNTIME_DEP_PKGS = CSWcoreutils CSWfakeroot CSWperl
RUNTIME_DEP_PKGS += CSWpmyaml CSWpmlibwww CSWpmhtmltree
RUNTIME_DEP_PKGS += CSWpython

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org/

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWcswutils += unidentified-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency|CSWpmhtmltree
CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency|CSWfakeroot
CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency|CSWpmyaml
CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency|CSWpmlibwww
CHECKPKG_OVERRIDES_CSWcswutils += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWcswutils += catalogname-does-not-start-with-py_

include gar/category.mk

# This target doesn't work when defined as $(DOWNLOADDIR)/%-r$(SVN_REV)
$(foreach F,$(SVN_FILES),$(DOWNLOADDIR)/$(F)-r$(SVN_REV)):
	svn export -r $(SVN_REV) $(SVNROOT)$(subst -r$(SVN_REV),,$(notdir $@))
	mv $(subst -r$(SVN_REV),,$(notdir $@)) $@
	@$(MAKECOOKIE)

$(DOWNLOADDIR)/opencsw.py:
	ln -s $(abspath gar/lib/python/opencsw.py) $(DOWNLOADDIR)/
	@$(MAKECOOKIE)

$(DOWNLOADDIR)/checkpkg.py:
	ln -s $(abspath gar/lib/python/checkpkg.py) $(DOWNLOADDIR)/
	@$(MAKECOOKIE)

$(DOWNLOADDIR)/submitpkg:
	ln -s $(abspath gar/bin/submitpkg) $(DOWNLOADDIR)/
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/checkpkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/cpan2pkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/createpkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/stagepkg $(DESTDIR)$(bindir)
	@ginstall $(GARDIR)/bin/fixlibtool $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@ginstall $(WORKSRC)/checkpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKSRC)/createpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKSRC)/stagepkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall -d $(DESTDIR)$(libdir)/python/csw
	@ginstall -m 644 $(WORKSRC)/opencsw.py $(WORKSRC)/checkpkg.py \
		$(DESTDIR)$(libdir)/python/csw/
	@ginstall -m 755 $(WORKSRC)/submitpkg $(DESTDIR)$(bindir)/submitpkg
	@for f in $(SVN_FILES); do \
		ginstall -m 755 $(WORKSRC)/$${f}-r$(SVN_REV) \
		$(DESTDIR)$(libdir)/python/csw/$${f}; \
	done
	@ln -s ../lib/python/csw/compare_pkgs.py $(DESTDIR)$(bindir)/comparepkg
	@$(MAKECOOKIE)
