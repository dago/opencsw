GARNAME = libxslt
GARVERSION = 1.1.24
CATEGORIES = lib

DESCRIPTION = XSLT engine for the XML Toolkit
define BLURB
  Libxslt is the XSLT C library developed for the GNOME project. XSLT itself is a an XML language to define transformation for XML. Libxslt is based on libxml2 the XML C library developed for the GNOME project. It also implements most of the EXSLT set of processor-portable extensions functions and some of Saxon's evaluate and expressions extensions.
endef

MASTER_SITES = ftp://xmlsoft.org/libxslt/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibxslt,prototype)

PREREQUISITE_PKGS = CSWlibxml2 CSWlibxml2devel
TEST_TARGET = check

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
