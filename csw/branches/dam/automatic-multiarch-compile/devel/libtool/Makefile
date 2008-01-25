GARNAME = libtool
GARVERSION = 1.5.24
CATEGORIES = devel

DESCRIPTION = A generic library support tool.
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibtool)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk

post-install:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(prefix)/share/info/dir
	@$(MAKECOOKIE)

