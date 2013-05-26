# $Id$
#
# ! There are test failures, unfortunately.

NAME = libxml2
VERSION = 2.9.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = XML Parser Library
define BLURB
  Libxml2 is the XML C parser and toolkit developed for the Gnome project.
endef

MASTER_SITES = ftp://xmlsoft.org/libxmlDISTNAME).tar.gz
# PATCHFILES = 0001-Forcefully-disable-the-symbol-versioning.patch

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw --without-python

EXTRA_CPPFLAGS  = -DXML_XML_DEFAULT_CATALOG=\\\"$(sysconfdir)/xml/catalog\\\"
EXTRA_CPPFLAGS += -DXML_SGML_DEFAULT_CATALOG=\\\"$(sysconfdir)/sSWiconv CSWzlib

# We don't have 64 bit Python yet
CONFIGURE_ARGS_32 = --with-python=$(prefix)
CONFIGURE_ARGS_64 = -CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64_LIBS_ONLY = 1

PYCOMPILE = 1

STRIP_LIBTOOL = 1

PACKAGES += CSWlibxml2-2
OBSOLETED_BY_CSWlibxml2-2 = CSWlibxml2
SPKG_DESC_CSWlibxml2-2   = XML Parser Library
RUNTIME_DEP_PKGS_CSWlibxml2-2 += CSWliblzma5
RUNTIME_DEP_PKGS_CSWlibxml2-2 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibxml2-2 += CSWlibz1
# The catch-all package.

PACKAGES += CSWlibxml2-dev
OBSOLETED_BY_CSWlibxml2-dev = CSWlibxml2devel
SPKG_DESC_CSWlibxml2-dev = XML Parser Library Developer Files
RUNTIME_DEP_PKGS_CSWlibxml2-dev = CSWlibxml2-2ibdir)/python,p"

PKGFILES_CSWlibxml2-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxml2-dev += $(docdir)/libxml2/.*
PKGFILES_CSWlibxml2-dev += $(sharedstatedir)/gtk-doc/.*
PKGFILES_CSWlibxml2-dev += $(libdir)/xml2Conf.sh
PKGFILES_CSWlibxml2-dev += $(call isadirs,$(libdirACKAGES += CSWpy-libxml2
OBSOLETED_BY_CSWpy-libxml2 = CSWpylibxml2
SPKG_DESC_CSWpy-libxml2  = XML Parser Library Python Bindings
RUNTIME_DEP_PKGS_CSWpy-libxml2  = CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-libxml2 += CSWpython
RUNTIME_DEP_PKGS_CSWpy-libxml2 += CSWlibxml2-2
PKGFILES_CSWpy-libxml2  = $(libdir)/python/.*
PKGFILES_CSWpy-libxml2 += $(docdir)/pylibxml2/.*u# There is no 64-bit Python.
CHECKPKG_OVERRIDES_CSWpy-libxml2 += 64-bit-binaries-missingult64 = $(libdir)

EXTRA_PAX_ARGS  = -s ",^\.$(docdir)/libxml2-$(VERSION),.$(docdir)/libxml2,p"
EXTRA_PAX_ARGS += -s ",^\.$(docdir)/libxml2-python-$(VERSION),.$(docdir)/pylibxml2,p"
EXTRA_PAX_ARGS += -s ",^\.$(libdir)/python[^/]*,.$(lir)/pylibxml2/.*

CHECKPKG_OVERRIDES_CSWlibxml2-dev += file-with-bad-content|/usr/share|root/opt/csw/share/doc/libxml# http://lists.opencsw.org/pipermail/maintainers/2011-August/015093.html
SKIPTEST = 1

include gar/category.mk
