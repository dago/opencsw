GARNAME = cvsps
GARVERSION = 2.1
CATEGORIES = apps

DESCRIPTION = Patchsets for CVS
define BLURB
CVSps is a program for generating 'patchset' information from a CVS repository. A patchset in this case is defined as a set of changes made to a collection of files, and all committed at the same time (using a single 'cvs commit' command). This information is valuable to seeing the big picture of the evolution of a cvs project. While cvs tracks revision information, it is often difficult to see what changes were committed 'atomically' to the repository.
endef

MASTER_SITES = http://www.cobite.com/cvsps/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES = 0001-add-basic-autotools-files.patch
PATCHFILES += 0002-add-modified-autoconf-check_zlib-from-loic-dachary.patch
PATCHFILES += 0003-add-script-to-do-the-autotools-setup-steps.patch
PATCHFILES += 0004-add-config.h-awareness-to-all-source-files.patch
PATCHFILES += 0005-gnulib-import-of-missing-functions.patch
PATCHFILES += 0006-enabled-imported-gnulib-functions.patch
PATCHFILES += 0007-enable-installation-of-man-pages.patch

PREREQUISITE_PKGS = CSWzlib CSWautomake CSWautoconf

REQUIRED_PKGS = CSWzlib CSWcvs

LICENSE = COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS) --with-zlib=/opt/csw

include gar/category.mk

DOCDIR = $(datadir)/doc/$(GARNAME)

pre-configure-modulated:
	@echo About to initialize the autotools bits.
	@(cd $(WORKSRC); chmod +x autoinit.sh; ./autoinit.sh)
	@$(MAKECOOKIE)

post-install-modulated:
	@echo Installing README's, etc.
	@(cd $(WORKSRC_FIRSTMOD); ginstall -m 0755 -d $(DESTDIR)/$(DOCDIR); \
		ginstall -m 0644 CHANGELOG README COPYING $(DESTDIR)/$(DOCDIR))
	@$(MAKECOOKIE)
