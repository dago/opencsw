GARNAME = unrar
GARVERSION = 3.9.6
CATEGORIES = utils

DESCRIPTION = Brief description
define BLURB
  Long description
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

#BUILD_SCRIPTS = $(WORKSRC)/makefile.unix
BUILD_ARGS = -f makefile.unix CXX=$(CXX) CXXFLAGS="$(CXXFLAGS)" DEFINES="-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" STRIP=strip

TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

#CXXFLAGS=-fast -erroff=wvarhidemem
#DEFINES=-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE
#STRIP=strip
#DESTDIR=/usr

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKDIR)/unrar.1 $(DESTDIR)$(mandir)/man1/
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/unrar $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(docdir)/unrar
	ginstall $(WORKSRC)/readme.txt $(DESTDIR)$(docdir)/unrar
	@$(MAKECOOKIE)
