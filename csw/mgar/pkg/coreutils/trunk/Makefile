GARNAME = coreutils
GARVERSION = 8.2
CATEGORIES = utils

# seq has issues related to the handling of long double's with -O2.
# this issue manifested on sol8 and sol9 x86 only.  sparc was unaffected
# and sol10 x86 was fine too.
OPT_FLAGS_GCC = -O1 -pipe

# building with gcc gets us extra tools (eg: stdbuf)
GARCOMPILER = GCC4

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
CONFIGURE_ARGS += --enable-no-install-program=chcon

TEST_TARGET = check

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/bin:$(PATH)

post-install-modulated:
	@echo Cleaning up install directory...
	rm -rf $(DESTDIR)/$(libdir)
	@echo Manually install gsu (so no root rights required)
	cp $(WORKSRC)/src/su $(DESTDIR)$(bindir)/gsu

post-merge:
	@(cd $(PKGROOT)$(prefix); \
		mkdir gnu; cd gnu; \
		for f in ../bin/g*; do \
			echo Linking $$f; \
			base=$$(basename $$f); \
			gln -s $$f ./$${base/g/}; \
		done )
	@$(MAKECOOKIE)
