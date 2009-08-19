GARNAME = libxml2
GARVERSION = 2.7.3
CATEGORIES = lib

DESCRIPTION = XML Parser Library
define BLURB
  Libxml2 is the XML C parser and toolkit developed for the Gnome project.
endef

MASTER_SITES = ftp://xmlsoft.org/libxml2/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxml2 CSWlibxml2devel CSWpylibxml2

CATALOGNAME_CSWlibxml2 = libxml2
CATALOGNAME_CSWlibxml2devel = libxml2_devel
CATALOGNAME_CSWpylibxml2 = pylibxml2

REQUIRED_PKGS_CSWlibxml2 = CSWiconv CSWzlib
REQUIRED_PKGS_CSWlibxml2devel = CSWlibxml2
REQUIRED_PKGS_CSWpylibxml2 = CSWpython CSWlibxml2

# We don't have 64 bit Python yet
CONFIGURE_ARGS_32 = --with-python=$(prefix)
CONFIGURE_ARGS_64 = --without-python

EXTRA_CPPFLAGS  = -DXML_XML_DEFAULT_CATALOG=\\\"$(sysconfdir)/xml/catalog\\\"
EXTRA_CPPFLAGS += -DXML_SGML_DEFAULT_CATALOG=\\\"$(sysconfdir)/sgml/catalog\\\"

CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1
NO_ISAEXEC = 1

# Skip 64 bit binaries - they are just big and gain nothing
MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amd64 = $(libdir)

EXTRA_PAX_ARGS  = -s ",^\.$(docdir)/libxml2-$(GARVERSION),.$(docdir)/libxml2,p"
EXTRA_PAX_ARGS += -s ",^\.$(docdir)/libxml2-python-$(GARVERSION),.$(docdir)/pylibxml2,p"
EXTRA_PAX_ARGS += -s ",^\.$(libdir)/python[^/]*,.$(libdir)/python,p"

PKGFILES_CSWlibxml2devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxml2devel += $(docdir)/libxml2/.*
PKGFILES_CSWlibxml2devel += $(sharedstatedir)/gtk-doc/.*
PKGFILES_CSWlibxml2devel += $(libdir)/xml2Conf.sh
PKGFILES_CSWlibxml2devel += $(call isadirs,$(libdir),xml2Conf.sh)

PKGFILES_CSWpylibxml2  = $(libdir)/python/.*
PKGFILES_CSWpylibxml2 += $(docdir)/pylibxml2/.*

include gar/category.mk

