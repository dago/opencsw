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

PACKAGES = CSWlibxslt CSWlibxsltdevel CSWpy-libxslt

OBSOLETES_CSWpy-libxslt = CSWpylibxslt

CATALOGNAME_CSWlibxsltdevel = libxslt_devel
CATALOGNAME_CSWpy-libxslt = py_libxslt

BUILD_DEP_PKGS = CSWlibxml2 CSWlibxml2devel

SPKG_DESC_CSWlibxslt =  XSLT engine runtime package
SPKG_DESC_CSWlibxsltdevel = XSLT engine development package
SPKG_DESC_CSWpy-libxslt = XSLT engine python package

SPKG_SOURCEURL = http://xmlsoft.org/XSLT/
TEST_TARGET = check

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS_32 =
CONFIGURE_ARGS_64 = --without-python
CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1
NOISAEXEC = 1
STRIP_LIBTOOL = 1
PYCOMPILE = 1

RUNTIME_DEP_PKGS_CSWlibxslt = CSWgcrypt CSWgpgerr CSWiconv CSWlibxml2 CSWzlib
RUNTIME_DEP_PKGS_CSWlibxsltdevel = CSWlibxslt
RUNTIME_DEP_PKGS_CSWpy-libxslt  = CSWpython
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibxslt
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWlibxml2
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWzlib
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWgpgerr
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWgcrypt
RUNTIME_DEP_PKGS_CSWpy-libxslt += CSWiconv


PKGFILES_CSWlibxsltdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxsltdevel += $(docdir)/libxslt-$(VERSION)/.*
PKGFILES_CSWlibxsltdevel += $(libdir)/xsltConf.sh
PKGFILES_CSWlibxsltdevel += $(call isadirs,$(libdir),xsltConf.sh)
PKGFILES_CSWpy-libxslt = $(libdir)/python.*
PKGFILES_CSWpy-libxslt += $(docdir)/libxslt-python-$(VERSION)/.*

CHECKPKG_OVERRIDES_CSWlibxsltdevel += surplus-dependency|CSWlibxslt

include gar/category.mk
