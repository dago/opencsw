GARNAME = docbookdsssl
GARVERSION = 1.79
PATCHLEVEL = 4.1
CATEGORIES = xtra

DESCRIPTION = Norman Walsh's modular stylesheets for DocBook
define BLURB
These DSSSL stylesheets allow to convert any DocBook document to another
printed (for example, RTF or PostScript) or online (for example, HTML)
format.  They are highly customizable.
endef

SF_PROJ = docbook
MASTER_SITES = $(SF_MIRRORS)
DISTFILES = docbook-dsssl-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWdocbookdsssl,)

REQUIRED_PKGS = CSWdocbookdtds CSWsgmlcommon CSWopenjade

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

#nothing to configure or test
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = DESTDIR=$(DESTDIR) VERSION=$(GARVERSION)-$(PATCHLEVEL)
BUILD_ARGS += bindir=$(bindir) datadir=$(datadir)

include gar/category.mk
