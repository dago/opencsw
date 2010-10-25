# TODO (release-critical prefixed with !, non release-critical with *)

GARNAME = fio
GARVERSION = 1.44
CATEGORIES = apps

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
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES += 0001-Honour-GAR-CFLAGS-and-use-inttypes.h-instead-of-stdi.patch
PATCHFILES += 0002-Honor-prefix-when-installing-fio.patch
PATCHFILES += 0003-Install-man-pages.patch

# CLOCK_MONOTONIC undefined / not present on Solaris 9
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# fio compiler/compiler.h #errors out non gcc compilers
GARCOMPILER  = GCC3
# Required for PTHREAD_STACK_MIN
EXTRA_CFLAGS  = -D__EXTENSIONS__

CONFIGURE_SCRIPTS = 
BUILD_ARGS = -f Makefile.solaris
TEST_SCRIPTS =
INSTALL_ARGS = -f Makefile.solaris

include gar/category.mk

# install target requires ginstall as install
PATH := /opt/csw/gnu/:$(PATH)

post-install-modulated:
	mkdir -p $(PKGROOT)$(docdir)/fio/examples
	cp $(WORKSRC)/examples/* $(PKGROOT)$(docdir)/fio/examples/
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
