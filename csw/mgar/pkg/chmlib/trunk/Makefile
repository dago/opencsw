GARNAME = chmlib
GARVERSION = 0.40
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

PATCHFILES = 0001-Add-autoconf-support-from-gnulib-for-getopt.h.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-examples

TEST_TARGET = check

DOCS  = NEWS README
DOCS += ChmLib-ds6.zip ChmLib-ce.zip

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	$(foreach D,$(DOCS),ginstall $(WORKSRC)/$D $(DESTDIR)$(docdir)/$(GARNAME)/$D;)
	@$(MAKECOOKIE)
