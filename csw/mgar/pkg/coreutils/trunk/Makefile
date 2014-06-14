NAME = coreutils
VERSION = 8.22
GARTYPE = v2

# seq has issues related to the handling of long double's with -O2.
# this issue manifested on sol8 and sol9 x86 only.  sparc was unaffected
# and sol10 x86 was fine too.
# OPT_FLAGS_GCC = -O1 -pipe

# building with gcc gets us extra tools (eg: stdbuf)
GARCOMPILER = GNU

SHELL = /opt/csw/bin/bash

BUILD_DEP_PKGS =  CSWautomake CSWautoconf CSWbison CSWggettext-dev CSWgit
BUILD_DEP_PKGS += CSWgperf CSWgzip CSWperl CSWrsync CSWgtar CSWbash

RUNTIME_DEP_PKGS_CSWcoreutils += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcoreutils += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWcoreutils += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWcoreutils += CSWlibgmp10

INCOMPATIBLE_PKGS = CSWshutils CSWtextutils

DESCRIPTION = GNU core utilities
define BLURB
The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. These are the core utilities which are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU utilities, Fileutils, Shellutils, and Textutils. Those three have been combined into a single set of utilities called Coreutils.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.xz


PATCHFILES += 0001-Backport-some-patches-to-suppress-compiler-errors.patch
PATCHFILES += 0002-Avoid-compiler-error-by-casting-the-ignore-option-fr.patch
PATCHFILES += 0003-Only-define-the-out-label-if-it-will-be-used.patch
PATCHFILES += 0004-Ensure-that-dst_exists-is-used-in-all-cases-to-avoid.patch
PATCHFILES += 0005-src-df.c-get_dev-Initialize-variable-v-to-NULL-to-av.patch
PATCHFILES += 0006-Remove-wmudflap.-It-s-deprecated-with-gcc-4.9.patch
PATCHFILES += 0007-Disable-developer-compiler-warning-error-settings.patch

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
CONFIGURE_ARGS += --with-libintl-prefix=/opt/csw
CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw
# handle su manually to avoid needing fakeroot or some such.  this is now
# explicitly required as we modify both --enable-*install-program  lists
CONFIGURE_ARGS += --enable-no-install-program=chcon
CONFIGURE_ARGS += --enable-install-program=hostname,arch

# required for eaccess and not picked up automatically.
EXTRA_LDFLAGS = -lgen

# move the pegs forward
# 8.22 fails some tests for acl reasons on /tmp, but behaviour is identical to solaris tools.
# 8.22 fails some chown tests on nfs, but behaviour is identical to solaris tools.
ifneq ($(VERSION), 8.22)
else
TEST_SCRIPTS =
endif

include gar/category.mk

PATH := ~/bin:/opt/csw/gnu:/opt/csw/bin:$(PATH)

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
	@(cd $(PKGROOT)$(datadir)/info; \
		perl -pi -e 's#/usr/local/bin/printf#/opt/csw/bin/gprintf#g;' \
			 -e 's#/usr/local/bin/listusers#/my/bin/showusers#;' \
			coreutils.info)
	@$(MAKECOOKIE)
