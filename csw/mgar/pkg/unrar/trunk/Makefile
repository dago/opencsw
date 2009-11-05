GARNAME = unrar
GARVERSION = 3.9.6
CATEGORIES = utils

DESCRIPTION = RAR archive extractor
define BLURB
  WinRAR is a powerful archive manager. It can backup your data and reduce the size
  of email attachments, decompress RAR, ZIP and other files downloaded from Internet
  and create new archives in RAR and ZIP file format. You can try WinRAR before buy,
  its trial version is available in downloads.
endef

MASTER_SITES = http://www.rarlab.com/rar/
DISTFILES  = unrarsrc-$(GARVERSION).tar.gz
DISTFILES += unrar.1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.rarlab.com/rar_add.htm

LICENSE = license.txt

DISTNAME = unrar

CONFIGURE_SCRIPTS =

OPT_FLAGS_SOS = -fast -erroff=wvarhidemem

BUILD_ARGS = -f makefile.unix CXX=$(CXX) CXXFLAGS="$(CXXFLAGS)" DEFINES="-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" STRIP=strip

TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKDIR)/unrar.1 $(DESTDIR)$(mandir)/man1/
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/unrar $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(docdir)/unrar
	ginstall $(WORKSRC)/readme.txt $(DESTDIR)$(docdir)/unrar
	@$(MAKECOOKIE)
