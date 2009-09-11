GARNAME = giflib
GARVERSION = 4.1.6
CATEGORIES = lib

DESCRIPTION = A library for reading and writing gif images
define BLURB
  giflib is a library for reading and writing gif images.
  It is API and ABI compatible with libungif which was in
  wide use while the LZW compression algorithm was patented.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWgiflib CSWungif

CATALOGNAME_CSWgiflib = giflib
CATALOGNAME_CSWungif = libungif

SPKG_DESC_CSWgiflib = A library for reading and writing gif images
SPKG_DESC_CSWungif = Links to giflib now the patent is dropped

REQUIRED_PKGS_CSWungif = CSWgiflib

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# We don't want 64 bit executables as they gain no speed
NO_ISAEXEC = 1
MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amd64 = $(libdir)

PKGFILES_CSWungif = .*/libungif\..*

include gar/category.mk

DOCFILES = AUTHORS BUGS COPYING ChangeLog DEVELOPERS INSTALL NEWS ONEWS README TODO

post-install-modulated:
	@mkdir -p $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC) && cp $(DOCFILES) $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC)/doc && cp *.html *.png *.txt $(DESTDIR)$(docdir)/giflib
	@$(MAKECOOKIE)

post-merge:
	gln -s libgif.so.4 $(PKGROOT)$(libdir)/libungif.so.4
	gln -s libgif.so $(PKGROOT)$(libdir)/libungif.so
	@$(MAKECOOKIE)
