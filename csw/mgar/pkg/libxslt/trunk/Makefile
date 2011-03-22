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

PACKAGES = CSWlibxslt CSWlibxslt-dev CSWpy-libxslt

PACKAGES += CSWlibexslt0
CATALOGNAME_CSWlibexslt0 = libexslt0
PKGFILES_CSWlibexslt0 += $(call baseisadirs,$(libdir),libexslt\.so\.0\.8\.15)
PKGFILES_CSWlibexslt0 += $(call baseisadirs,$(libdir),libexslt\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibexslt0 += XSLT engine runtime package, libexslt.so.0
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWgpgerr
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibexslt0 += CSWgcrypt

PACKAGES += CSWlibxslt1
CATALOGNAME_CSWlibxslt1 = libxslt1
PKGFILES_CSWlibxslt1 += $(call baseisadirs,$(libdir),libxslt\.so\.1\.1\.26)
PKGFILES_CSWlibxslt1 += $(call baseisadirs,$(libdir),libxslt\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibxslt1 += XSLT engine runtime package, libxslt.so.1
RUNTIME_DEP_PKGS_CSWlibxslt1 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibxslt1 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibxslt1 += CSWzlib

RUNTIME_DEP_PKGS_CSWlibxslt += CSWlibxslt1

OBSOLETES_CSWpy-libxslt = CSWpylibxslt
OBSOLETES_CSWlibxslt-dev = CSWlibxsltdevel

CATALOGNAME_CSWlibxslt-dev = libxslt_dev
CATALOGNAME_CSWpy-libxslt = py_libxslt

BUILD_DEP_PKGS = CSWlibxml2 CSWlibxml2devel

SPKG_DESC_CSWlibxslt =  XSLT engine runtime package
SPKG_DESC_CSWlibxslt-dev = XSLT engine development package
SPKG_DESC_CSWpy-libxslt = XSLT engine python package

SPKG_SOURCEURL = http://xmlsoft.org/XSLT/
TEST_TARGET = check

CONFIGURE_ARGS_32 =
CONFIGURE_ARGS_64 = --without-python
CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1
NOISAEXEC = 1
STRIP_LIBTOOL = 1
PYCOMPILE = 1

RUNTIME_DEP_PKGS_CSWlibxslt = CSWgcrypt CSWgpgerr CSWiconv CSWlibxml2 CSWzlib
RUNTIME_DEP_PKGS_CSWlibxslt += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibxslt += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWlibxslt-dev = CSWlibxslt
RUNTIME_DEP_PKGS_CSWlibxslt-dev += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibxslt-dev += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWpy-libxslt  = CSWpython
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibxml2
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWzlib
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWgpgerr
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWgcrypt
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWiconv

PKGFILES_CSWlibxslt-dev  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxslt-dev += $(docdir)/libxslt-$(VERSION)/.*
PKGFILES_CSWlibxslt-dev += $(libdir)/xsltConf.sh
PKGFILES_CSWlibxslt-dev += $(call isadirs,$(libdir),xsltConf.sh)
PKGFILES_CSWpy-libxslt = $(libdir)/python.*
PKGFILES_CSWpy-libxslt += $(docdir)/libxslt-python-$(VERSION)/.*

include gar/category.mk

post-merge:
	@echo Correcting DTD reference in tutorial materials.
	@( cd $(PKGROOT)$(docdir)/$(NAME)-$(VERSION)/html/tutorial2/; \
		perl -pi -e 's!/usr/share!/opt/csw/share!' libxslt_pipes.xml)
	@$(MAKECOOKIE)
