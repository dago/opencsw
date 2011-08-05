NAME = bzip2
VERSION = 1.0.5
CATEGORIES = utils

DESCRIPTION = Compression Utility
define BLURB
bzip2 is a freely available, patent free, high-quality data compressor. It typically
compresses files to within 10% to 15% of the best available techniques (the PPM family of
statistical compressors), whilst being around twice as fast at compression and six
times faster at decompression.
endef

MASTER_SITES = http://www.bzip.org/$(VERSION)/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
PATCHFILES   = 0001-CFLAGS-LDFLAGS-for-SOS12-shared-lib.patch
PATCHFILES  += 0002-test-should-depend-on-bzip2.patch
PATCHFILES  += 0003-generate-bzip2recover.patch

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES    = CSWbzip2
CATALOGNAME = bzip2

LICENSE = LICENSE

BUILD64              = 1
NOISAEXEC            = 1
MERGE_DIRS_isa-extra = $(libdir)

EXTRA_CFLAGS  += -KPIC -D_FILE_OFFSET_BITS=64
LDFLAGS += $(LD_OPTIONS)

BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"

BUILD_SCRIPTS     = custom
TEST_SCRIPTS      = custom
CONFIGURE_SCRIPTS =
INSTALL_SCRIPTS   = custom

# The tests will fail if CSWbzip2 isn't already installed, since the runpath for
# bzip2 goes through /opt/csw/lib/... instead of . - just help it out here.
LD_LIBRARY_PATH=.
export LD_LIBRARY_PATH
EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

include gar/category.mk

DOCFILES  = CHANGES README manual.html manual.pdf manual.xml
BINFILES  = bzip2 bzdiff bzgrep bzip2recover bzmore
LIBFILES  = libbz2.so.1.0.5
INCFILES  = bzlib.h

build-custom:
	$(MAKE) -C $(WORKSRC) -f Makefile-libbz2_so $(BUILD_ARGS)
	@$(MAKECOOKIE)

test-custom:
	$(MAKE) -C $(WORKSRC) -f Makefile-libbz2_so test
	@$(MAKECOOKIE)

install-custom:
	@echo " => Installing $(CATALOGNAME)"
	@ginstall -d $(DESTDIR)$(includedir)
	@ginstall -d $(DESTDIR)$(libdir)
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@# install the libraries
	@( for file in $(LIBFILES) ; do \
	     ginstall -c -m 755 $(WORKSRC)/$$file $(DESTDIR)$(libdir) ; \
	   done )
	@ln -s -f $(DESTDIR)$(libdir)/libbz2.so.1.0.5 $(DESTDIR)$(libdir)/libbz2.so
	@ln -s -f $(DESTDIR)$(libdir)/libbz2.so.1.0.5 $(DESTDIR)$(libdir)/libbz2.so.1.0
	@# install the binaries
	@( for file in $(BINFILES) ; do \
	     ginstall -m 755 $(WORKSRC)/$$file $(DESTDIR)$(bindir) ; \
	   done )
	@ginstall -m 755 $(WORKSRC)/bzip2 $(DESTDIR)$(bindir)/bunzip2
	@ginstall -m 755 $(WORKSRC)/bzip2 $(DESTDIR)$(bindir)/bzcat
	@ln -f $(DESTDIR)$(bindir)/bzgrep $(DESTDIR)$(bindir)/bzegrep
	@ln -f $(DESTDIR)$(bindir)/bzgrep $(DESTDIR)$(bindir)/bzfgrep
	@ln -f $(DESTDIR)$(bindir)/bzmore $(DESTDIR)$(bindir)/bzless
	@ln -f $(DESTDIR)$(bindir)/bzdiff $(DESTDIR)$(bindir)/bzcmp
	@# install the include files
	@( for file in $(INCFILES) ; do \
	     ginstall -m 644 $(WORKSRC)/$$file $(DESTDIR)$(includedir) ; \
	   done )
	@# install the doc files
	@( for file in $(DOCFILES) ; do \
	     ginstall -m 644 $(WORKSRC)/$$file $(DESTDIR)$(docdir)/$(NAME) ; \
	   done )
	@$(MAKECOOKIE)
