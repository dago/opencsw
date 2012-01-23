NAME = chmlib
VERSION = 0.40
CATEGORIES = lib

DESCRIPTION = Library designed for accessing MS ITSS files (chm)
define BLURB
  CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
  Right now, it is a very simple library, but sufficient for dealing with
  all of the .chm files I've come across. Due to the fairly well-designed
  indexing built into this particular file format, even a small library is
  able to gain reasonably good performance indexing into ITSS archives.
endef

MASTER_SITES = http://www.jedrea.com/chmlib/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

PATCHFILES =  0001-gnulib-import-getopt-posix.patch
PATCHFILES += 0002-integrate-gnulib-into-the-auto-tool-files.patch
PATCHFILES += 0003-add-dummy-config.h-file.patch
PATCHFILES += 0004-add-autoconf-checks-for-lnsl-and-lsocket.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-examples

MERGE_DIRS_isa-extra = $(libdir)

DOCS  = NEWS README
DOCS += ChmLib-ds6.zip ChmLib-ce.zip

include gar/category.mk

pre-configure-modulated:
	@(cd $(WORKSRC); aclocal -I gnulib/m4; autoconf -I gnulib/m4; automake)
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	$(foreach D,$(DOCS),ginstall $(WORKSRC)/$D $(DESTDIR)$(docdir)/$(NAME)/$D;)
	@$(MAKECOOKIE)
