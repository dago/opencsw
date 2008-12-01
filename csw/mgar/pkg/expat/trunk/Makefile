GARNAME = expat
GARVERSION = 2.0.0
CATEGORIES = lib

DESCRIPTION = XML Parser Toolkit
define BLURB
	This is James Clark's Expat XML parser library in C. It is a stream oriented
	parser that requires setting handlers to deal with the structure that the
	parser discovers in the document.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWexpat,depend prototype)
DISTFILES += $(call admfiles,CSWexpat-devel,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Compatibility libraries
EXTLIBS   += libexpat.so.0.4.0
EXTLIBS   += libexpat.so.0.5.0
DISTFILES += $(EXTLIBS)

# The expat 'check' target tries to compile tests that use GCC
# constructs -- won't compile under Forte without hackery.
TEST_TARGET = check
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install:
	@for extlib in $(EXTLIBS) ; do \
	    install -m 0755 $(WORKDIR)/$$extlib $(DESTDIR)$(libdir) ; \
	done
