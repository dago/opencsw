NAME = libxml2
VERSION = 2.7.7
CATEGORIES = lib

DESCRIPTION = XML Parser Library
define BLURB
  Libxml2 is the XML C parser and toolkit developed for the Gnome project.
endef

MASTER_SITES = ftp://xmlsoft.org/libxml2/
DISTFILES = $(NAME)-$(VERSION).tar.gz
PATCHFILES = ld-symbol-handling-fixup.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibxml2-2 CSWlibxml2devel CSWpy-libxml2

OBSOLETS_CSWlibxml2-2 = CSWlibxml2
OBSOLETES_CSWpy-libxml2 = CSWpylibxml2
OBSOLETES_CSWlibxml2-dev = CSWlibxml2devel

CATALOGNAME_CSWlibxml2-2 = libxml2_2
CATALOGNAME_CSWlibxml2-dev = libxml2_dev
CATALOGNAME_CSWpy-libxml2 = py_libxml2

SPKG_DESC_CSWlibxml2      = XML Parser Library
SPKG_DESC_CSWlibxml2-dev = XML Parser Library Developer Files
SPKG_DESC_CSWpy-libxml2    = XML Parser Library Python Bindings

RUNTIME_DEP_PKGS_CSWlibxml2 = CSWiconv CSWzlib
RUNTIME_DEP_PKGS_CSWlibxml2-dev = CSWlibxml2
RUNTIME_DEP_PKGS_CSWpy-libxml2  = CSWlibpython2-6-1-0 CSWlibxml2
RUNTIME_DEP_PKGS_CSWpy-libxml2 += CSWiconv CSWzlib

# We don't have 64 bit Python yet
CONFIGURE_ARGS_32 = --with-python=$(prefix)
CONFIGURE_ARGS_64 = --without-python

EXTRA_CPPFLAGS  = -DXML_XML_DEFAULT_CATALOG=\\\"$(sysconfdir)/xml/catalog\\\"
EXTRA_CPPFLAGS += -DXML_SGML_DEFAULT_CATALOG=\\\"$(sysconfdir)/sgml/catalog\\\"

CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1
NOISAEXEC = 1

PYCOMPILE = 1

STRIP_LIBTOOL = 1

# Skip 64 bit binaries - they are just big and gain nothing
MERGE_SCRIPTS_isa-default64 = copy-relocated-only copy-config-only
MERGE_DIRS_isa-default64 = $(libdir)

EXTRA_PAX_ARGS  = -s ",^\.$(docdir)/libxml2-$(VERSION),.$(docdir)/libxml2,p"
EXTRA_PAX_ARGS += -s ",^\.$(docdir)/libxml2-python-$(VERSION),.$(docdir)/pylibxml2,p"
EXTRA_PAX_ARGS += -s ",^\.$(libdir)/python[^/]*,.$(libdir)/python,p"

PKGFILES_CSWlibxml2-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxml2-dev += $(docdir)/libxml2/.*
PKGFILES_CSWlibxml2-dev += $(sharedstatedir)/gtk-doc/.*
PKGFILES_CSWlibxml2-dev += $(libdir)/xml2Conf.sh
PKGFILES_CSWlibxml2-dev += $(call isadirs,$(libdir),xml2Conf.sh)

PKGFILES_CSWpy-libxml2  = $(libdir)/python/.*
PKGFILES_CSWpy-libxml2 += $(docdir)/pylibxml2/.*

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

# override checkpkg for this
CHECKPKG_OVERRIDES_CSWlibxml2-dev += surplus-dependency|CSWlibxml2

include gar/category.mk

