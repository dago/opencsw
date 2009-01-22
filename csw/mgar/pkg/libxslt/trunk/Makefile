GARNAME = libxslt
GARVERSION = 1.1.24
CATEGORIES = lib

DESCRIPTION = XSLT engine for the XML Toolkit

define BLURB
	Libxslt is the XSLT C library developed for the GNOME project. XSLT itself is a an XML language to define transformation for XML. Libxslt is based on libxml2 the XML C library developed for the GNOME project. It also implements most of the EXSLT set of processor-portable extensions functions and some of Saxon's evaluate and expressions extensions.
endef

MASTER_SITES = ftp://xmlsoft.org/libxslt/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibxslt,)
DISTFILES += $(call admfiles,CSWlibxsltdevel,)
DISTFILES += $(call admfiles,CSWpylibxslt,

PREREQUISITE_PKGS = CSWlibxml2 CSWlibxml2devel

SPKG_DESC_CSWlibxslt =  XSLT engine runtime package
SPKG_DESC_CSWlibxsltdevel = XSLT engine development package
SPKG_DESC_CSWpylibxslt = XSLT engine python package

SPKG_SOURCEURL = http://xmlsoft.org/XSLT/
TEST_TARGET = check

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_AGGS_32 =
CONFIGURE_ARGS_64 = --without-python
CONFIGURE_ARGS = $(DIRPATHS) $(CONFIGURE_ARGS_$(MEMORYMODEL))

BUILD64 = 1
NO_ISAEXEC = 1

REQUIRED_PKGS_CSWlibxslt = CSWgcrypt CSWgpgerr CSWiconv CSWlibxml2 CSWzlib
REQUIRED_PKGS_CSWlibxsltdevel = CSWlibxslt
REQUIRED_PKGS_CSWpylibxslt = CSWpython CSWlibxslt

PKGFILES_CSWlibxsltdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibxsltdevel += $(docdir)/libxslt-$(GARVERSION)/.*
PKGFILES_CSWlibxsltdevel += $(libdir)/xsltConf.sh
PKGFILES_CSWlibxsltdevel += $(call isadirs,$(libdir),xsltConf.sh)
PKGFILES_CSWpylibxslt = $(libdir)/python.*
PKGFILES_CSWpylibxslt += $(docdir)/libxslt-python-$(GARVERSION)/.*

include gar/category.mk
