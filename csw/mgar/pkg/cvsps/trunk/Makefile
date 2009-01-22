GARNAME = cvsps
GARVERSION = 2.1
CATEGORIES = apps

DESCRIPTION = Patchsets for CVS
define BLURB
CVSps is a program for generating 'patchset' information from a CVS repository. A patchset in this case is defined as a set of changes made to a collection of files, and all committed at the same time (using a single 'cvs commit' command). This information is valuable to seeing the big picture of the evolution of a cvs project. While cvs tracks revision information, it is often difficult to see what changes were committed 'atomically' to the repository.
endef

MASTER_SITES = http://www.cobite.com/cvsps/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcvsps,)

PATCHFILES = 0001-adding-initial-autotools-files.patch
PATCHFILES += 0002-adding-script-to-do-the-auto-steps.patch
PATCHFILES += 0004-make-cvsps.c-aware-of-config.h-from-autoconf.patch
PATCHFILES += 0005-add-autoconf-checks-for-lsocket-lnsl.patch
PATCHFILES += 0006-corrected-naming-mistake-in-Makefile.am.patch

PREREQUISITE_PKGS = CSWzlib CSWautomake CSWautoconf

REQUIRED_PKGS = CSWzlib CSWcvs

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

pre-configure-isa-i386:
	@echo About to initialize the autotools bits.
	@(cd $(WORKSRC_FIRSTMOD); chmod +x autoinit.sh; ./autoinit.sh)
	@$(MAKECOOKIE)


install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 755 $(WORKSRC)/cvsps $(DESTDIR)$(bindir)/
	ginstall -m 644 $(WORKSRC)/cvsps.1 $(DESTDIR)$(mandir)/man1/
