NAME = chmlib
VERSION = 0.40
GARTYPE = v2

DESCRIPTION = Library designed for accessing MS ITSS files (chm)
define BLURB
  CHMLIB is a library for dealing with Microsoft ITSS/CHM format files.
  Right now, it is a very simple library, but sufficient for dealing with
  all of the .chm files I've come across. Due to the fairly well-designed
  indexing built into this particular file format, even a small library is
  able to gain reasonably good performance indexing into ITSS archives.
endef

MASTER_SITES = http://www.jedrea.com/chmlib/
DISTFILES += $(DISTNAME).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES += CSWlibchm0
SPKG_DESC_CSWlibchm0 = Library designed for accessing MS ITSS files (chm), libchm.so.0
PKGFILES_CSWlibchm0 += $(call pkgfiles_lib,libchm.so.0)
OBSOLETED_BY_CSWlibchm0 += CSWchmlib

PACKAGES += CSWlibchm-dev
SPKG_DESC_CSWlibchm-dev = Development files for libchm.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibchm-dev += CSWlibchm0

EXTRA_LINKER_FLAGS += -lnsl -lsocket

BUILD64 = 1
ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-examples

DOCS  = NEWS README
DOCS += ChmLib-ds6.zip ChmLib-ce.zip

include gar/category.mk

post-install:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	$(foreach D,$(DOCS),ginstall $(WORKSRC)/$D $(DESTDIR)$(docdir)/$(NAME)/$D;)
	@$(MAKECOOKIE)
