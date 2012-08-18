# TODO (release-critical prefixed with !, non release-critical with *)

NAME = fio
VERSION = 2.0.8
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Flexible I/O Tester
define BLURB
  fio is an I/O tool meant to be used both for benchmark and
  stress/hardware verification. It has support for 13 different types of I/O
  engines (sync, mmap, libaio, posixaio, SG v3, splice, null, network,
  syslet, guasi, solarisaio, and more), I/O priorities (for newer Linux
  kernels), rate I/O, forked or threaded jobs, and much more. It can work on
  block devices as well as files. fio accepts job descriptions in a
  simple-to-understand text format. Several example job files are included.
  fio displays all sorts of I/O performance information. It supports Linux,
  FreeBSD, NetBSD, OS X, and OpenSolaris.
endef

VENDOR_URL   = http://freshmeat.net/projects/fio
MASTER_SITES = http://brick.kernel.dk/snaps/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PATCHFILES	+= 0001-shell-commands.patch

# fio compiler/compiler.h #errors out non gcc compilers
GARCOMPILER  = GCC4
# Required for PTHREAD_STACK_MIN
EXTRA_CFLAGS  = -D__EXTENSIONS__

CONFIGURE_SCRIPTS = 
#BUILD_ARGS = -f Makefile.solaris
TEST_SCRIPTS =
#INSTALL_ARGS = -f Makefile.solaris

INSTALL_OVERRIDE_VARS = INSTALL prefix mandir
INSTALL_OVERRIDE_VAR_INSTALL = $(bindir)/ginstall
INSTALL_OVERRIDE_VAR_prefix  = $(prefix)
INSTALL_OVERRIDE_VAR_mandir  = $(mandir)

include gar/category.mk

post-install-modulated:
	mkdir -p $(DESTDIR)$(docdir)/fio/examples
	cp $(WORKSRC)/examples/* $(DESTDIR)$(docdir)/fio/examples/
	cp $(WORKSRC)/README $(DESTDIR)$(docdir)/fio/
	cp $(WORKSRC)/HOWTO $(DESTDIR)$(docdir)/fio/
	perl -pi -e 's,/bin/sh,/bin/bash,' $(DESTDIR)$(bindir)/fio_generate_plots
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
