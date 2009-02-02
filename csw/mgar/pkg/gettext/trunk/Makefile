GARNAME = gettext
GARVERSION = 0.17
CATEGORIES = lib

DESCRIPTION = GNU locale utilities
define BLURB
	GNU gettext utilities are a set of tools that provides a framework to help other GNU packages produce multi-lingual messages
endef

MASTER_SITES = $(GNU_MIRROR)

DISTFILES  = $(call admfiles,CSWggettext,)
DISTFILES += $(call admfiles,CSWggettextdoc,)
DISTFILES += $(GARNAME)-$(GARVERSION).tar.gz
#Include earlier library revisions for compatibility with existing packages
DISTFILES += libgettextlib-0.14.1.so.i
DISTFILES += libgettextlib-0.14.1.so.s
DISTFILES += libintl.so.2.i
DISTFILES += libintl.so.2.s
DISTFILES += libintl.so.3.i
DISTFILES += libintl.so.3.s

#Apply two bug fixes from gnulib, retrieved from:
#http://git.savannah.gnu.org/cgit/gnulib.git/tree/tests/test-wcwidth.c
#blob: 582a8aa2e87a8235186aa3b1e402bbf03e6646a7
PATCHFILES = test-wcwidth.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
#Dont' depend on packages that depend on me
CONFIGURE_ARGS += --with-included-glib
CONFIGURE_ARGS += --with-included-libcroco
#No glibc
CONFIGURE_ARGS += --with-included-gettext

#Fix acl bug http://savannah.gnu.org/bugs/?21604
EXTRA_LD_FLAGS = -lsec

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

REQUIRED_PKGS_CSWggettext = CSWiconv CSWexpat CSWncurses

#NOTE: gettext tests are sensitive to bash environment variables, make sure
#      custom paths are prefixed by $PATH, may be better to set aside
#      ~/.bashrc, etc. during build.
TEST_TARGET = check

#provided by iconv
MERGE_EXCLUDE_FILES  = .*/charset.alias
MERGE_EXCLUDE_FILES += .*/iconv.m4

PKGFILES_CSWggettextdoc  = $(PKGFILES_DOC)

include gar/category.mk

#Include old libraries for compatibility with existing packages
#  TODO: Convert to modulated builds
post-install-isa-sparcv8:
	@cp $(FILEDIR)/libgettextlib-0.14.1.so.s $(INSTALLISADIR)/opt/csw/lib/libgettextlib-0.14.1.so
	@cp $(FILEDIR)/libintl.so.2.s $(INSTALLISADIR)/opt/csw/lib/libintl.so.2
	@cp $(FILEDIR)/libintl.so.3.s $(INSTALLISADIR)/opt/csw/lib/libintl.so.3

post-install-isa-sparcv9:
	@cp $(FILEDIR)/libgettextlib-0.14.1.so.s9 $(INSTALLISADIR)/opt/csw/lib/64/libgettextlib-0.14.1.so
	@cp $(FILEDIR)/libintl.so.2.s9 $(INSTALLISADIR)/opt/csw/lib/64/libintl.so.2
	@cp $(FILEDIR)/libintl.so.3.s9 $(INSTALLISADIR)/opt/csw/lib/64/libintl.so.3

post-install-isa-i386:
	@cp $(FILEDIR)/libgettextlib-0.14.1.so.i $(INSTALLISADIR)/opt/csw/lib/libgettextlib-0.14.1.so
	@cp $(FILEDIR)/libintl.so.2.i $(INSTALLISADIR)/opt/csw/lib/libintl.so.2
	@cp $(FILEDIR)/libintl.so.3.i $(INSTALLISADIR)/opt/csw/lib/libintl.so.3
