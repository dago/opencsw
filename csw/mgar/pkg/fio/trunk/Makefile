# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Solaris 9 is missing getopt_long
#   gcc -mtune=i686 -O2 -pipe -m32 -march=i386 -D__EXTENSIONS__ -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DFIO_INC_DEBUG -o fio gettime.o fio.o ioengines.o init.o stat.o log.o time.o filesetup.o eta.o verify.o memory.o io_u.o parse.o mutex.o options.o rbtree.o fifo.o smalloc.o filehash.o lib/strsep.o helpers.o solaris.o profile.o debug.o lib/rand.o lib/flist_sort.o lib/num2str.o crc/crc7.o crc/crc16.o crc/crc32.o crc/crc32c.o crc/crc32c-intel.o crc/crc64.o crc/sha1.o crc/sha256.o crc/sha512.o crc/md5.o engines/cpu.o engines/mmap.o engines/posixaio.o engines/sync.o engines/null.o engines/net.o engines/solarisaio.o  -lpthread -lm -ldl -laio -lrt -lnsl -lsocket
#   Undefined                       first referenced
#   symbol                             in file
#   getopt_long_only                    init.o
#


GARNAME = fio
GARVERSION = 1.44.2
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
PATCHFILES += 0003-Install-man-pages.patch
# Should be integrated in future releases,
# cf. http://www.spinics.net/lists/fio/msg00580.html
PATCHFILES += 0005-Warn-on-missing-direct-IO-support.patch
PATCHFILES += 0006-Use-CLOCK_HIGHRES-if-CLOCK_MONOTONIC-is-missing.patch

# fio compiler/compiler.h #errors out non gcc compilers
GARCOMPILER  = GCC3
# Required for PTHREAD_STACK_MIN
EXTRA_CFLAGS  = -D__EXTENSIONS__

CONFIGURE_SCRIPTS = 
BUILD_ARGS = -f Makefile.solaris
TEST_SCRIPTS =
INSTALL_ARGS = -f Makefile.solaris

INSTALL_OVERRIDE_VARS = INSTALL prefix mandir
INSTALL_OVERRIDE_VAR_INSTALL = $(bindir)/ginstall
INSTALL_OVERRIDE_VAR_prefix  = $(prefix)
INSTALL_OVERRIDE_VAR_mandir  = $(mandir)

include gar/category.mk

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
