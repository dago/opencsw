NAME = libxslt
VERSION = 1.1.26
CATEGORIES = lib

DESCRIPTION = XSLT engine for the XML Toolkit

define BLURB
	Libxslt is the XSLT C library developed for the GNOME project. XSLT itself is a an XML language to define transformation for XML. Libxslt is based on libxml2 the XML C library developed for the GNOME project. It also implements most of the EXSLT set of processor-portable extensions functions and some of Saxon's evaluate and expressions extensions.
endef

MASTER_SITES = ftp://xmlsoft.org/libxslt/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES += 0001-Forcefully-disable-version-script-use.patch

BUILD_DEP_PKGS = CSWlibxml2-dev CSWlibgcrypt-dev

PACKAGES = CSWlibxslt
SPKG_DESC_CSWlibxslt =  XSLT engine runtime package
CATALOGNAME_CSWlibxslt = libxslt
RUNTIME_DEP_PKGS_CSWlibxslt += CSWlibgcrypt11 CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibxslt += CSWiconv CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibxslt += CSWzlib
RUNTIME_DEP_PKGS_CSWlibxslt += CSWlibxslt1 CSWlibexslt0

PACKAGES += CSWlibxslt-dev
CATALOGNAME_CSWlibxslt-dev = libxslt_dev
SPKG_DESC_CSWlibxslt-dev = XSLT engine development package
OBSOLETED_BY_CSWlibxslt-dev = CSWlibxsltdevel
RUNTIME_DEP_PKGS_CSWlibxslt-dev = CSWlibxslt
RUNTIME_DEP_PKGS_CSWlibxslt-dev += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibxslt-dev += CSWlibexslt0
PKGFILES_CSWlibxslt-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxslt-dev += $(docdir)/libxslt-$(VERSION)/.*
PKGFILES_CSWlibxslt-dev += $(libdir)/xsltConf.sh
PKGFILES_CSWlibxslt-dev += $(call isadirs,$(libdir),xsltConf.sh)

PACKAGES += CSWpy-libxslt
CATALOGNAME_CSWpy-libxslt = py_libxslt
SPKG_DESC_CSWpy-libxslt = XSLT engine python package
OBSOLETED_BY_CSWpy-libxslt = CSWpylibxslt
RUNTIME_DEP_PKGS_CSWpy-libxslt  = CSWpython
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWzlib
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWiconv
PKGFILES_CSWpy-libxslt = $(libdir)/python.*
PKGFILES_CSWpy-libxslt += $(docdir)/libxslt-python-$(VERSION)/.*

PACKAGES += CSWlibexslt0
CATALOGNAME_CSWlibexslt0 = libexslt0
PKGFILES_CSWlibexslt0 += $(call baseisadirs,$(libdir),libexslt\.so\.0\.8\.15)
PKGFILES_CSWlibexslt0 += $(call baseisadirs,$(libdir),libexslt\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibexslt0 += XSLT engine runtime package, libexslt.so.0
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWlibgcrypt11

PACKAGES += CSWlibxslt1
CATALOGNAME_CSWlibxslt1 = libxslt1
PKGFILES_CSWlibxslt1 += $(call baseisadirs,$(libdir),libxslt\.so\.1\.1\.26)
PKGFILES_CSWlibxslt1 += $(call baseisadirs,$(libdir),libxslt\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibxslt1 += XSLT engine runtime package, libxslt.so.1
RUNTIME_DEP_PKGS_CSWlibxslt1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibxslt1 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibxslt1 += CSWzlib

SPKG_SOURCEURL = http://xmlsoft.org/XSLT/
TEST_TARGET = check

CONFIGURE_ARGS_32 =
CONFIGURE_ARGS_64 = --without-python
CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1
STRIP_LIBTOOL = 1
PYCOMPILE = 1

include gar/category.mk

post-merge:
	@echo Correcting DTD reference in tutorial materials.
	@( cd $(PKGROOT)$(docdir)/$(NAME)-$(VERSION)/html/tutorial2/; \
		perl -pi -e 's!/usr/share!/opt/csw/share!' libxslt_pipes.xml)
	@$(MAKECOOKIE)
