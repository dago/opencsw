NAME = unzip
VERSION = 6.0
UNZIPVERSION = $(subst .,,$(VERSION))
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Info-Zip UnZip extraction utility for archives compressed in .zip format
define BLURB
endef

SF_PROJECT = infozip
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)$(UNZIPVERSION)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

SPKG_SOURCEURL = http://www.info-zip.org/

LICENSE = LICENSE

# zip's configure is... "special". We use a custom version
CONFIGURE_SCRIPTS = 

EXTRA_CFLAGS  = -D_FILE_OFFSET_BITS=64 -DACORN_FTYPE_NFS
EXTRA_CFLAGS += -DWILD_STOP_AT_DIR -DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT
EXTRA_CFLAGS += -DUNICODE_WCHAR -DUTF8_MAYBE_NATIVE -DNO_LCHMOD -DDATE_FORMAT=DF_YMD
EXTRA_CFLAGS += -DUSE_BZIP2 -DNATIVE

BUILD_ARGS    = -f unix/Makefile LOCAL_UNZIP="$(CFLAGS)" LD="$(CC) $(LDFLAGS)"
BUILD_ARGS   += LF2="" D_USE_BZ2=-DUSE_BZIP2 L_BZ2=-lbz2 unzips
INSTALL_ARGS  = -f unix/Makefile INSTALL=ginstall BINDIR=$(DESTDIR)$(bindir) MANDIR=$(DESTDIR)$(mandir)/man1 install

BUILD64 = 1
ISAEXEC = 1

LICENSE = LICENSE

# There is no test suite
TEST_SCRIPTS = 

include gar/category.mk
