GARNAME = sword
GARVERSION = 1.5.9
CATEGORIES = lib

DESCRIPTION = SWORD Engine (gcc3)
define BLURB
The SWORD Engine is a software framework that allows research manipulation of Biblical texts. There are a number of projects that use The SWORD Engine, including Bibletime, GnomeSword, and The SWORD Project for Windows. Many of these projects already include The SWORD Engine in their distribution, so only download if you were instructed to do so, or are a software developer wishing to develop Bible software.
endef

MASTER_SITES = http://crosswire.org/ftpmirror/pub/sword/source/v1.5
UPSTREAM_MASTER_SITES = http://crosswire.org/ftpmirror/pub/sword/source/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsword, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = v(\d+(?:\.\d+)*)

GARCOMPILER ?= GNU
CPPFLAGS=-D_REENTRANT

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

pre-configure:
	( cd $(WORKSRC); ./usrinst.sh )
	@$(MAKECOOKIE)
