# $Id$

NAME = cswutils
VERSION = 1.20
CATEGORIES = utils

DESCRIPTION = Utilities for CSW maintainers
define BLURB
endef

SVNROOT = http://opencsw.svn.sourceforge.net/svnroot/opencsw/utilities/
SVN_REV = 364

SVNROOT_gar = https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/v2/lib/python/
SVN_REV_gar = HEAD

MASTER_SITES =

DISTFILES = COPYING
DISTFILES += checkpkg checkpkg.8
DISTFILES += cpan2pkg
DISTFILES += createpkg createpkg.8
DISTFILES += stagepkg stagepkg.8
DISTFILES += stagepkg stagepkg.8

BUILD_DEP_PKGS = CSWrsync

RUNTIME_DEP_PKGS += CSWcoreutils
RUNTIME_DEP_PKGS += CSWfakeroot
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpmhtmltree
RUNTIME_DEP_PKGS += CSWpmlibwww
RUNTIME_DEP_PKGS += CSWpmyaml
RUNTIME_DEP_PKGS += CSWpy-cheetah
RUNTIME_DEP_PKGS += CSWpy-hachoir-core
RUNTIME_DEP_PKGS += CSWpy-hachoir-parser
RUNTIME_DEP_PKGS += CSWpy-libmagic
RUNTIME_DEP_PKGS += CSWpy-progressbar
RUNTIME_DEP_PKGS += CSWpy-sqlobject
RUNTIME_DEP_PKGS += CSWpy-curl
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

# possibly remove these and omit the *test* files from distribution entirely
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/home|root/opt/csw/lib/python/csw/testdata/rpaths.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/home|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/opt/build|root/opt/csw/lib/python/csw/testdata/rpaths.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/opt/build|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/usr/local|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/usr/local|root/opt/csw/lib/python/csw/testdata/rpaths.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/medusa|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/medusa|root/opt/csw/lib/python/csw/testdata/rpaths.py

ALTERNATIVES_CSWcswutils = legacy python
ALTERNATIVE_legacy = /opt/csw/bin/checkpkg checkpkg /opt/csw/bin/checkpkg.legacy 5
ALTERNATIVE_python = /opt/csw/bin/checkpkg checkpkg /opt/csw/bin/checkpkg.python 10

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/checkpkg $(DESTDIR)$(bindir)/checkpkg.legacy
	@ginstall $(WORKSRC)/cpan2pkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/createpkg $(DESTDIR)$(bindir)
	@ginstall $(WORKSRC)/stagepkg $(DESTDIR)$(bindir)
	@ginstall $(GARDIR)/bin/fixlibtool $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@ginstall $(WORKSRC)/checkpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKSRC)/createpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKSRC)/stagepkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall -d $(DESTDIR)$(libdir)/python/csw
	@ginstall -d $(DESTDIR)$(datadir)/opencsw/gar
	@ginstall -m 0644 $(GARDIR)/etc/commondirs* $(DESTDIR)/$(datadir)/opencsw/gar/
	@rsync -av --exclude=.svn/ --exclude='*.pyc' $(GARDIR)/lib/python/ \
		$(DESTDIR)/$(libdir)/python/csw/
	@ln -s ../lib/python/csw/compare_pkgs.py \
		$(DESTDIR)$(bindir)/comparepkg
	@ln -s ../lib/python/csw/submit_to_newpkgs.py \
		$(DESTDIR)$(bindir)/submitpkg
	@ln -s ../lib/python/csw/csw_upload_pkg.py \
		$(DESTDIR)$(bindir)/csw-upload-pkg
	@ln -s ../lib/python/csw/checkpkg2.py \
		$(DESTDIR)$(bindir)/checkpkg.python
	@ln -s ../lib/python/csw/pkgdb.py \
		$(DESTDIR)$(bindir)/pkgdb
	@$(MAKECOOKIE)
