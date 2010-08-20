GARNAME = bzip2
GARVERSION = 1.0.5
CATEGORIES = utils

DESCRIPTION = bzip2 Compression Utility
define BLURB
bzip2 is a freely available, patent free, high-quality data compressor. It typically
compresses files to within 10% to 15% of the best available techniques (the PPM family of
statistical compressors), whilst being around twice as fast at compression and six
times faster at decompression.
endef

MASTER_SITES = http://www.bzip.org/$(GARVERSION)/
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES   = 0001-CFLAGS-LDFLAGS-for-SOS12-shared-lib.patch
PATCHFILES  += 0002-test-should-depend-on-bzip2.patch
PATCHFILES  += 0003-generate-bzip2recover.patch

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES    = CSWbzip2
CATALOGNAME = bzip2

LICENSE = LICENSE

CHECKPKG_OVERRIDES_CSWbzip2 += pkginfo-description-not-starting-with-uppercase|bzip2|Compression|Utility

BUILD64     = 1
GARCOMPILER = SOS12

CFLAGS  += -KPIC -D_FILE_OFFSET_BITS=64 -fast $(SOS12_CC_FLAGS)
LDFLAGS += $(SOS12_LD_FLAGS) $(RUNPATH_LINKER_FLAGS)

BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"

BUILD_SCRIPTS     = custom
TEST_SCRIPTS      = custom
CONFIGURE_SCRIPTS =
INSTALL_SCRIPTS   = custom

LD_LIBRARY_PATH=.
export LD_LIBRARY_PATH
EXTRA_TEST_EXPORTS = LD_LIBRARY_PATH

include gar/category.mk

PLATFORM  = $(shell if [ `uname -i` = "i86pc" ] ; then echo i86pc ; else echo sun4 ; fi )
OBJDIR    = $(WORKDIR)/$(DISTNAME)
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
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@# install the libraries
	@( for file in $(LIBFILES) ; do \
	     ginstall -c -m 755 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
	   done )
	@ln -s -f $(DESTDIR)$(libdir)/libbz2.so.1.0.5 $(DESTDIR)$(libdir)/libbz2.so
	@ln -s -f $(DESTDIR)$(libdir)/libbz2.so.1.0.5 $(DESTDIR)$(libdir)/libbz2.so.1.0
	@# install the binaries
	@( for file in $(BINFILES) ; do \
	     ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(bindir) ; \
	   done )
	@ginstall -m 755 $(OBJDIR)/bzip2 $(DESTDIR)$(bindir)/bunzip2
	@ginstall -m 755 $(OBJDIR)/bzip2 $(DESTDIR)$(bindir)/bzcat
	@ln -s -f $(DESTDIR)$(bindir)/bzgrep $(DESTDIR)$(bindir)/bzegrep
	@ln -s -f $(DESTDIR)$(bindir)/bzgrep $(DESTDIR)$(bindir)/bzfgrep
	@ln -s -f $(DESTDIR)$(bindir)/bzmore $(DESTDIR)$(bindir)/bzless
	@ln -s -f $(DESTDIR)$(bindir)/bzdiff $(DESTDIR)$(bindir)/bzcmp
	@# install the include files
	@( for file in $(INCFILES) ; do \
	     ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(includedir) ; \
	   done )
	@# install the doc files
	@( for file in $(DOCFILES) ; do \
	     ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(docdir)/$(GARNAME) ; \
	   done )
	@$(MAKECOOKIE)
