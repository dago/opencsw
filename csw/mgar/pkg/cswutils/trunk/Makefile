# $Id$

NAME = cswutils
VERSION = 1.$(GARHEAD)
GARTYPE = v2
GARHEAD = $(shell svn info $(SVNROOT_gar) | grep 'Last Changed Rev' | sed 's/[^0-9]*//')

DESCRIPTION = Utilities for CSW maintainers

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
RUNTIME_DEP_PKGS += CSWpy-libmagic
RUNTIME_DEP_PKGS += CSWpy-pyelftools
RUNTIME_DEP_PKGS += CSWpy-progressbar
RUNTIME_DEP_PKGS += CSWpy-sqlobject
RUNTIME_DEP_PKGS += CSWpy-curl
RUNTIME_DEP_PKGS += CSWpython

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org/

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWcswutils += surplus-dependency
CHECKPKG_OVERRIDES_CSWcswutils += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWcswutils += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWcswutils += archall-with-arch-paths|/opt/csw/share/opencsw/gar/commondirs-i386
CHECKPKG_OVERRIDES_CSWcswutils += archall-with-arch-paths|/opt/csw/share/opencsw/gar/commondirs-sparc

# possibly remove these and omit the *test* files from distribution entirely
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/home|root/opt/csw/lib/python/csw/testdata/rpaths.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/home|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/opt/build|root/opt/csw/lib/python/csw/testdata/rpaths.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/opt/build|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/usr/local|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/usr/local|root/opt/csw/lib/python/csw/testdata/rpaths.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/medusa|root/opt/csw/lib/python/csw/package_checks_test.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/export/medusa|root/opt/csw/lib/python/csw/testdata/rpaths.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/usr/local|root/opt/csw/lib/python/csw/testdata/vsftpd_stats.py
CHECKPKG_OVERRIDES_CSWcswutils += file-with-bad-content|/usr/share|root/opt/csw/lib/python/csw/testdata/vsftpd_stats.py

ALTERNATIVES_CSWcswutils = legacy python
ALTERNATIVE_legacy = /opt/csw/bin/checkpkg checkpkg /opt/csw/bin/checkpkg.legacy 5
ALTERNATIVE_python = /opt/csw/bin/checkpkg checkpkg /opt/csw/bin/checkpkg.python 10

include gar/category.mk

build-custom:
	cd $(WORKSRC) && svn export $(SVNROOT_gar) gar-code
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall $(WORKDIR)/checkpkg $(DESTDIR)$(bindir)/checkpkg.legacy
	@ginstall $(WORKDIR)/cpan2pkg $(DESTDIR)$(bindir)
	@ginstall $(WORKDIR)/createpkg $(DESTDIR)$(bindir)
	@ginstall $(WORKDIR)/stagepkg $(DESTDIR)$(bindir)
	@ginstall $(GARDIR)/bin/fixlibtool $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man8
	@ginstall $(WORKDIR)/checkpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKDIR)/createpkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall $(WORKDIR)/stagepkg.8 $(DESTDIR)$(mandir)/man8/
	@ginstall -d $(DESTDIR)$(libdir)/python/csw
	@ginstall -d $(DESTDIR)$(datadir)/opencsw/gar
	@(echo $(GARHEAD) > $(DESTDIR)$(datadir)/opencsw/gar/cswutils.svn_version.txt)
	@ginstall -m 0644 $(GARDIR)/etc/commondirs* $(DESTDIR)/$(datadir)/opencsw/gar/
	@rsync -av \
		--exclude=testdata/ \
		--exclude='*.pyc' \
		$(WORKSRC)/gar-code/ \
		$(DESTDIR)/$(libdir)/python/csw/
	@ln -s ../lib/python/csw/csw_upload_pkg.py \
		$(DESTDIR)$(bindir)/csw-upload-pkg
	@ln -s ../lib/python/csw/checkpkg2.py \
		$(DESTDIR)$(bindir)/checkpkg.python
	@ln -s ../lib/python/csw/pkgdb.py \
		$(DESTDIR)$(bindir)/pkgdb
	@$(MAKECOOKIE)
