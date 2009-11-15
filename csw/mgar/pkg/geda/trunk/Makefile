# 2009-11-15: Building successfully against svn version of guile, the 
#             current version in GAR is too old. Getting messages like these when
#             starting:
#             Read system config file [/opt/csw/share/gEDA/system-gafrc]
#             Read system config file [/opt/csw/share/gEDA/system-gschemrc]
#             Read init scm file [/opt/csw/share/gEDA/scheme/gschem.scm]
#             Should probably find a way to move the configuration files under 
#             /etc/opt/csw.
#                                                                    - Trygve

GARNAME = geda
GARVERSION = 1.6.0
CATEGORIES = devel

DESCRIPTION = The gEDA suite with gschem, gattrib, gnetlist, gsch2pcb, gsymcheck and libgeda
define BLURB
endef

MASTER_SITES = http://geda.seul.org/release/v1.6/1.6.0/
DISTFILES  = geda-gaf-$(GARVERSION).tar.gz

WORKSRC = $(WORKDIR)/geda-gaf-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = geda-gaf-(\d+(?:\.\d+)*).tar.gz
# That pattern won't work, geda has a funny major.minor/major.minor.micro 
# layout, see MASTER_SITES - trygve

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
GARCOMPILER = GCC4
CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
