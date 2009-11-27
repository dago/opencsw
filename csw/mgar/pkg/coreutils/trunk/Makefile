GARNAME = coreutils
GARVERSION = 8.1
CATEGORIES = utils

SHELL = /opt/csw/bin/bash

PREREQUISITE_PKGS = CSWbash

DESCRIPTION = GNU core utilities
define BLURB
The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. These are the core utilities which are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU utilities, Fileutils, Shellutils, and Textutils. Those three have been combined into a single set of utilities called Coreutils.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Fix-solaris-acl-support-breakage.patch
PATCHFILES += 0002-Add-lintl-to-xalloc-die-LDADD-flags.patch

PREREQUISITE_PKGS =  CSWautomake CSWautoconf CSWbison CSWggettext CSWgit
PREREQUISITE_PKGS += CSWgperf CSWgzip CSWperl CSWrsync CSWgtar CSWbash

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
CONFIGURE_ARGS += --with-libintl-prefix=/opt/csw/
CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw/

TEST_SCRIPTS = custom

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)

test-custom:
	@(cd $(WORKSRC); gmake check)
	@$(MAKECOOKIE)

post-install-modulated:
	@echo Cleaning up install directory...
	rm -rf $(DESTDIR)/$(libdir)

post-merge:
	@(cd $(PKGROOT)$(prefix); \
		mkdir gnu; cd gnu; \
		for f in ../bin/g*; do \
			echo Linking $$f; \
			base=$$(basename $$f); \
			gln -s $$f ./$${base/g/}; \
		done )