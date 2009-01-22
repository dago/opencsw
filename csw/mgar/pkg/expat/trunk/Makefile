GARNAME = expat
GARVERSION = 2.0.1
CATEGORIES = lib

DESCRIPTION = XML Parser Toolkit
define BLURB
	This is James Clark's Expat XML parser library in C. It is a stream oriented
	parser that requires setting handlers to deal with the structure that the
	parser discovers in the document.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWexpat,)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10127
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

BUILD64 = 1
NO_ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

# The expat 'check' target tries to compile tests that use GCC
# constructs -- won't compile under Forte without hackery.
TEST_TARGET = check
TEST_SCRIPTS =

PKGFILES_CSWexpat-devel = $(PKGFILES_DEVEL)

include gar/category.mk
