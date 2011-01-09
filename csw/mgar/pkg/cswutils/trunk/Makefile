# $Id$

NAME = cswutils
VERSION = 1.16
CATEGORIES = utils

DESCRIPTION = Utilities for CSW maintainers
define BLURB
endef

SVNROOT = http://opencsw.svn.sourceforge.net/svnroot/opencsw/utilities/
SVN_REV = 133

SVNROOT_gar = https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2/lib/python/
SVN_REV_gar = HEAD

MASTER_SITES =

# these are pulled from gar/lib/python
PYFILES += catalog.py
PYFILES += checkpkg.py
PYFILES += checkpkg2.py
PYFILES += checkpkg_lib.py
PYFILES += common_constants.py
PYFILES += compare_pkgs.py
PYFILES += configuration.py
PYFILES += database.py
PYFILES += dependency_checks.py
PYFILES += inspective_package.py
PYFILES += ldd_emul.py
PYFILES += models.py
PYFILES += mute_progressbar.py
PYFILES += opencsw.py
PYFILES += overrides.py
PYFILES += package.py
PYFILES += package_checks.py
PYFILES += package_stats.py
PYFILES += pkgdb.py
PYFILES += pkgmap.py
PYFILES += pylintrc
PYFILES += sharedlib_utils.py
PYFILES += shell.py
PYFILES += struct_util.py
PYFILES += submit_to_newpkgs.py
PYFILES += system_pkgmap.py
PYFILES += tag.py

DISTFILES = COPYING
DISTFILES += checkpkg checkpkg.8
DISTFILES += cpan2pkg
DISTFILES += createpkg createpkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += $(PYFILES)

RUNTIME_DEP_PKGS += CSWcoreutils
RUNTIME_DEP_PKGS += CSWfakeroot
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpmhtmltree
RUNTIME_DEP_PKGS += CSWpmlibwww
RUNTIME_DEP_PKGS += CSWpmyaml
RUNTIME_DEP_PKGS += CSWpy-hachoir-parser
RUNTIME_DEP_PKGS += CSWpy-libmagic
RUNTIME_DEP_PKGS += CSWpy-progressbar
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
	@ln -s ../lib/python/csw/compare_pkgs.py $(DESTDIR)$(bindir)/comparepkg
	@ln -s ../lib/python/csw/submit_to_newpkgs.py $(DESTDIR)$(bindir)/submitpkg
	@$(MAKECOOKIE)
