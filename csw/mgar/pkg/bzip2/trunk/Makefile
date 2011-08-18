# $Id$

NAME = bzip2
VERSION = 1.0.6
CATEGORIES = utils

DESCRIPTION = Compression Utility
define BLURB
  bzip2 is a freely available, patent free, high-quality data compressor. It typically
  compresses files to within 10% to 15% of the best available techniques (the PPM family of
  statistical compressors), whilst being around twice as fast at compression and six
  times faster at decompression.
endef

MASTER_SITES = http://www.bzip.org/$(VERSION)/
DISTFILES = $(DISTNAME).tar.gz

PATCHFILES += 0001-Fix-build-for-shared-lib-for-Solaris-linker.patch

PACKAGES += CSWbzip2
SPKG_DESC_CSWbzip2 += Compression utility for bzip2 compression algorithm
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWbzip2 += CSWlibbz2-1-0

PACKAGES += CSWlibbz2-1-0
SPKG_DESC_CSWlibbz2-1-0 = Compression library, libbz2.so.1.0
PKGFILES_CSWlibbz2-1-0 += $(call pkgfiles_lib,libbz2.so.1.0)

PACKAGES += CSWlibbz2-dev
SPKG_DESC_CSWlibbz2-dev = Development files for libbz2.so.1.0
PKGFILES_CSWlibbz2-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibbz2-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWlibbz2-dev += CSWlibbz2-1-0
CHECKPKG_OVERRIDES_CSWlibbz2-dev += surplus-dependency|CSWlibbz2-1-0
# These are default install locations
CHECKPKG_OVERRIDES_CSWlibbz2-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/bzip2/CHANGES
CHECKPKG_OVERRIDES_CSWlibbz2-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/bzip2/README

LICENSE = LICENSE

BUILD64 = 1

EXTRA_CFLAGS += -KPIC
EXTRA_CFLAGS += -D_FILE_OFFSET_BITS=64

BUILD_ARGS += -f Makefile-libbz2_so
CONFIGURE_SCRIPTS =
TEST_ARGS += -f Makefile-libbz2_so
INSTALL_SCRIPTS = custom

DOCFILES += CHANGES
DOCFILES += README
DOCFILES += manual.html
DOCFILES += manual.pdf
DOCFILES += manual.xml
BINFILES += bzip2
BINFILES += bzdiff
BINFILES += bzgrep
BINFILES += bzip2recover
BINFILES += bzmore
LIBFILES += libbz2.so.$(VERSION)
INCFILES += bzlib.h

include gar/category.mk

install-custom:
	@echo " => Installing $(CATALOGNAME)"
	ginstall -d $(DESTDIR)$(libdir)
	cd $(WORKSRC) && ginstall -c -m 755 $(LIBFILES) $(DESTDIR)$(libdir)
	ln -s libbz2.so.$(VERSION) $(DESTDIR)$(libdir)/libbz2.so
	ln -s libbz2.so.$(VERSION) $(DESTDIR)$(libdir)/libbz2.so.1.0
	ginstall -d $(DESTDIR)$(bindir)
	cd $(WORKSRC) && ginstall -m 755 $(BINFILES) $(DESTDIR)$(bindir)/
	cd $(DESTDIR)$(bindir) && \
		ln bzip2 bunzip2 && \
		ln bzip2 bzcat && \
		ln bzgrep bzegrep && \
		ln bzgrep bzfgrep && \
		ln bzmore bzless && \
		ln bzdiff bzcmp
	ginstall -d $(DESTDIR)$(mandir)/man1
	cd $(WORKSRC) && ginstall -m 644 bzip2.1 bzdiff.1 bzgrep bzip2recover $(DESTDIR)$(mandir)/man1/
	echo ".so man1/bzgrep.1" > $(DESTDIR)$(mandir)/man1/bzegrep.1
	echo ".so man1/bzgrep.1" > $(DESTDIR)$(mandir)/man1/bzfgrep.1
	echo ".so man1/bzmore.1" > $(DESTDIR)$(mandir)/man1/bzless.1
	echo ".so man1/bzdiff.1" > $(DESTDIR)$(mandir)/man1/bzcmp.1
	ginstall -d $(DESTDIR)$(includedir)
	cd $(WORKSRC) && ginstall -m 644 $(INCFILES) $(DESTDIR)$(includedir)/
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	cd $(WORKSRC) && ginstall -m 644 $(DOCFILES) $(DESTDIR)$(docdir)/$(NAME)/
	@$(MAKECOOKIE)
