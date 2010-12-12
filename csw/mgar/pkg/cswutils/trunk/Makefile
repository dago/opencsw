# $Id$

NAME = cswutils
VERSION = 1.15
CATEGORIES = utils

DESCRIPTION = Utilities for CSW maintainers
define BLURB
endef

SVNROOT = http://opencsw.svn.sourceforge.net/svnroot/opencsw/utilities/
SVN_REV = 133

SVNROOT_gar = https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2/lib/python/
SVN_REV_gar = HEAD

MASTER_SITES =
SVN_FILES = compare_pkgs.py

# these are pulled from gar/lib/python
PYFILES = opencsw.py checkpkg.py submit_to_newpkgs.py package_checks.py
PYFILES += dependency_checks.py overrides.py configuration.py tag.py

DISTFILES = COPYING
DISTFILES += checkpkg checkpkg.8
DISTFILES += cpan2pkg
DISTFILES += createpkg createpkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += $(foreach F,$(SVN_FILES),$(F)-r$(SVN_REV))
DISTFILES += $(PYFILES)

RUNTIME_DEP_PKGS += CSWcoreutils
RUNTIME_DEP_PKGS += CSWfakeroot
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpmhtmltree
RUNTIME_DEP_PKGS += CSWpmlibwww
RUNTIME_DEP_PKGS += CSWpmyaml
RUNTIME_DEP_PKGS += CSWpy-libmagic
RUNTIME_DEP_PKGS += CSWpy-hachoir-parser
RUNTIME_DEP_PKGS += CSWpython

WORKSRC = $(WORKDIR)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org/

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency
CHECKPKG_OVERRIDES_CSWcswutils += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWcswutils += catalogname-does-not-start-with-py_

include gar/category.mk

# This target doesn't work when defined as $(DOWNLOADDIR)/%-r$(SVN_REV)
$(foreach F,$(SVN_FILES),$(DOWNLOADDIR)/$(F)-r$(SVN_REV)):
	svn export -r $(SVN_REV) $(SVNROOT)$(subst -r$(SVN_REV),,$(notdir $@))
	mv $(subst -r$(SVN_REV),,$(notdir $@)) $@
	@$(MAKECOOKIE)

$(foreach PY,$(PYFILES),$(DOWNLOADDIR)/$(PY)):
	@echo "Grabbing $@"
	@svn export -r $(SVN_REV_gar) $(SVNROOT_gar)$(subst -r$(SVN_REV_gar),,$(notdir $@))
	@mv $(subst -r$(SVN_REV_gar),,$(notdir $@)) $@
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
	@for f in $(PYFILES); do \
		ginstall -m 755 $(WORKSRC)/$${f} \
			$(DESTDIR)/$(libdir)/python/csw/; \
	done
	@for f in $(SVN_FILES); do \
		ginstall -m 755 $(WORKSRC)/$${f}-r$(SVN_REV) \
		$(DESTDIR)$(libdir)/python/csw/$${f}; \
	done
	@ln -s ../lib/python/csw/compare_pkgs.py $(DESTDIR)$(bindir)/comparepkg
	@ln -s ../lib/python/csw/submit_to_newpkgs.py $(DESTDIR)$(bindir)/submitpkg
	@$(MAKECOOKIE)
